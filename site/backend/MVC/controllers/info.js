const model = require('../models/info')

const getAll = (req,res,next) => {
    const data = model.getAll()

    if(data.error){
        return next({status: 404, message: `blogs not found`, error: data.error})
    }

    res.status(200).json(data)
}

module.exports = { getAll }