function carregar(){
    var msg = document.getElementById('msg');
    var img = document.getElementById('imagem');
    var data = new Date(); //pega a data
    var hora = data.getHours();//pega a hora
    var min = data.getMinutes();
    var seg = data.getSeconds();

    msg.innerHTML = `Agora são ${hora}:${min}:${seg}, `
    
    if(hora >=5 && hora < 12){
        msg.innerHTML += 'Bom dia!'
        img.src = 'manhãweb.png'
        document.body.style.background = '#ffdf66';
    } else if (hora >= 12 && hora < 18){
        msg.innerHTML += 'Boa tarde!'
        img.src = 'tardeweb.png'
        document.body.style.background = '#fd6e02';
    } else {
        msg.innerHTML += 'Boa noite!'
        img.src = 'noiteweb.png'
        document.body.style.background = '#3372a4';
    }
}