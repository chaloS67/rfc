let index = 0;

const slides = document.querySelectorAll(".slide");

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
        (index - 1 + slides.length)
        % slides.length;

    const siguiente =
        (index + 1)
        % slides.length;

    slides[anterior].classList.add("anterior");

    slides[siguiente].classList.add("siguiente");
}

document
.querySelector(".derecha")
.addEventListener("click", () => {

    index++;

    if(index >= slides.length){
        index = 0;
    }

    actualizarCarrusel();
});

document
.querySelector(".izquierda")
.addEventListener("click", () => {

    index--;

    if(index < 0){
        index = slides.length - 1;
    }

    actualizarCarrusel();
});

actualizarCarrusel();