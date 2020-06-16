// importar a dependencia do sqlite3
const sqlite3 = require("sqlite3").verbose()// Esse método é para a database mandar mensagens de status

// Criar o objeto que irá fazer operações no banco de dados
const db = new sqlite3.Database("./src/database/database.db")// new pode receber um objteto desde que esteja acompanhado de um construtor

module.exports = db
// Utilizar o banco de dados para o projeto

// db.serialize(() => {
//     // com comandos sql eu vou:
//     // 1- Criar uma tabela 
//     // db.run(` 
//     //     CREATE TABLE IF NOT EXISTS places (
//     //         id INTEGER PRIMARY KEY AUTOINCREMENT,
//     //         image TEXT,
//     //         name TEXT,
//     //         address TEXT,
//     //         address2 TEXT,
//     //         state TEXT,
//     //         city TEXT,
//     //         items TEXT
//     //     );
//     // `)

//     // 2- Inserir dados na tabela
//     // const query = `
//     //     INSERT INTO places (
//     //         image,
//     //         name,
//     //         address,
//     //         address2,
//     //         state,
//     //         city,
//     //         items
//     //     ) VALUES (?,?,?,?,?,?,?);
//     // `
//     // const values = [
//     //     "https://images.unsplash.com/photo-1567393528677-d6adae7d4a0a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60",
//     //     "Papersider",
//     //     "Guilherme Gemballa, Jardim América",
//     //     "Número 260",
//     //     "Santa Catarina",
//     //     "Rio do sul",
//     //     "Resíduos Elétronicos, Lâmpadas"
//     // ]

//     // function afterInsertData(err){//Funçao de callback de erro
//     //     if(err){
//     //         return console.log(err)
//     //     }
//     //     console.log("Cadastrado com sucesso")
//     //     console.log(this)
//     // }

//     // db.run(query, values, afterInsertData)

//     // 3- Consultar os dados da tabela
//     // db.all(`SELECT * FROM places`, function(err, rows){//recebe o erro e os rows do callback
//     //     if(err){
//     //         return console.log(err)
//     //     }
//     //     console.log("Aqui estão seus registros")
//     //     console.log(rows)
//     // })

//     // 4- Deletar um dado da tabela
//     // db.run(`DELETE FROM places WHERE id = ?`, [1], function(err){
//     //     if(err){
//     //         return console.log(err)
//     //     }
//     //     console.log("registro deletado com sucesso")
//     // })

// })//roda sequencia de código
