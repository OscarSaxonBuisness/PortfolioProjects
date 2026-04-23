from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import torch
import torch.nn as nn
from torchvision import transforms
import os

app = Flask(__name__)

MODEL_PATH = "pc_diagnostics_model.pth"
IMG_SIZE = 128
CONFIDENCE_THRESHOLD = 0.70
CLASSES = ["Artifacting", "BIOS", "BSOD", "NormalScreen", "NoSignal"]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class PCDiagnosticsCNN(nn.Module):
    def __init__(self, num_classes=5):
        super(PCDiagnosticsCNN, self).__init__()

        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(256 * 8 * 8, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

# LOAD MODEL 
cnn_model = None

if os.path.exists(MODEL_PATH):
    cnn_model = PCDiagnosticsCNN(num_classes=len(CLASSES)).to(device)
    cnn_model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    cnn_model.eval()
    print("CNN model loaded successfully")
else:
    print("No trained model found — using RGB fallback only")

# TRANSFORM
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

# RGB FALLBACK
def rgb_analysis(image):
    image = image.convert("RGB").resize((200, 200))
    pixels = np.array(image)

    avg_r = np.mean(pixels[:, :, 0])
    avg_g = np.mean(pixels[:, :, 1])
    avg_b = np.mean(pixels[:, :, 2])
    brightness = (avg_r + avg_g + avg_b) / 3
    variance = np.var(pixels)
    blue_dominance = avg_b - max(avg_r, avg_g)
    green_dominance = avg_g - max(avg_r, avg_b)

    print(f"RGB fallback — brightness:{brightness:.1f} variance:{variance:.1f}")

    if brightness < 30:
        return "NoSignal"
    if blue_dominance > 30 and avg_b > 100:
        return "BSOD"
    if green_dominance > 20 and brightness < 120:
        return "BIOS"
    if variance > 4000:
        return "Artifacting"
    return "NormalScreen"

# CNN PREDICTION
def cnn_predict(image):
    img_tensor = transform(image.convert("RGB")).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = cnn_model(img_tensor)
        probabilities = torch.softmax(outputs, dim=1)[0]
        confidence = float(probabilities.max())
        predicted_class = CLASSES[probabilities.argmax().item()]

    print(f"CNN: {predicted_class} ({confidence*100:.1f}% confidence)")
    return predicted_class, confidence

# ROUTE
@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    image = Image.open(file.stream)

    prediction = None
    method_used = "rgb"

    if cnn_model is not None:
        predicted_class, confidence = cnn_predict(image)
        if confidence >= CONFIDENCE_THRESHOLD:
            prediction = predicted_class
            method_used = "cnn"
        else:
            print(f"Low confidence ({confidence*100:.1f}%) — falling back to RGB")
            prediction = rgb_analysis(image)
    else:
        prediction = rgb_analysis(image)

    print(f"Final: {prediction} via {method_used}")

    return jsonify({
        "prediction": prediction,
        "method": method_used
    })

if __name__ == "__main__":
    app.run(port=8000)