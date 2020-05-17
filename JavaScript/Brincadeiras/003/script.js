const request = require('request-promise')
const cheerio = require('cheerio')

const URL = 'https://www.worldometers.info/coronavirus/'

async function acesso(){
    const response = await request(URL)
    let $ = cheerio.load(response)
    let teste = $('div.maincounter-number').text()
    teste = teste.trim()
    console.log(teste.slice(0, teste.indexOf('\n')))
}
acesso()
