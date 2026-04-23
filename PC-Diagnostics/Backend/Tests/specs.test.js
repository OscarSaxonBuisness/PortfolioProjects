const request = require("supertest");
const express = require("express");
const mongoose = require("mongoose");
const authRoutes = require("../Routes/AuthRoutes");
const specsRoutes = require("../Routes/SpecsRoutes");

const app = express();
app.use(express.json());
app.use("/api/auth", authRoutes);
app.use("/api", specsRoutes);

let authToken = "";

beforeAll(async () => {
  await mongoose.connect("mongodb://127.0.0.1:27017/pc-diagnostics-test");
  await request(app)
    .post("/api/auth/register")
    .send({ email: "specstest@example.com", password: "password123" });
  const res = await request(app)
    .post("/api/auth/login")
    .send({ email: "specstest@example.com", password: "password123" });
  authToken = res.body.token;
}, 15000);

afterAll(async () => {
  await mongoose.connection.dropDatabase();
  await mongoose.disconnect();
}, 15000);

describe("GET /api/specs", () => {
  it("should return specs for a known laptop model", async () => {
    const res = await request(app)
      .get("/api/specs?model=Dell XPS")
      .set("Authorization", `Bearer ${authToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty("found");
  }, 10000);

  it("should return suggestions when exact match not found", async () => {
    const res = await request(app)
      .get("/api/specs?model=laptop")
      .set("Authorization", `Bearer ${authToken}`);
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.suggestions)).toBe(true);
  }, 10000);

  it("should return 400 when no model query provided", async () => {
    const res = await request(app)
      .get("/api/specs")
      .set("Authorization", `Bearer ${authToken}`);
    expect(res.statusCode).toBe(400);
    expect(res.body.error).toBe("Model name required");
  }, 10000);

  it("should reject request without a token", async () => {
    const res = await request(app).get("/api/specs?model=Dell XPS");
    expect(res.statusCode).toBe(401);
  }, 10000);

  it("should return found:false for a nonsense model name", async () => {
    const res = await request(app)
      .get("/api/specs?model=xyzabcnotamodel999")
      .set("Authorization", `Bearer ${authToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body.found).toBe(false);
  }, 10000);
});