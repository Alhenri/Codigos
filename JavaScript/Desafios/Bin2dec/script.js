function converter(){
    var txtbin = document.querySelector("input#txtbin")
    var txtdec = document.querySelector("input#txtdec")
    var bin = String(txtbin.value)

    bin.map((char) => {
        if(char != '0' && char != '1') window.alert("Entre um numero binário")
    })
}