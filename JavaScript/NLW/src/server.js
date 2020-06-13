const express = require("express")
const server = express()

//Configurar a leitura das pastas
server.use(express.static("public"))

//utilizando template engine
const nunjucks = require("nunjucks")
nunjucks.configure("src/views", {//onde ta os html, objeto
    express: server,
    noCache: true
})

//configurar caminhos da minha aplicação
    //pagina inicial
        //req: requisição
        //res: respostas
server.get("/", (req, res) => { //get é um verbo de requisição http, e o '/' é a primeira chamada
    //res.sendFile(__dirname + "/views/index.html") //dirname é o diretório em que eu estou
    return res.render("index.html", {
        title: "Ecoleta" //envia a variável
    })
})

server.get("/create", (req, res) => {//o arquivo deverá ser chamado exatamente como está o primeiro argumento
    return res.render("create-point.html")
})

server.get("/search", (req, res) => {
    return res.render("search-results.html")
})

// ligar o servidor
server.listen(3000)