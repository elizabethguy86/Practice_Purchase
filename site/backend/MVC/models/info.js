const file = require('./filesync')
const info = require('./data/info')

function getAll(){
    const blogs = file.filesync('read', '/blogs.json')
    const error = []

    if(!blogs){
        error.push('no blogs found')
        return { error }
    }

    return { blogs }
}