$(document).ready(function() {
	$("#addressSwitcher").change(function() {
		if (this.checked)
			$(".billing-address").find('input').not(this).attr("disabled", false);
    	else
    		$(".billing-address").find('input').not(this).attr("disabled", true);
	}).change();
});