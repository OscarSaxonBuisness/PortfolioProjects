const express = require("express");
const router = express.Router();
const { getLaptopSpecs } = require("../Controllers/SpecsController");
const authMiddleware = require("../Middleware/authMiddleware");

router.get("/specs", authMiddleware, getLaptopSpecs);

module.exports = router;
