function contar(){
    var c_inicio = document.querySelector("input#txtini")
    var c_fim = document.querySelector("input#txtfim")
    var c_passo = document.querySelector("input#txtpas")

    var inicio = Number(c_inicio.value)
    var fim = Number(c_fim.value)
    var passo = Number(c_passo.value)

    var resposta = ''

    if(!inicio){
        window.alert("Defina um inicio e tente novamente")
    }
    else {
        if(passo == 0){
            window.alert("Passo inválido, continuarei a execução considerando como '1' ")
            passo = 1
        }
        //Contagem crescente
        if(passo > 0 && fim > inicio){
            for(var c=inicio; c<=fim; c += passo){
                if(c == fim || c+passo > fim){
                    resposta += `${c} Fim!`
                    break
                }
                resposta += `${c} \u{1F449} `
            }
        }
        //Contagem decrescente
        else if(passo < 0 && inicio > fim){
            for(var c=inicio; c>=fim; c += passo){
                if(c == fim || c+passo < fim){
                    resposta += `${c} Fim!`
                    break
                }
                resposta += `${c} \u{1F449} `
            }
        }else{
            resposta = 'Preenchimento sem sentido!'
        }
        
        var res = document.querySelector("div#res")
        res.innerHTML = resposta
    }
}