Basket = function(localStorageName) {
	this.localStorageName = localStorageName;
}

Basket.prototype.add = function(book) {
	var books = this.get();
	if (books == null)
		books = [];
	else if (this.indexOf(book.id, books) !== undefined) {
		console.warn("Nie można dodać książki która już istnieje");
		return;
	}
	books.push(book);
	localStorage.setItem(this.localStorageName, JSON.stringify(books));
};

Basket.prototype.get = function() {
	var books = localStorage.getItem(this.localStorageName);
	if (books)
		return JSON.parse(books);
	else
		return null;
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