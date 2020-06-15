// importar a dependencia do sqlite3
const sqlite3 = require("sqlite3").verbose()// Esse método é para a database mandar mensagens de status

// Criar o objeto que irá fazer operações no banco de dados
const db = new sqlite3.Database("./src/database/database.db")// new pode receber um objteto desde que esteja acompanhado de um construtor

// Utilizar o banco de dados para o projeto
db.serialize(() => {
    // Criar uma tabela
    // Inserir dados na tabela
    // Consultar os dados da tabela
    // Deletar um dado da tabela
})//roda sequencia de código