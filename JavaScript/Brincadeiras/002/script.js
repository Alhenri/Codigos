var txtH = document.querySelector("input#txthor")
var txtM = document.querySelector("input#txtmin")
var txtS = document.querySelector("input#txtsec")
var txtTempo = document.querySelector("label#cont")
var tempo
function config(){
    tempo = Number(txtH.value)*3600 + Number(txtM.value)*60 + Number(txtS.value)
    console.log(txtS.value)
    txtH.value = ''
    txtM.value = ''
    txtS.value = ''
    contar()
}
function parar(){
    tempo = 0
}
function reset(){
    tempo = 1
}
function contar(){
    if(tempo <= 0){
        return
    }
    tempo--
    var H = Number.parseInt((tempo/3600))
    var M = Number.parseInt((tempo%3600)/60)
    var S = Number.parseInt((tempo%3600)%60)
    txtTempo.innerHTML = `Restam ${H} <b>horas</b> ${M} <b>minutos</b> e ${S} <b>segundos</b>.`
    
    
    setTimeout('contar()', 1000)
}