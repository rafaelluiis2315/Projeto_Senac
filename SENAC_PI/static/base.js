// Active navbar
var navbar = document.getElementsByClassName('nav-link');

[...navbar].forEach(element => {
    element.addEventListener('click', function (Event) {
        [...navbar].forEach(elemento => {
            elemento.className = 'nav-link'
        });

        Event.target.classList.add('active');

    })
});
