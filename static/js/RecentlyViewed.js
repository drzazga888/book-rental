RecentlyViewed = function(localStorageName) {
	Basket.call(this, localStorageName);
}

RecentlyViewed.prototype = Object.create(Basket.prototype);
RecentlyViewed.prototype.constructor = Basket;

RecentlyViewed.prototype.add = function(book) {
	this.remove(book.id);
	Basket.prototype.add.call(this, book);
	var books = this.get();
	if (books.length > 10) {
		books.shift();
		localStorage.setItem(this.localStorageName, JSON.stringify(books));
	}
};

RecentlyViewed.prototype.show = function() {
	var container;
	if ((container = $("#recently-reviewd")).length == 0)
		return;
	var owl = container.find("#owl-recently-viewed");
	var books = this.get();
	owl.data('owlCarousel').destroy();
	owl.children().remove();
	for (var i = 0; i < books.length; ++i)
		owl.prepend(this.stringify(books[i]));
	owl.owlCarousel({
   		stopOnHover: true,
		rewindNav: true,
		items: 6,
		pagination: false,
		itemsTablet: [768,3]
    });
};

RecentlyViewed.prototype.stringify = function(book) {
	var titleCropped = book.title;
	if (book.title.length > 40) {
		titleCropped = book.title.substr(0, 37);
		titleCropped += "...";
	}
	return '\
		<div class="no-margin carousel-item product-item-holder size-small hover">\
			<div class="product-item book-container" data-book-id="' + book.id + '"> \
				<div class="image">\
					<img alt="" src="/static/books/' + book.id + '.jpg" />\
				</div>\
				<div class="body">\
					<div class="title">\
						<a class="book-title" href="/books/book/' + book.id + '">' + titleCropped + '</a>\
					</div>\
					<div class="brand book-author">' + book.author + '</div>\
				</div>\
				<div class="prices">\
					<div class="book-price price-current text-right">' + book.price + ' PLN</div>\
				</div>\
				<div class="hover-area">\
					<div class="add-cart-button">\
						<a href="javascript:void(0);" onclick="Book.add(event, basket);" class="le-button">+ Koszyk</a>\
					</div>\
				</div>\
			</div>\
		</div>\
	';
};