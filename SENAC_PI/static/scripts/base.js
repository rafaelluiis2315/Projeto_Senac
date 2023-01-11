// Navbar dinamica
const indicator = document.querySelector('.nav-indicator');
const items = document.querySelectorAll('.nav-item');

const url_atual = window.location.href;
console.log(url_atual);

items.forEach(element => {
	let elementLink = element.getAttribute('href');
	console.log(elementLink.replace('/', ''));
});

const clickedElement = 'a';

function defaultActiveLink() {
	items[3].classList.add('is-active');
	indicator.style.width = `${items[3].offsetWidth}px`;
	indicator.style.left = `${items[3].offsetLeft}px`;
	indicator.style.backgroundColor = items[3].getAttribute('active-color');
};

defaultActiveLink();
