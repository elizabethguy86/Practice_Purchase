const file = require('./filesync')
const info = require('./data/chris')
const info2 = require('./data/sarah')
const info3 = require('./data/karl')

function getAll(){
    const info = file.filesync('read', '/chris.json')
    const info2 = file.filesync('read', '/karl.json')
    const info3 = file.filesync('read', '/sarah.json')
    const error = []

    console.log({ })
    return { info, info2, info3 }
}

module.exports = { getAll }