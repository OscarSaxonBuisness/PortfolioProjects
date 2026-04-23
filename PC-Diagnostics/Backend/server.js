require("dotenv").config();

const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");

const deviceRoutes = require("./Routes/DeviceRoutes");
const uploadRoutes = require("./Routes/UploadRoutes");
const authRoutes = require("./Routes/AuthRoutes");
const specsRoutes = require("./Routes/SpecsRoutes");

mongoose.connect("mongodb://127.0.0.1:27017/pc-diagnostics");
mongoose.connection.once("open", () => console.log("MongoDB connected"));

const app = express();

app.use(cors());
app.use(express.json());

app.use("/api", deviceRoutes);
app.use("/api", uploadRoutes);
app.use("/api/auth", authRoutes);
app.use("/api", specsRoutes);

app.listen(5000, () => console.log("Server running on port 5000"));