function criaPessoa(nome, sobrenome){
    let pessoa = {};
    pessoa.nome = nome;
    pessoa.sobrenome = sobrenome;
    
    function nomeCompleto(){
        return `${nome} ${sobrenome}`
    }
    
    pessoa.nomeCompleto = nomeCompleto;

    return pessoa;
}