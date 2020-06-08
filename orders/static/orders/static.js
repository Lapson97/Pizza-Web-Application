window.onscroll = function() {myFunction()};

var navbar = document.getElementById("myNavbar");
var sticky = navbar.offsetTop;
console.log("test");
console.log("test");
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}