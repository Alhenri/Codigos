const a = require('request-promise')
const cheerio = require('cheerio')

const req = a("http://www.calculadoraonline.com.br/basica")

let $ = cheerio.load(req)
console.log(req)