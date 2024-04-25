function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}


window.onclick = function(event) {
  	if (!event.target.matches('.menu_button')) {
    // menu_button.style.background-image = url("../img/settings.png");
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      	var openDropdown = dropdowns[i];
      	if (openDropdown.classList.contains('show')) {
        	openDropdown.classList.remove('show');
      	}
    }
  }
}
