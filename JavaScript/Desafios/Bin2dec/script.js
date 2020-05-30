function converter(){
    var txtbin = document.querySelector("input#txtbin")
    var txtdec = document.querySelector("input#txtdec")
    var bin = String(txtbin.value)
                                      
    while(bin.length < 8){
        bin = '0' + bin
    }

    let ag = false
    bin.split("").map((char) => {//sem o split, a string nao tem o map 
        if(char != '0' && char != '1') {
            if(ag){
                return
            }
            window.alert("Entre um numero binário")
            ag = true
        }
    })


    let decBin = parseInt(bin, 2)//converte a string para um inteiro de base dois e vice-versa
    txtdec.value = `${decBin}`
    
}