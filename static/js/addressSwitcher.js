$(document).ready(function() {
	$("#addressSwitcher").change(function() {
        var billingAddress = $(".billing-address");
        billingAddress.find('input').not(this).not($(".billing-address").find('input[name=phone]')).attr("disabled", !this.checked);
	}).change();
});