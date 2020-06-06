function populateUFs(){
    const ufselector = document.querySelector("select[name=uf]")

    //then: ele pega o retorno da função anterior e jogar na próxima
    //que pode ser uma arrow function ou não

    fetch("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
    .then( res =>  res.json() ) //(res) => {return res.json()} de forma resumida
    .then( states => {
        for(const state of states){
            ufselector.innerHTML += `<option value="${state.id}">${state.nome}</option>`
        }
    } )
}

function getCities(event){
    const citySelector = document.querySelector("select[name=city]")
    const stateInput = document.querySelector("input[name=state]")

    const ufValue = event.target.value

    const indexOfSelectedState = event.target.selectedIndex
    stateInput.value = event.target.options[indexOfSelectedState].text
    
    const url = `https://servicodados.ibge.gov.br/api/v1/localidades/estados/${ufValue}/municipios`

    citySelector.innerHTML = "<option value=>Selecione uma cidade</option>"
    citySelector.disabled = true

    fetch(url).then(res => res.json()).then(cities => {
        for(city of cities){
            citySelector.innerHTML += `<option value="${city.nome}">${city.nome}</option>`
        }
        citySelector.disabled = false
    })
}

populateUFs()

document.querySelector("select[name=uf]")
.addEventListener("change", getCities)//passando a função por referencia

//Seletor dos itens de coleta

const itemsToCollect = document.querySelectorAll(".items-grid li")//selecionar o itens dessa forma acaba trazendo os itens filho junto
//para resolver isso é necessário muda no arquivo css com o "pointer-event: none;"

const collectedItems = document.querySelector("input[name=items]")

for(const item of itemsToCollect){
    item.addEventListener("click", handleSelectedItem)
}

let selectedItems = []//itens selecionados

function handleSelectedItem(){
    const itemLi = event.target
    //adicionar ou remover uma classe com js dependendo da existencia
    itemLi.classList.toggle("selected")

    const itemId = itemLi.dataset.id

    //Verifica se existem itens selecionados, se sim, pega ele
    const alreadySelected = selectedItems.findIndex(item => item == itemId)//retorna o index do array quando receber o parametro true
    /* equivalente a: 
    function (item){
        if(item == itemId){
            return true
        }
    } */

    //se ja estiver selecionado, tira da seleção
    if( alreadySelected != -1){
        //essa função remove do array quando o valor der falso
       const filteredItems = selectedItems.filter(item => {
           const itemIsDifferent = item != itemId
           return itemIsDifferent
       })

       selectedItems = filteredItems
       console.log(selectedItems)

    } else{
        //se não estiver selecionado, adicione a seleção
        selectedItems.push(itemId)
    }
    collectedItems.value = selectedItems
}