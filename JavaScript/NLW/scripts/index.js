const buttonSearch = document.querySelector("#page-home main a")
const modal = document.querySelector("#modal")
const close = document.querySelector("#modal .header a")


buttonSearch.addEventListener("click", () => {
    // remove mata uma classe com o nome dos parametros
    // do elemento referenciado
    modal.classList.remove("hide")
})

close.addEventListener("click", () => {
    modal.classList.add("hide")
})