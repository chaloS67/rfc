let index = 0;

const slides = document.querySelectorAll(".actividades-slide");
const btnDerecha = document.querySelector(".carousel-btn.right");
const btnIzquierda = document.querySelector(".carousel-btn.left");

if(slides.length > 0 && btnDerecha && btnIzquierda){

    function actualizarCarrusel(){

        slides.forEach(slide => {
            slide.classList.remove("activo", "anterior", "siguiente");
        });

        slides[index].classList.add("activo");

        const anterior = (index - 1 + slides.length) % slides.length;
        const siguiente = (index + 1) % slides.length;

        slides[anterior].classList.add("anterior");
        slides[siguiente].classList.add("siguiente");
    }

    btnDerecha.addEventListener("click", () => {
        index = (index + 1) % slides.length;
        actualizarCarrusel();
    });

    btnIzquierda.addEventListener("click", () => {
        index = (index - 1 + slides.length) % slides.length;
        actualizarCarrusel();
    });

    actualizarCarrusel();
}

const btnMenu = document.getElementById("btn-menu");
const menu = document.getElementById("menu");

if(btnMenu && menu){
    btnMenu.addEventListener("click", () => {
        menu.classList.toggle("activo");
    });
}

const imagenes = document.querySelectorAll(
    ".foto-galeria, .actividades-img"
);

const modal = document.getElementById("modal");
const imagenModal = document.getElementById("imagen-modal");
const cerrar = document.querySelector(".cerrar");

if(modal && imagenModal && cerrar){

    imagenes.forEach(imagen => {

        imagen.addEventListener("click", () => {

            modal.style.display = "flex";
            imagenModal.src = imagen.src;

        });

    });

    cerrar.addEventListener("click", () => {
        modal.style.display = "none";
    });

    modal.addEventListener("click", (e) => {
        if(e.target === modal){
            modal.style.display = "none";
        }
    });

}

/*======================================
CARRUSEL HOME
======================================*/

const heroSlides = document.querySelectorAll(".hero-slide");
const heroIndicadores = document.querySelectorAll(".hero-indicador");

let heroIndex = 0;
let heroIntervalo;


function mostrarHeroSlide(index){

    heroSlides.forEach(slide => {
        slide.classList.remove("activo");
    });

    heroIndicadores.forEach(indicador => {
        indicador.classList.remove("activo");
    });

    heroSlides[index].classList.add("activo");

    if(heroIndicadores[index]){
        heroIndicadores[index].classList.add("activo");
    }

}


function siguienteHeroSlide(){

    heroIndex++;

    if(heroIndex >= heroSlides.length){
        heroIndex = 0;
    }

    mostrarHeroSlide(heroIndex);

}


function iniciarHeroCarrusel(){

    if(heroSlides.length <= 1){
        return;
    }

    heroIntervalo = setInterval(
        siguienteHeroSlide,
        5000
    );

}


if(heroSlides.length > 0){

    heroIndicadores.forEach((indicador, index) => {

        indicador.addEventListener("click", () => {

            heroIndex = index;

            mostrarHeroSlide(heroIndex);

            clearInterval(heroIntervalo);

            iniciarHeroCarrusel();

        });

    });

    mostrarHeroSlide(heroIndex);

    iniciarHeroCarrusel();

}

const comienzosSlides = document.querySelectorAll(".comienzos-slide");
const comienzosIndicadores = document.querySelectorAll(".comienzos-indicador");

let comienzosIndex = 0;

function mostrarComienzosSlide(index){

    comienzosSlides.forEach(slide => {
        slide.classList.remove("activo");
    });

    comienzosIndicadores.forEach(indicador => {
        indicador.classList.remove("activo");
    });

    comienzosSlides[index].classList.add("activo");
    comienzosIndicadores[index].classList.add("activo");

    comienzosIndex = index;
}

comienzosIndicadores.forEach((indicador, index) => {

    indicador.addEventListener("click", () => {
        mostrarComienzosSlide(index);
    });

});

const entrenadoresCarousel = document.getElementById("entrenadores-carousel");
const entrenadoresPrev = document.getElementById("entrenadores-prev");
const entrenadoresNext = document.getElementById("entrenadores-next");

if(entrenadoresCarousel && entrenadoresPrev && entrenadoresNext){

    entrenadoresNext.addEventListener("click", () => {

        entrenadoresCarousel.scrollBy({
            left:300,
            behavior:"smooth"
        });

    });

    entrenadoresPrev.addEventListener("click", () => {

        entrenadoresCarousel.scrollBy({
            left:-300,
            behavior:"smooth"
        });

    });

}