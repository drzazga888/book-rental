RecentlyViewed = function(localStorageName) {
	Basket.call(this, localStorageName);
}

RecentlyViewed.prototype = Object.create(Basket.prototype);
RecentlyViewed.prototype.constructor = Basket;

RecentlyViewed.prototype.add = function(bookID) {
	Basket.prototype.add.call(this, bookID);
	var books = this.get();
	if (books.length > 10)
	{
		books.shift();
		localStorage.setItem(this.localStorageName, JSON.stringify(books));
	}
};