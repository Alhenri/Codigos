//Variaveis
let idade = 5; //Novo tipo de declaração equivalente a var
const altura = 1.75 //Valor nao pode mais ser alterado
let boleano = true //variavel boleana
let indefinido = undefined // valor indefinido
let nulo = null //Geralmente usado para redefinir um valor

//Objeto
let pessoa = { //Declarando um objeto em JS
    nome: 'Alexandre', //Combinação de chave e valor
    idade: 19,
    Sit: true,
    sobrenome: 'Soares'
};

//Arrays
let familia = [54, 12, 65];
let tamanho = familia.length; //os arrays são como objetos e possuem metodos internos

//Função (Verbo + substantivo)
let corSite = 'Azul'
function resetaCor(cor){
    corSite = cor;
}