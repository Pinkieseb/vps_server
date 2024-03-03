document.addEventListener('DOMContentLoaded', function() {
    var navToggle = document.createElement('a');
    navToggle.innerHTML = '&#9776;'; // Hamburger icon
    navToggle.style.fontSize = '30px';
    navToggle.style.cursor = 'pointer';
    navToggle.style.color = 'white';
    navToggle.style.padding = '10px';
    navToggle.onclick = function() {
        var links = document.querySelectorAll('nav ul li');
        for (var i = 0; i < links.length; i++) {
            if (links[i].style.display === 'block') {
                links[i].style.display = 'none';
            } else {
                links[i].style.display = 'block';
            }
        }
    };

    var nav = document.querySelector('nav');
    nav.insertBefore(navToggle, nav.childNodes[0]);
});