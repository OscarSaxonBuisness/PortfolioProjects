const axios = require("axios");
const fs = require("fs");
const FormData = require("form-data");

exports.uploadImage = async (req, res) => {

  try {

    const filePath = req.file.path;

    const form = new FormData();
    form.append("image", fs.createReadStream(filePath));

    const response = await axios.post(
      "http://127.0.0.1:8000/predict",
      form,
      { headers: form.getHeaders() }
    );

    const prediction = response.data.prediction;

    console.log("AI Prediction:", prediction);

    res.json({
      message: "Image analysed successfully",
      prediction: prediction
    });

  } catch (error) {

    console.error("AI error:", error);

    res.status(500).json({
      message: "Error analysing image"
    });

  }

};