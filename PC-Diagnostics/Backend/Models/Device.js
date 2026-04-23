const mongoose = require("mongoose");

const deviceSchema = new mongoose.Schema({
  deviceType: String,
  model: String,
  cpu: String,
  gpu: String,
  ram: String,
  motherboard: String,
  psu: String,

  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User"
  }
});

module.exports = mongoose.model("Device", deviceSchema);