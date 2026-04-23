import { useState } from "react";

const imageFixes: Record<string, string[]> = {
  "Artifacting": [
    "Check your GPU temperatures using MSI Afterburner — should be under 85°C",
    "Reinstall GPU drivers using DDU (Display Driver Uninstaller)",
    "Reseat the GPU in its PCIe slot",
    "Check all GPU power connectors are fully plugged in"
  ],
  "BIOS": [
    "Reset BIOS to default settings by clearing CMOS",
    "Check your boot drive is detected in BIOS",
    "Reseat RAM and storage connections",
    "Update your BIOS firmware from the motherboard manufacturer's site"
  ],
  "BSOD": [
    "Check your RAM using Windows Memory Diagnostic",
    "Update or roll back your GPU drivers",
    "Run 'sfc /scannow' in Command Prompt as Administrator",
    "Note the stop code on screen and search it for a targeted fix"
  ],
  "NormalScreen": [
    "No visible issues detected in the screenshot"
  ],
  "NoSignal": [
    "Check your HDMI or DisplayPort cable at both ends",
    "Make sure your monitor is on the correct input source",
    "Reseat the GPU firmly in its PCIe slot",
    "Try a different cable or display port"
  ]
};

function personaliseFixes(fixes: string[], device: any, specs: any): string[] {
  if (!device && !specs) return fixes;

  const merged = { ...device, ...specs };
  const gpu = merged.gpu || merged.GPU || null;
  const cpu = merged.cpu || merged.CPU || null;
  const isLaptop = device?.deviceType === "laptop";
  const deviceName = device?.model || "your device";

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
        fix.toLowerCase().includes("pcie slot")
      ) {
        return `${fix} (note: on a laptop like the ${deviceName} this may require professional service)`;
      }
    }
    return fix;
  });
}

interface Props {
  selectedDevice?: any;
  lookedUpSpecs?: any;
}

function UploadImage({ selectedDevice, lookedUpSpecs }: Props) {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [prediction, setPrediction] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files) return;
    const selected = e.target.files[0];
    setFile(selected);
    setPreview(URL.createObjectURL(selected));
    setPrediction("");
    setError("");
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select an image first");
      return;
    }

    const token = localStorage.getItem("token");
    const formData = new FormData();
    formData.append("image", file);

    setLoading(true);
    setError("");
    setPrediction("");

    try {
      const res = await fetch("http://localhost:5000/api/upload", {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
        body: formData,
      });

      const data = await res.json();
      setPrediction(data.prediction);
    } catch {
      setError("Error connecting to server");
    } finally {
      setLoading(false);
    }
  };

  const rawFixes = prediction ? (imageFixes[prediction] ?? []) : [];
  const fixes = personaliseFixes(rawFixes, selectedDevice, lookedUpSpecs);

  return (
    <div>
      <h3>Upload Screenshot</h3>

      <input type="file" accept="image/*" onChange={handleFileChange} />

      <br /><br />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Analysing..." : "Analyse Image"}
      </button>

      {error && (
        <p style={{ color: "#f87171", marginTop: "10px" }}>{error}</p>
      )}

      {preview && (
        <div style={{ marginTop: "15px" }}>
          <img
            src={preview}
            alt="preview"
            style={{
              width: "100%",
              maxWidth: "400px",
              borderRadius: "8px",
              border: "1px solid #334155"
            }}
          />
        </div>
      )}

      {prediction && (
        <div style={{ marginTop: "15px" }}>
          <p>
            <strong>Detected: </strong>
            <span style={{ color: prediction === "NormalScreen" ? "#4ade80" : "#f87171" }}>
              {prediction}
            </span>
          </p>

          {fixes.length > 0 && (
            <>
              <h3>Suggested Fixes</h3>
              {selectedDevice && (
                <p style={{ color: "#38bdf8", fontSize: "13px", marginBottom: "10px" }}>
                  Based on your {selectedDevice.deviceType === "laptop"
                    ? `laptop (${selectedDevice.model})`
                    : `Custom PC — ${selectedDevice.gpu || "no GPU listed"}`}
                  {lookedUpSpecs && " — specs auto-detected"}
                </p>
              )}
              <ul style={{ paddingLeft: "20px", lineHeight: "1.8" }}>
                {fixes.map((fix, i) => (
                  <li key={i}>{fix}</li>
                ))}
              </ul>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default UploadImage;