let index = 0;

const slides = document.querySelectorAll(".slide");
const btnDerecha = document.querySelector(".derecha");
const btnIzquierda = document.querySelector(".izquierda");

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