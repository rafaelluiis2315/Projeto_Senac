// Navbar dinamica
const indicator = document.querySelector('.nav-indicator');
const items = document.querySelectorAll('.nav-item');

const url_atual = window.location.href;

function defaultActiveLink() {
	items[0].classList.add('is-active');
	indicator.style.width = `${items[0].offsetWidth}px`;
	indicator.style.left = `${items[0].offsetLeft}px`;
	indicator.style.backgroundColor = items[0].getAttribute('active-color');
};

defaultActiveLink();
