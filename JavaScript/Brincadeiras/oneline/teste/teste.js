function LeDadosDoArduino() {
    nocache = "&nocache=" + Math.random() * 1000000;
    var request = new XMLHttpRequest();
    var posIni;
    var valPosIni;
    var valPosFim;
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                if (this.responseText != null) {
                    posIni = this.responseText.indexOf("PD2");
                    if ( posIni > -1) {
                        valPosIni = this.responseText.indexOf("#", posIni) + 1;
                        valPosFim = this.responseText.indexOf("|", posIni);
                        document.getElementById("pino2").checked = Number(this.responseText.substring(valPosIni, valPosFim));
                    }
                    posIni = this.responseText.indexOf("PA1");
                    if ( posIni > -1) {
                        valPosIni = this.responseText.indexOf("#", posIni) + 1;
                        valPosFim = this.responseText.indexOf("|", posIni);
                        document.getElementById("pino1").innerHTML = "Porta 1- Valor: " + this.responseText.substring(valPosIni, valPosFim);
                    }
                }
            }
        }
    }
    request.open("GET", "solicitacao_via_ajax" + nocache, true);
    request.send(null);
    setTimeout('LeDadosDoArduino()', 1000);
}