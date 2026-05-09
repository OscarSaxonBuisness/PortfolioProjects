# Pneumonia Detection — Chest X-Ray CNN

A binary image classification model that detects pneumonia from chest X-ray images, built with TensorFlow/Keras and trained in Google Colab. Achieves **88.46%** test accuracy on the Kaggle chest X-ray dataset.

---

## Dataset

[Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) by Paul Mooney on Kaggle.

- **5,216** training images
- **16** validation images  
- **624** test images
- Two classes: `NORMAL` and `PNEUMONIA`

---

## Model Architecture

A custom CNN built with Keras Sequential API:

| Layer | Details |
|-------|---------|
| Conv2D + MaxPool | 32 filters, 3×3, ReLU |
| Conv2D + MaxPool | 64 filters, 3×3, ReLU |
| Conv2D + MaxPool | 128 filters, 3×3, ReLU |
| Flatten | — |
| Dense | 256 units, ReLU |
| Dense (output) | 1 unit, Sigmoid |

Binary cross-entropy loss, Adam optimiser, trained for 10 epochs.

---

## Data Augmentation

Applied to the training set to improve generalisation:

- Random rotation (±15°)
- Zoom (up to 10%)
- Horizontal and vertical shifts (up to 10%)
- Horizontal flip
- Pixel rescaling (÷255)

---

## Results

| Metric | Score |
|--------|-------|
| Test Accuracy | 88.46% |
| Test Loss | 0.4336 |

**Classification Report:**

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| NORMAL | 0.92 | 0.76 | 0.83 |
| PNEUMONIA | 0.87 | 0.96 | 0.91 |

**Confusion Matrix:**
```
              Predicted
              NORMAL  PNEUMONIA
Actual NORMAL   177       57
       PNEUMONIA  15      375
```

The model is notably better at detecting pneumonia (96% recall) than ruling it out (76% recall for NORMAL). In a medical screening context this is the preferable bias — missing a real pneumonia case is more costly than a false alarm.

---

## How to Run

This project is designed to run in **Google Colab**.

1. Open the notebook in [Google Colab](https://colab.research.google.com/)
2. Upload your `kaggle.json` API token when prompted (get this from your Kaggle account settings)
3. Run all cells in order — the dataset will be downloaded and extracted automatically
4. At the end, upload a chest X-ray image to get a prediction

---

## Requirements

All dependencies are pre-installed in Google Colab. If running locally:

```bash
pip install tensorflow scikit-learn matplotlib numpy
```

---

## Predicting on a New Image

The final cells of the notebook allow you to upload any chest X-ray image and receive an instant prediction:

```
Prediction: PNEUMONIA
```

The image is displayed alongside the predicted label.

---

## Limitations

- The validation set in this dataset is very small (16 images), so validation accuracy during training is noisy — test set metrics are more reliable
- The model is not clinically validated and should not be used for any real medical decision-making
