import { useState, useEffect } from "react";
import DeviceForm from "./DeviceForm";

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    const savedToken = localStorage.getItem("token");
    if (savedToken) setToken(savedToken);
  }, []);

  const register = async () => {
    const res = await fetch("http://localhost:5000/api/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await res.json();
    setMessage(data.message);
  };

  const login = async () => {
    const res = await fetch("http://localhost:5000/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await res.json();
    if (data.token) {
      setToken(data.token);
      localStorage.setItem("token", data.token);
      setMessage("Login successful");
    } else {
      setMessage(data.message);
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setToken("");
    setMessage("Logged out");
  };

  return (
    <div className="container">

      <div className="header">
        <div className="title">PC Diagnostics</div>
        {token && (
          <button className="logout-btn" onClick={logout}>Logout</button>
        )}
      </div>

      {!token && (
        <div style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          minHeight: "70vh"
        }}>
          <div className="device-card" style={{ width: "100%", maxWidth: "400px" }}>
            <h2>Login / Register</h2>

            <input
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />

            <br /><br />

            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <br /><br />

            <button onClick={register}>Register</button>
            <button onClick={login} style={{ marginLeft: "10px" }}>Login</button>

            {message && <p style={{ marginTop: "10px" }}>{message}</p>}
          </div>
        </div>
      )}

      {token && (
        <div className="section">
          <DeviceForm />
        </div>
      )}

    </div>
  );
}

export default App;