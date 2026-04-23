const request = require("supertest");
const express = require("express");
const mongoose = require("mongoose");
const deviceRoutes = require("../Routes/DeviceRoutes");
const authRoutes = require("../Routes/AuthRoutes");

const app = express();
app.use(express.json());
app.use("/api/auth", authRoutes);
app.use("/api", deviceRoutes);

let authToken = "";
let createdDeviceId = "";

beforeAll(async () => {
  await mongoose.connect("mongodb://127.0.0.1:27017/pc-diagnostics-test");
  await request(app)
    .post("/api/auth/register")
    .send({ email: "devicetest@example.com", password: "password123" });
  const res = await request(app)
    .post("/api/auth/login")
    .send({ email: "devicetest@example.com", password: "password123" });
  authToken = res.body.token;
}, 15000);

afterAll(async () => {
  await mongoose.connection.dropDatabase();
  await mongoose.disconnect();
}, 15000);

describe("POST /api/device", () => {
  it("should save a device when authenticated", async () => {
    const res = await request(app)
      .post("/api/device")
      .set("Authorization", `Bearer ${authToken}`)
      .send({ deviceType: "laptop", model: "Dell XPS 15", cpu: "Intel i7", gpu: "NVIDIA RTX 3050", ram: "16GB" });
    expect(res.statusCode).toBe(200);
    expect(res.body.device).toBeDefined();
    expect(res.body.device.model).toBe("Dell XPS 15");
    createdDeviceId = res.body.device._id;
  }, 10000);

  it("should reject saving a device without a token", async () => {
    const res = await request(app)
      .post("/api/device")
      .send({ deviceType: "laptop", model: "Dell XPS 15" });
    expect(res.statusCode).toBe(401);
    expect(res.body.error).toBe("No token provided");
  }, 10000);

  it("should reject saving a device with an invalid token", async () => {
    const res = await request(app)
      .post("/api/device")
      .set("Authorization", "Bearer invalidtoken123")
      .send({ deviceType: "laptop", model: "Dell XPS 15" });
    expect(res.statusCode).toBe(401);
    expect(res.body.error).toBe("Invalid token");
  }, 10000);
});

describe("GET /api/devices", () => {
  it("should return the user's devices when authenticated", async () => {
    const res = await request(app)
      .get("/api/devices")
      .set("Authorization", `Bearer ${authToken}`);
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  }, 10000);

  it("should reject fetching devices without a token", async () => {
    const res = await request(app).get("/api/devices");
    expect(res.statusCode).toBe(401);
  }, 10000);
});

describe("DELETE /api/device/:id", () => {
  it("should delete a device that belongs to the user", async () => {
    const res = await request(app)
      .delete(`/api/device/${createdDeviceId}`)
      .set("Authorization", `Bearer ${authToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body.message).toBe("Device deleted");
  }, 10000);

  it("should reject deleting without a token", async () => {
    const res = await request(app)
      .delete(`/api/device/${createdDeviceId}`);
    expect(res.statusCode).toBe(401);
  }, 10000);
});