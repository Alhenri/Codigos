const express = require("express")
const server = express()

//Configurar a leitura das pastas
server.use(express.static("public"))

//configurar caminhos da minha aplicação
    //pagina inicial
        //req: requisição
        //res: respostas
server.get("/", (req, res) => { //get é um verbo de requisição http, e o '/' é a primeira chamada
    res.sendFile(__dirname + "/views/index.html") //dirname é o diretório em que eu estou    
})

server.get("/create-point", (req, res) => {//o arquivo deverá ser chamado exatamente como está o primeiro argumento
    res.sendFile(__dirname + "/views/create-point.html")
})

server.get("/search-results", (req, res) => {
    res.sendFile(__dirname + "/views/search-results.html")
})
// ligar o servidor
server.listen(3000)