let createCore = require('./core.js')
let core = createCore()

try {
    core.start()
    core.stop()
} catch {
    console.log('ERRO! no index.js')
}