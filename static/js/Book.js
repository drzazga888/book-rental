/**
* Wymagana struktura elementu do
* odpowiedniego pobrania danych.
* [.book-container, data-book-id]
*  -> [.book-title]
*  -> [.book-author]
*  -> [.book-price]
*  -> [caller onclick=add(storage)]
*/

Book = function(id, title, author, price) {
	this.id = id;
	this.title = title;
	this.author = author;
	this.price = price;
}

Book.add = function(event, storage) {
	var caller = $(event.target);
	var bookContainer;
	if (!(storage instanceof RecentlyViewed))
		bookContainer = caller.closest(".book-container");
	else
		bookContainer = caller.find("#single-product");
	var book = new Book();
	book.id = bookContainer.data("book-id");
	book.title = bookContainer.find(".book-title").text();
	book.author = bookContainer.find(".book-author").text();
	book.price = bookContainer.find(".book-price").text().split(" ")[0].replace(' PLN', '').replace('PLN', '');
	storage.add(book);
	if (!(storage instanceof RecentlyViewed))
		storage.show();
}

Book.remove = function(event, storage) {
	var caller = $(event.target);
	var bookContainer = caller.closest(".book-container");
	var id = bookContainer.data("book-id");
	storage.remove(id);
	if (storage instanceof Basket)
		storage.show();
}