const express = require("express");
const router = express.Router();
const multer = require("multer");
const path = require("path");

const { uploadImage } = require("../Controllers/uploadController");

const storage = multer.diskStorage({
  destination: "Uploads/",
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({ storage });

router.post("/upload", upload.single("image"), uploadImage);

module.exports = router;