function createCore(){
    function start(){
        console.log('Iniciando sistema...')
    }
    function stop(){
        console.log('Desligando o sistema...')
    }
    return{
        start,
        stop
    }
}
module.exports = createCore