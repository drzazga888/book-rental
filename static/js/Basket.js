Basket = function(localStorageName) {
	this.localStorageName = localStorageName;
	if (!localStorage[localStorageName])
		localStorage[localStorageName] = JSON.stringify([]);
};

Basket.prototype.add = function(book) {
	var books = this.get();
	if (this.indexOf(book.id, books) !== undefined) {
		console.warn("Nie można dodać książki która już istnieje");
		return;
	}
	books.push(book);
	localStorage.setItem(this.localStorageName, JSON.stringify(books));
};

Basket.prototype.get = function() {
	return JSON.parse(localStorage.getItem(this.localStorageName));
};

Basket.prototype.remove = function(bookID) {
	var books = this.get();
	var bookToRemoveIndex = this.indexOf(bookID, books);
	if (bookToRemoveIndex === undefined) {
		console.warn("Książka o podanym ID nie istnieje i nie można ją usunąć");
		return;
	}
	books.splice(bookToRemoveIndex, 1);
	localStorage.setItem(this.localStorageName, JSON.stringify(books));
};

Basket.prototype.indexOf = function(bookID, books) {
	for (var i = 0; i < books.length; ++i) {
		if (books[i].id == bookID)
			return i;
	}
	return undefined;
};

Basket.prototype.show = function() {
	var books = basket.get();
	var form = $(".basket");
	var basketInfo = form.children(".dropdown-toggle");
	basketInfo.children(".basket-item-count").children(".count").text(books ? books.length : 0);
	var bookContainer = form.children(".dropdown-menu");
	bookContainer.children().not(".checkout").remove();
	var totalPrice = Number(0);
	if (books.length > 0) {
		for (var i = books.length - 1; i >= 0; --i) {
			totalPrice += Number(books[i].price.replace(",", "."));
			var toPrepend = this.stringify(books[i]);
			bookContainer.prepend(toPrepend);
		}
	}
	else
		bookContainer.prepend('<li><p class="basket-item">Brak książek w koszyku</p></li>');
	totalPrice = totalPrice.toFixed(2);
	basketInfo.children(".total-price-basket").children(".total-price").children(".value").text(totalPrice);
};

Basket.prototype.stringify = function(book) {
	return '\
		<li>\
			<div class="basket-item book-container" data-book-id="' + book.id + '">\
				<div class="row">\
					<div class="col-xs-4 col-sm-4 text-center fit-me">\
						<div class="thumb fit-me">\
							<img alt="" src="/static/books/' + book.id + '.jpg" />\
						</div>\
					</div>\
					<div class="col-xs-8 col-sm-8">\
						<div class="title book-title">' + book.title + '</div>\
						<div class="author book-author">' + book.author + '</div>\
						<div class="price book-price">' + book.price + ' PLN</div>\
					</div>\
				</div>\
				<a class="close-btn" href="javascript:void(0);" onclick="Book.remove(event, basket)"></a>\
			</div>\
		</li>\
	';
};