/* ======================================
1. CARRUSEL ACTIVIDADES
====================================== */

let index = 0;

const slides = document.querySelectorAll(".actividades-slide");
const btnDerecha = document.querySelector(".carousel-btn.right");
const btnIzquierda = document.querySelector(".carousel-btn.left");

if(slides.length > 0 && btnDerecha && btnIzquierda){

    function actualizarCarrusel(){

        slides.forEach(slide => {
            slide.classList.remove(
                "activo",
                "anterior",
                "siguiente"
            );
        });

        slides[index].classList.add("activo");

        const anterior =
            (index - 1 + slides.length) % slides.length;

        const siguiente =
            (index + 1) % slides.length;

        slides[anterior].classList.add("anterior");
        slides[siguiente].classList.add("siguiente");
    }


    btnDerecha.addEventListener("click", () => {

        index = (index + 1) % slides.length;

        actualizarCarrusel();

    });


    btnIzquierda.addEventListener("click", () => {

        index =
            (index - 1 + slides.length) % slides.length;

        actualizarCarrusel();

    });


    actualizarCarrusel();
}


/* ======================================
2. MENU MOBILE
====================================== */

const btnMenu = document.getElementById("btn-menu");
const menu = document.getElementById("menu");

if(btnMenu && menu){

    btnMenu.addEventListener("click", () => {

        menu.classList.toggle("activo");

    });

}


/* ======================================
3. MODAL GALERIA
====================================== */

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


/* ======================================
4. HERO HOME
====================================== */

const heroSlides =
    document.querySelectorAll(".hero-slide");

const heroIndicadores =
    document.querySelectorAll(".hero-indicador");

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

        heroIndicadores[index]
            .classList.add("activo");

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

    heroIndicadores.forEach(
        (indicador, index) => {

            indicador.addEventListener(
                "click",
                () => {

                    heroIndex = index;

                    mostrarHeroSlide(heroIndex);

                    clearInterval(heroIntervalo);

                    iniciarHeroCarrusel();

                }
            );

        }
    );

    mostrarHeroSlide(heroIndex);

    iniciarHeroCarrusel();
}



/* ======================================
5. CARRUSEL NUESTROS COMIENZOS
====================================== */

const comienzosSlides =
    document.querySelectorAll(".comienzos-slide");

const comienzosIndicadores =
    document.querySelectorAll(".comienzos-indicador");

const comienzosPrev =
    document.querySelector(".comienzos-prev");

const comienzosNext =
    document.querySelector(".comienzos-next");

const comienzosCarousel =
    document.querySelector(".comienzos-carousel");

let comienzosIndex = 0;

let touchInicioX = 0;
let touchFinX = 0;


/* ======================================
MOSTRAR SLIDE
====================================== */

function mostrarComienzosSlide(index){

    comienzosSlides.forEach(slide => {
        slide.classList.remove("activo");
    });

    comienzosIndicadores.forEach(indicador => {
        indicador.classList.remove("activo");
    });

    comienzosSlides[index].classList.add("activo");

    if(comienzosIndicadores[index]){
        comienzosIndicadores[index].classList.add("activo");
    }

    comienzosIndex = index;
}


/* ======================================
INDICADORES
====================================== */

comienzosIndicadores.forEach(
    (indicador, index) => {

        indicador.addEventListener("click", () => {

            mostrarComienzosSlide(index);

        });

    }
);


/* ======================================
FLECHA SIGUIENTE
====================================== */

if(comienzosNext){

    comienzosNext.addEventListener("click", () => {

        let siguiente = comienzosIndex + 1;

        if(siguiente >= comienzosSlides.length){
            siguiente = 0;
        }

        mostrarComienzosSlide(siguiente);

    });

}


/* ======================================
FLECHA ANTERIOR
====================================== */

if(comienzosPrev){

    comienzosPrev.addEventListener("click", () => {

        let anterior = comienzosIndex - 1;

        if(anterior < 0){
            anterior = comienzosSlides.length - 1;
        }

        mostrarComienzosSlide(anterior);

    });

}


/* ======================================
SWIPE MOBILE
====================================== */

if(comienzosCarousel){

    comienzosCarousel.addEventListener(
        "touchstart",
        (e) => {

            touchInicioX =
                e.touches[0].clientX;

        },
        { passive:true }
    );


    comienzosCarousel.addEventListener(
        "touchend",
        (e) => {

            touchFinX =
                e.changedTouches[0].clientX;

            manejarSwipeComienzos();

        },
        { passive:true }
    );

}


/* ======================================
DETECTAR DIRECCION DEL SWIPE
====================================== */

function manejarSwipeComienzos(){

    const distancia =
        touchInicioX - touchFinX;

    const minimoSwipe = 50;


    /* desliza hacia izquierda */

    if(distancia > minimoSwipe){

        let siguiente =
            comienzosIndex + 1;

        if(siguiente >= comienzosSlides.length){
            siguiente = 0;
        }

        mostrarComienzosSlide(siguiente);

    }


    /* desliza hacia derecha */

    else if(distancia < -minimoSwipe){

        let anterior =
            comienzosIndex - 1;

        if(anterior < 0){
            anterior =
                comienzosSlides.length - 1;
        }

        mostrarComienzosSlide(anterior);

    }

}


/* ======================================
6. CARRUSEL ENTRENADORES
====================================== */

const entrenadoresCarousel =
    document.getElementById("entrenadores-carousel");

const entrenadoresPrev =
    document.getElementById("entrenadores-prev");

const entrenadoresNext =
    document.getElementById("entrenadores-next");

if(
    entrenadoresCarousel &&
    entrenadoresPrev &&
    entrenadoresNext
){

    function moverEntrenadores(direccion){

        const tarjeta =
            entrenadoresCarousel.querySelector(".entrenador-card");

        if(!tarjeta){
            return;
        }

        const estilos =
            getComputedStyle(entrenadoresCarousel);

        const gap =
            parseFloat(estilos.gap) || 0;

        const distancia =
            tarjeta.offsetWidth + gap;

        entrenadoresCarousel.scrollBy({
            left: distancia * direccion,
            behavior: "smooth"
        });
    }


    entrenadoresNext.addEventListener("click", () => {
        moverEntrenadores(1);
    });


    entrenadoresPrev.addEventListener("click", () => {
        moverEntrenadores(-1);
    });

    document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("entrenador-modal");
    const btnCerrar = document.getElementById("modal-cerrar-btn");
    const cards = document.querySelectorAll(".entrenador-card-clickable");

    const modalImg = document.getElementById("modal-profe-img");
    const modalNombre = document.getElementById("modal-profe-nombre");
    const modalDisciplina = document.getElementById("modal-profe-disciplina");
    const modalDias = document.getElementById("modal-profe-dias");
    const modalHorarios = document.getElementById("modal-profe-horarios");

    // Abrir modal con los datos de la tarjeta clickeada
    cards.forEach(card => {
        card.addEventListener("click", function () {
            modalNombre.textContent = this.dataset.nombre || "";
            modalDisciplina.textContent = this.dataset.disciplina || "";
            modalDias.textContent = this.dataset.dias || "A coordinar";
            modalHorarios.textContent = this.dataset.horarios || "A coordinar";

            if (this.dataset.foto) {
                modalImg.src = this.dataset.foto;
                modalImg.style.display = "block";
            } else {
                modalImg.style.display = "none";
            }

            modal.style.display = "flex";
            document.body.style.overflow = "hidden"; // Evita scroll de fondo
        });
    });

    // Cerrar con botón X
    btnCerrar.addEventListener("click", function () {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
    });

    // Cerrar haciendo clic fuera de la cajita modal
    modal.addEventListener("click", function (e) {
        if (e.target === modal) {
            modal.style.display = "none";
            document.body.style.overflow = "auto";
        }
    });

    // Cerrar con tecla Escape
    document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && modal.style.display === "flex") {
            modal.style.display = "none";
            document.body.style.overflow = "auto";
        }
    });
});

    

}