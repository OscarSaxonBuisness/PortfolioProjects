import { useState, useEffect, useRef } from "react";
import UploadImage from "./UploadImage";

type DeviceType = "laptop" | "custom";

const knowledgeBase: { title: string; keywords: string[]; fixes: string[] }[] = [
  {
    title: "Blue Screen of Death (BSOD)",
    keywords: ["blue screen", "bsod", "blue", "crash", "stop error", "dump"],
    fixes: [
      "Check your RAM — run Windows Memory Diagnostic from the Start menu",
      "Update or roll back your GPU drivers via Device Manager",
      "Run 'sfc /scannow' in Command Prompt as Administrator to repair corrupted files",
      "Check your storage drive for errors using 'chkdsk /f /r' in Command Prompt",
      "Note the stop code shown on the blue screen and search it for a specific fix"
    ]
  },
  {
    title: "No Display / No Signal",
    keywords: ["no signal", "black screen", "no display", "monitor", "screen not working", "no output"],
    fixes: [
      "Check your HDMI or DisplayPort cable is fully seated at both ends",
      "Ensure your monitor is powered on and set to the correct input source",
      "Reseat your GPU — remove it and firmly push it back into the PCIe slot",
      "Try a different display cable or a different port on your GPU",
      "If using integrated graphics, make sure the monitor is plugged into the motherboard not the GPU"
    ]
  },
  {
    title: "Overheating",
    keywords: ["overheating", "hot", "temperature", "thermal", "fan", "throttling", "shutting down"],
    fixes: [
      "Clean dust from your fans and heatsinks using compressed air",
      "Check that all fans are spinning correctly",
      "Reapply thermal paste to your CPU — old paste loses effectiveness over time",
      "Ensure your case has adequate airflow — check cable management is not blocking fans",
      "Monitor temperatures using HWMonitor or MSI Afterburner"
    ]
  },
  {
    title: "Poor Performance",
    keywords: ["slow", "lagging", "performance", "freezing", "stuttering", "hanging"],
    fixes: [
      "Open Task Manager and check which process is using the most CPU or RAM",
      "Check your storage drive health — a failing drive causes severe slowdowns",
      "Run a malware scan using Windows Defender or Malwarebytes",
      "Disable startup programs in Task Manager > Startup tab",
      "If on a laptop, check your power plan is set to Balanced or High Performance"
    ]
  },
  {
    title: "Boot Failure",
    keywords: ["no boot", "won't start", "not booting", "boot loop", "restart loop", "stuck on logo"],
    fixes: [
      "Disconnect all external USB devices and try booting again",
      "Enter BIOS and confirm your boot drive is listed and set as first boot device",
      "If recently added new hardware, remove it and test",
      "Try booting into Safe Mode by pressing F8 during startup",
      "Run Startup Repair from Windows Recovery Environment"
    ]
  },
  {
    title: "GPU / Display Issues",
    keywords: ["gpu", "graphics", "artifacting", "glitch", "visual", "flickering", "screen tearing"],
    fixes: [
      "Check your GPU temperatures using MSI Afterburner — should be under 85°C under load",
      "Uninstall GPU drivers completely using DDU then reinstall",
      "Reseat the GPU in its PCIe slot",
      "Check the GPU power connectors are fully plugged in",
      "Test with a different monitor or cable to rule out display issues"
    ]
  },
  {
    title: "Network / WiFi Issues",
    keywords: ["wifi", "internet", "network", "connection", "disconnecting", "no internet"],
    fixes: [
      "Restart your router and modem",
      "Update your network adapter drivers via Device Manager",
      "Forget the WiFi network and reconnect from scratch",
      "Run the Windows Network Troubleshooter",
      "Check if the issue occurs on other devices — if so the problem is with your router"
    ]
  },
  {
    title: "Audio Issues",
    keywords: ["sound", "audio", "no sound", "speakers", "headphones", "volume"],
    fixes: [
      "Right-click the volume icon and check the correct output device is selected",
      "Update your audio drivers via Device Manager",
      "Check the audio cable is fully plugged in",
      "Run the Windows Audio Troubleshooter",
      "Check the application's own volume settings not just system volume"
    ]
  },
  {
    title: "Storage / Drive Issues",
    keywords: ["storage", "disk", "hard drive", "ssd", "not detected", "drive missing"],
    fixes: [
      "Check the SATA or NVMe connection is secure inside the case",
      "Open Disk Management to see if the drive appears but has no letter assigned",
      "Run 'chkdsk' to check for file system errors",
      "Test the drive using CrystalDiskInfo to check its health status",
      "Try the drive in a different SATA port or USB enclosure"
    ]
  },
  {
    title: "RAM / Memory Issues",
    keywords: ["ram", "memory", "not detected", "8gb", "16gb", "less memory"],
    fixes: [
      "Reseat your RAM sticks — remove and firmly reinsert them",
      "Try each stick individually to identify a faulty module",
      "Run Windows Memory Diagnostic to test for RAM errors",
      "Check your BIOS to confirm the RAM speed and XMP profile settings",
      "Make sure the RAM is installed in the correct slots per your motherboard manual"
    ]
  }
];

function getFixes(issue: string): { title: string; fixes: string[] } {
  const lower = issue.toLowerCase();
  for (const entry of knowledgeBase) {
    if (entry.keywords.some((keyword) => lower.includes(keyword))) {
      return { title: entry.title, fixes: entry.fixes };
    }
  }
  return {
    title: "General Troubleshooting",
    fixes: [
      "Try restarting your PC as a first step",
      "Check Device Manager for any warning icons on hardware",
      "Run Windows Update to ensure all drivers are current",
      "Search the exact error message or symptom online for specific guidance",
      "If the problem persists consider checking hardware connections inside the case"
    ]
  };
}

function personaliseFixes(fixes: string[], device: any): string[] {
  if (!device) return fixes;
  const isLaptop = device.deviceType === "laptop";
  const deviceName = device.model || "your device";
  const gpu = device.gpu || null;
  const cpu = device.cpu || null;

  return fixes.map((fix) => {
    if (gpu && fix.toLowerCase().includes("gpu")) {
      fix = fix.replace(/your GPU/gi, `your ${gpu}`);
    }
    if (cpu && fix.toLowerCase().includes("cpu")) {
      fix = fix.replace(/your CPU/gi, `your ${cpu}`);
    }
    if (isLaptop) {
      if (
        fix.toLowerCase().includes("reseat the gpu") ||
        fix.toLowerCase().includes("pcie slot") ||
        fix.toLowerCase().includes("inside the case")
      ) {
        return `${fix} (note: on a laptop like the ${deviceName} this may require professional service)`;
      }
    }
    return fix;
  });
}

function DeviceForm() {
  const [deviceType, setDeviceType] = useState<DeviceType>("laptop");
  const [model, setModel] = useState("");
  const [cpu, setCpu] = useState("");
  const [gpu, setGpu] = useState("");
  const [ram, setRam] = useState("");
  const [motherboard, setMotherboard] = useState("");
  const [psu, setPsu] = useState("");
  const [devices, setDevices] = useState<any[]>([]);
  const [selectedDevice, setSelectedDevice] = useState<any>(null);
  const [selectedDeviceSpecs, setSelectedDeviceSpecs] = useState<any>(null);
  const [issue, setIssue] = useState("");
  const [fixes, setFixes] = useState<string[]>([]);
  const [detectedIssue, setDetectedIssue] = useState("");
  const [message, setMessage] = useState("");
  const [lookedUpSpecs, setLookedUpSpecs] = useState<any>(null);
  const [specsSuggestions, setSpecsSuggestions] = useState<string[]>([]);
  const [specsLoading, setSpecsLoading] = useState(false);
  const debounceTimer = useRef<any>(null);

  const fetchDevices = async () => {
    const token = localStorage.getItem("token");
    if (!token) return;
    const res = await fetch("http://localhost:5000/api/devices", {
      headers: { Authorization: `Bearer ${token}` },
    });
    const data = await res.json();
    if (Array.isArray(data)) setDevices(data);
    else setDevices([]);
  };

  useEffect(() => { fetchDevices(); }, []);

  const fetchSpecs = async (modelName: string) => {
    if (!modelName.trim() || modelName.trim().length < 2) return;
    const token = localStorage.getItem("token");
    setSpecsLoading(true);

    try {
      const res = await fetch(
        `http://localhost:5000/api/specs?model=${encodeURIComponent(modelName)}`,
        { headers: { Authorization: `Bearer ${token}` } }
      );
      const data = await res.json();

      if (data.found) {
        setLookedUpSpecs(data.specs);
        setSpecsSuggestions(data.suggestions || []);
      } else {
        setLookedUpSpecs(null);
        setSpecsSuggestions(data.suggestions || []);
      }
    } catch {
     
    } finally {
      setSpecsLoading(false);
    }
  };

  const handleModelChange = (value: string) => {
    setModel(value);
    setLookedUpSpecs(null);
    setSpecsSuggestions([]);

    if (debounceTimer.current) clearTimeout(debounceTimer.current);
    debounceTimer.current = setTimeout(() => {
      if (value.trim().length >= 2) fetchSpecs(value);
    }, 500);
  };

  const handleSelectSuggestion = async (suggestion: string) => {
    setModel(suggestion);
    setSpecsSuggestions([]);
    await fetchSpecs(suggestion);
  };

  const handleSelectDevice = async (device: any) => {
    setSelectedDevice(device);
    setSelectedDeviceSpecs(null);

    if (device.deviceType === "laptop" && device.model) {
      const token = localStorage.getItem("token");
      try {
        const res = await fetch(
          `http://localhost:5000/api/specs?model=${encodeURIComponent(device.model)}`,
          { headers: { Authorization: `Bearer ${token}` } }
        );
        const data = await res.json();
        if (data.found) setSelectedDeviceSpecs(data.specs);
      } catch {
      
      }
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const token = localStorage.getItem("token");
    if (!token) return setMessage("You must be logged in");
    const res = await fetch("http://localhost:5000/api/device", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ deviceType, model, cpu, gpu, ram, motherboard, psu }),
    });
    const data = await res.json();
    if (!res.ok) return setMessage(data.error);
    setMessage("Device saved successfully!");
    fetchDevices();
    setModel("");
    setCpu("");
    setGpu("");
    setRam("");
    setMotherboard("");
    setPsu("");
    setLookedUpSpecs(null);
    setSpecsSuggestions([]);
  };

  const handleDelete = async (id: string) => {
    const token = localStorage.getItem("token");
    await fetch(`http://localhost:5000/api/device/${id}`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${token}` },
    });
    if (selectedDevice?._id === id) {
      setSelectedDevice(null);
      setSelectedDeviceSpecs(null);
    }
    fetchDevices();
  };

  const handleGetFix = () => {
    if (!issue.trim()) {
      setMessage("Please describe your issue first");
      return;
    }

    const enrichedDevice = selectedDevice
      ? { ...selectedDevice, ...selectedDeviceSpecs, ...lookedUpSpecs }
      : lookedUpSpecs
      ? { deviceType: "laptop", model, ...lookedUpSpecs }
      : null;

    const { title, fixes: rawFixes } = getFixes(issue);
    const personalised = personaliseFixes(rawFixes, enrichedDevice);
    setDetectedIssue(title);
    setFixes(personalised);

    if (enrichedDevice) {
      setMessage(`Showing fixes for: ${enrichedDevice.model || "your device"}`);
    } else {
      setMessage("");
    }
  };

  const specsBoxStyle = {
    marginTop: "10px",
    padding: "10px",
    background: "#0f172a",
    borderRadius: "8px",
    fontSize: "13px",
    color: "#94a3b8"
  };

  const renderSpecs = (specs: any) => (
    <div style={specsBoxStyle}>
      <p style={{ color: "#38bdf8", marginBottom: "6px" }}>✅ Specs:</p>
      {specs.cpu && <p>CPU: {specs.cpu}</p>}
      {specs.gpu && <p>GPU: {specs.gpu}</p>}
      {specs.ram && <p>RAM: {specs.ram}</p>}
      {specs.display && <p>Display: {specs.display}</p>}
      {specs.storage && <p>Storage: {specs.storage}</p>}
      {specs.os && <p>OS: {specs.os}</p>}
    </div>
  );

  return (
    <div className="layout">

      {/* ================= LEFT SIDE ================= */}
      <div>

        <div className="device-card">
          <h3>Describe Your Issue</h3>
          <div className="input-row">
            <input
              value={issue}
              onChange={(e) => {
                setIssue(e.target.value);
                setFixes([]);
                setDetectedIssue("");
              }}
              placeholder="e.g. blue screen, overheating, no display..."
            />
          </div>
          <button onClick={handleGetFix} style={{ marginTop: "15px" }}>
            Get Fix
          </button>
          {message && (
            <p style={{ marginTop: "10px", color: "#38bdf8", fontSize: "14px" }}>
              {message}
            </p>
          )}

          {fixes.length > 0 && (
            <div style={{ marginTop: "20px" }}>
              <div style={{
                background: "#0f172a",
                border: "1px solid #334155",
                borderRadius: "8px",
                padding: "10px 14px",
                marginBottom: "15px"
              }}>
                <p style={{ color: "#94a3b8", fontSize: "12px", marginBottom: "4px" }}>
                  Detected Problem
                </p>
                <p style={{ color: "#f87171", fontWeight: "bold", fontSize: "16px" }}>
                  {detectedIssue}
                </p>
              </div>

              <h3>Suggested Fixes</h3>
              {selectedDevice && (
                <p style={{ color: "#38bdf8", fontSize: "13px", marginBottom: "10px" }}>
                  Based on your{" "}
                  {selectedDevice.deviceType === "laptop"
                    ? `laptop (${selectedDevice.model})`
                    : `Custom PC — ${selectedDevice.gpu || "no GPU listed"}`}
                  {selectedDeviceSpecs && " — specs auto-detected"}
                </p>
              )}
              <ul style={{ paddingLeft: "20px", lineHeight: "1.8" }}>
                {fixes.map((fix, i) => (
                  <li key={i}>{fix}</li>
                ))}
              </ul>
            </div>
          )}
        </div>

        <div className="device-card">
          <UploadImage selectedDevice={selectedDevice} lookedUpSpecs={selectedDeviceSpecs || lookedUpSpecs} />
        </div>

      </div>

      {/* ================= RIGHT SIDE ================= */}
      <div>

        <div className="device-card">
          <h3>My Devices</h3>
        </div>

        {devices.map((device) => (
          <div
            key={device._id}
            className={`device-card ${selectedDevice?._id === device._id ? "selected" : ""}`}
          >
            <p><strong>{device.model || "Custom PC"}</strong></p>

            {selectedDevice?._id === device._id && selectedDeviceSpecs && (
              renderSpecs(selectedDeviceSpecs)
            )}

            <div className="actions" style={{ marginTop: "10px" }}>
              <button onClick={() => handleSelectDevice(device)}>Use</button>
              <button className="delete-btn" onClick={() => handleDelete(device._id)}>
                Delete 
              </button>
            </div>
          </div>
        ))}

        <div className="device-card">
          <h2>Add Your Device</h2>
          <form onSubmit={handleSubmit}>

            <div className="toggle-group">
              <button
                type="button"
                className={deviceType === "laptop" ? "active" : ""}
                onClick={() => setDeviceType("laptop")}
              >
                Laptop
              </button>
              <button
                type="button"
                className={deviceType === "custom" ? "active" : ""}
                onClick={() => setDeviceType("custom")}
              >
                Custom PC
              </button>
            </div>

            {deviceType === "laptop" && (
              <div style={{ marginTop: "20px" }}>
                <p>Model</p>
                <input
                  value={model}
                  onChange={(e) => handleModelChange(e.target.value)}
                  placeholder="Dell XPS 15"
                />

                {specsLoading && (
                  <p style={{ color: "#94a3b8", fontSize: "13px", marginTop: "6px" }}>
                    Searching...
                  </p>
                )}

                {specsSuggestions.length > 0 && (
                  <div style={{ marginTop: "10px" }}>
                    <p style={{ color: "#94a3b8", fontSize: "13px", marginBottom: "6px" }}>
                      Did you mean:
                    </p>
                    {specsSuggestions.map((suggestion, i) => (
                      <button
                        key={i}
                        type="button"
                        onClick={() => handleSelectSuggestion(suggestion)}
                        style={{
                          display: "block",
                          marginBottom: "6px",
                          background: "#1e293b",
                          color: "#38bdf8",
                          border: "1px solid #334155",
                          borderRadius: "6px",
                          padding: "6px 12px",
                          cursor: "pointer",
                          fontSize: "13px",
                          textAlign: "left",
                          width: "100%"
                        }}
                      >
                        {suggestion}
                      </button>
                    ))}
                  </div>
                )}

                {lookedUpSpecs && renderSpecs(lookedUpSpecs)}
              </div>
            )}

            {deviceType === "custom" && (
              <div style={{ marginTop: "20px" }}>
                <p>CPU</p><input value={cpu} onChange={(e) => setCpu(e.target.value)} />
                <p>GPU</p><input value={gpu} onChange={(e) => setGpu(e.target.value)} />
                <p>RAM</p><input value={ram} onChange={(e) => setRam(e.target.value)} />
                <p>Motherboard</p>
                <input value={motherboard} onChange={(e) => setMotherboard(e.target.value)} />
                <p>PSU</p><input value={psu} onChange={(e) => setPsu(e.target.value)} />
              </div>
            )}

            <button style={{ marginTop: "20px" }}>Save Device</button>
          </form>
          {message && <p style={{ marginTop: "10px" }}>{message}</p>}
        </div>

      </div>
    </div>
  );
}

export default DeviceForm;