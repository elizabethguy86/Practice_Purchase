const express = require('express')
const router = express.Router()
const interFaceController = require('../controllers/info')

router.get('/', interFaceController.getAll)

module.exports = router