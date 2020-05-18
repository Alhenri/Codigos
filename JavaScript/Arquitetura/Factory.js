//Exemplos de funções usando o design patern da factory

function criaPessoa(nome, sobrenome){//Fábrica responsavel pela criação da pessoa
    let pessoa = {};//objeto que será retornado
    pessoa.nome = nome;//atribuições ao objeto
    pessoa.sobrenome = sobrenome;
    
    function nomeCompleto(){
        return `${nome} ${sobrenome}`//Método interno mas que será publicado posteriormente
    }
    
    pessoa.nomeCompleto = nomeCompleto; //se caso colocasse nomeCompleto(); ele executaria a função e daria o valor 
    //direto a variavel, mas dessa forma a execução so é feita na chamada.

    return pessoa;
}

function criaCaneta(marca, cor, carga){
    let caneta = {}
    
    caneta.marca = marca
    caneta.cor = cor
    caneta.carga = Number(carga)

    function escrever(){
        caneta.carga -= 1
    }
    
    caneta.escrever = escrever;
    
    return caneta
}