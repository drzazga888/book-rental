var basket;
var recentlyViewed;

$(document).ready(function(){
	basket = new Basket("basket");
	recentlyViewed = new RecentlyViewed("recently-viewed");
	basket.show();
	recentlyViewed.show();
});

$('.dropdown-menu').click(function(e) {
    e.stopPropagation();
});

$("#total-area").find(".additional-price").change(function() {
    Basket.refreshPrice();
});