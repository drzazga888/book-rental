$(document).ready(function() {
	$("#addressSwitcher").change(function() {
        var billingAddress = $(".billing-address");
        billingAddress.find('input').not(this).attr("disabled", !this.checked);
        if (this.checked)
            billingAddress.children(".hideable").show(200);
        else
            billingAddress.children(".hideable").hide(200);
	}).change();
});