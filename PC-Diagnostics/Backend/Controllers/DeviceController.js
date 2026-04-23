const Device = require("../Models/Device");

exports.saveDevice = async (req, res) => {
  try {
    console.log("User ID:", req.userId);
    console.log("Received device:", req.body);

    const device = new Device({
      ...req.body,
      user: req.userId
    });

    await device.save();

    console.log("Saved to DB:", device);

    res.json({
      message: "Device saved successfully",
      device
    });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
};
exports.getUserDevices = async (req, res) => {
  try {
    const devices = await Device.find({ user: req.userId });

    res.json(devices);

  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
exports.deleteDevice = async (req, res) => {
  try {
    const { id } = req.params;

    await Device.findOneAndDelete({
      _id: id,
      user: req.userId 
    });

    res.json({ message: "Device deleted" });

  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};