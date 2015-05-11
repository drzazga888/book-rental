$(document).ready(function(){
    $("#perpageSwitcher").change(function(){
        location.href="/books/perpage/"+this.options[this.selectedIndex].value
    })
})