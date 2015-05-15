var basket;
var recentlyViewed;

$(document).ready(function(){
	basket = new Basket("basket");
	recentlyViewed = new RecentlyViewed("recently-viewed");
	showBooksInBasket();
});

$('.dropdown-menu').click(function(e) {
    e.stopPropagation();
});

// BASKET

function addBookFromListToBasket(button) {
	button = $(button);
	var form = button.parent().parent().parent();
	var book = new Book();
	book.id = form.children(".image").children("img").attr("src").split("/")[3].split(".")[0];
	book.title = form.children(".body").children(".title").children("a").text();
	book.author = form.children(".body").children(".brand").text();
	book.price = form.children(".prices").children(".price-current").text().split(" ")[0];
	basket.add(book);
	showBooksInBasket();
}

function removeBookFromBasket(button) {
	var thumb = $(button).parent().children(".row").find(".thumb").children("img");
	var id = thumb.attr("src").split("/")[3].split(".")[0];
	basket.remove(id);
	showBooksInBasket();
}

function showBooksInBasket() {
	var books = basket.get();
	var form = $(".basket");
	var basketInfo = form.children(".dropdown-toggle");
	basketInfo.children(".basket-item-count").children(".count").text(books ? books.length : 0);
	var bookContainer = form.children(".dropdown-menu");
	bookContainer.children().not(".checkout").remove();
	var totalPrice = Number(0);
	if (books && books.length > 0) {
		for (var i = books.length - 1; i >= 0; --i) {
			totalPrice += Number(books[i].price.replace(",", "."));
			var toPrepend = getBasketElementString(books[i]);
			bookContainer.prepend(toPrepend);
		}
	}
	else
	{
		console.log("0");
		bookContainer.prepend('<li><p class="basket-item">Brak książek w koszyku</p></li>');
	}
	totalPrice = totalPrice.toFixed(2);
	basketInfo.children(".total-price-basket").children(".total-price").children(".value").text(totalPrice);
}

function getBasketElementString(book) {
	return '\
		<li>\
			<div class="basket-item">\
				<div class="row">\
					<div class="col-xs-4 col-sm-4 text-center fit-me">\
						<div class="thumb fit-me">\
							<img alt="" src="/static/books/' + book.id + '.jpg" />\
						</div>\
					</div>\
					<div class="col-xs-8 col-sm-8">\
						<div class="title">' + book.title + '</div>\
						<div class="author">' + book.author + '</div>\
						<div class="price">' + book.price + ' PLN</div>\
					</div>\
				</div>\
				<a class="close-btn" href="javascript:void(0);" onclick="removeBookFromBasket(this)"></a>\
			</div>\
		</li>\
	';
}

// RECENTLY VIEWED

function addBookToRecentlyViewed() {
	var recentlyViewedForm = $("#recently-viewed-add-form");
	if (!recentlyViewedForm[0].checkValidity()) {
		console.error(recentlyViewedForm[0].validationMessage);
		return;
	}
	var book = new Book();
	book.id = recentlyViewedForm.children(".id").val();
	book.title = recentlyViewedForm.children(".title").val();
	book.author = recentlyViewedForm.children(".author").val();
	book.price = recentlyViewedForm.children(".price").val();
	recentlyViewed.add(book);
}

function showBooksInRecentlyViewed() {
	var books = recentlyViewed.get();
	console.log(books);
}