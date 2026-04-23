const request = require("supertest");
const express = require("express");
const mongoose = require("mongoose");
const authRoutes = require("../Routes/AuthRoutes");

const app = express();
app.use(express.json());
app.use("/api/auth", authRoutes);

beforeAll(async () => {
  await mongoose.connect("mongodb://127.0.0.1:27017/pc-diagnostics-test");
}, 15000);

afterAll(async () => {
  await mongoose.connection.dropDatabase();
  await mongoose.disconnect();
}, 15000);

describe("POST /api/auth/register", () => {
  it("should register a new user", async () => {
    const res = await request(app)
      .post("/api/auth/register")
      .send({ email: "test@example.com", password: "password123" });
    expect(res.statusCode).toBe(200);
    expect(res.body.message).toBeDefined();
  }, 10000);

  it("should not register the same email twice", async () => {
    const res = await request(app)
      .post("/api/auth/register")
      .send({ email: "test@example.com", password: "password123" });
    expect(res.statusCode).toBe(200);
    expect(res.body.message).toBe("User already exists");
  }, 10000);

  it("should handle registration with missing password gracefully", async () => {
    const res = await request(app)
      .post("/api/auth/register")
      .send({ email: "nopassword@example.com" });
    expect(res.statusCode).toBe(500); 
  }, 10000);
});

describe("POST /api/auth/login", () => {
  it("should return a token on valid login", async () => {
    await request(app)
      .post("/api/auth/register")
      .send({ email: "logintest@example.com", password: "password123" });
    const res = await request(app)
      .post("/api/auth/login")
      .send({ email: "logintest@example.com", password: "password123" });
    expect(res.statusCode).toBe(200);
    expect(res.body.token).toBeDefined();
  }, 10000);

  it("should reject login with wrong password", async () => {
    await request(app)
      .post("/api/auth/register")
      .send({ email: "wrongpass@example.com", password: "password123" });
    const res = await request(app)
      .post("/api/auth/login")
      .send({ email: "wrongpass@example.com", password: "wrongpassword" });
    expect(res.statusCode).toBe(400);
    expect(res.body.error).toBe("Invalid credentials");
  }, 10000);

  it("should reject login with non-existent user", async () => {
    const res = await request(app)
      .post("/api/auth/login")
      .send({ email: "nobody@example.com", password: "password123" });
    expect(res.statusCode).toBe(400);
    expect(res.body.error).toBe("User not found");
  }, 10000);
});