const express = require("express");
const router = express.Router();

const { saveDevice, getUserDevices, deleteDevice } = require("../Controllers/DeviceController");
const authMiddleware = require("../Middleware/authMiddleware");

router.post("/device", authMiddleware, saveDevice);
router.get("/devices", authMiddleware, getUserDevices);
router.delete("/device/:id", authMiddleware, deleteDevice);

module.exports = router;