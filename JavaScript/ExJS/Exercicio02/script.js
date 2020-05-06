function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.querySelector('input#txtano')
    var res = document.querySelector('div#res')

    if(fano.value.length == 0 || fano.value > ano){
        window.alert('[ERRO] Verifique os dados e tente novamente')
    }else{
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var sexo = ''
        var img = document.createElement('img') //cria um elemento img no html
        img.setAttribute('id', 'foto') //coloca uma id='foto' no elemento criado
        img.setAttribute('width', '236') //padronizar o tamanho da imagem
        img.setAttribute('height', '236')
        if(fsex[0].checked){
            sexo = 'homem'
            if (idade < 12) {
                //criança
                img.setAttribute('src', 'ch.png')
            }else if(idade < 21){
                //Jovem
                img.setAttribute('src', 'jh.png')
            }else if(idade < 50){
                //Adulto
                img.setAttribute('src', 'ah.png')
            }else{
                //Idoso
                img.setAttribute('src', 'vh.png')
            }
        }else{
            sexo = 'mulher'
            if (idade < 12) {
                //criança
                img.setAttribute('src', 'cm.png')
            }else if(idade < 21){
                //Jovem
                img.setAttribute('src', 'jm.png')
            }else if(idade < 50){
                //Adulto
                img.setAttribute('src', 'am.png')
            }else{
                //Idoso
                img.setAttribute('src', 'vm.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${sexo} com ${idade} anos`
        res.appendChild(img)//adiciona o item img ao 'res'
    }
}