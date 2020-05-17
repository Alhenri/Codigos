function tabuada(){
    let num = document.getElementById('txtn')
    let tab = document.getElementById("seltab")
    if(num.value.length == 0){
        window.alert("Por favor digite um numero")
    }
    else{
        let n = Number(num.value)
        let c = 1
        tab.innerHTML = ''//Limpa a área
        while(c <= 10){
            let item = document.createElement('option')
            //Text é o que fica entre as marcações
            item.text = `${n} X ${c} = ${n*c}`
            item.value = `tab${c}` //Acrescenta o parametro value à marcação
            tab.appendChild(item)
            c++
        }
    }
}