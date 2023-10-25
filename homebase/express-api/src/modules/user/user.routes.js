const express = require('express');
const router = express.Router();
const userController = require('./user.controller');

// Define User routes
router.post('/', userController.createUser);
router.get('/:id', userController.getUser);
router.put('/:id', userController.updateUser);
router.delete('/:id', userController.deleteUser);
router.get('/', userController.getList);

module.exports = router;