# PC Diagnostics — Manual Testing Checklist

Make sure all three servers are running before starting:
- React frontend: http://localhost:5173
- Express backend: http://localhost:5000
- Flask AI service: http://localhost:8000

---

## 1. Authentication

### Register
- [ ] Go to http://localhost:5173
- [ ] Enter a new email and password and click Register
- [ ] Should see "User registered successfully"
- [ ] Try registering the same email again — should see "User already exists"
- [ ] Try registering with no password — should not crash the app

### Login
- [ ] Enter the email and password you just registered and click Login
- [ ] Should see "Login successful" and the DeviceForm should appear
- [ ] Refresh the page — should still be logged in (token persisted in localStorage)
- [ ] Click Logout — should return to the login screen
- [ ] Try logging in with the wrong password — should see "Invalid credentials"
- [ ] Try logging in with an email that doesn't exist — should see "User not found"

---

## 2. Device Management

### Add a Laptop
- [ ] Make sure "Laptop" is selected in the toggle
- [ ] Type "Dell XPS 15" in the Model field
- [ ] After 500ms a "Searching..." indicator should appear briefly
- [ ] Specs should auto-populate below the input (CPU, GPU, RAM, Display, Storage, OS)
- [ ] If no exact match, "Did you mean:" suggestions should appear as clickable buttons
- [ ] Click a suggestion — model field should update and specs should load
- [ ] Click "Save Device" — should see "Device saved successfully!"
- [ ] Device should appear in the "My Devices" list on the right

### Add a Custom PC
- [ ] Switch the toggle to "Custom PC"
- [ ] Fill in CPU, GPU, RAM, Motherboard, PSU fields
- [ ] Click "Save Device" — should appear in the list

### Select a Device
- [ ] Click "Use" on a saved device
- [ ] The card should get a blue border (selected state)
- [ ] If it's a laptop, specs should appear under the device card

### Delete a Device
- [ ] Click "Delete" on a saved device
- [ ] Device should disappear from the list immediately
- [ ] If the deleted device was selected, selection should clear

### Persistence
- [ ] Add a device, then logout and log back in
- [ ] Your devices should still be there (stored in MongoDB)

---

## 3. Text-Based Diagnostics Chatbot

- [ ] Type "blue screen" in the Describe Your Issue box and click Get Fix 🔧
- [ ] Should show "Blue Screen of Death (BSOD)" as detected problem with 5 fixes
- [ ] Type "overheating" — should show Overheating fixes
- [ ] Type "no signal" — should show No Display / No Signal fixes
- [ ] Type "slow" — should show Poor Performance fixes
- [ ] Type "wifi not working" — should show Network / WiFi Issues fixes
- [ ] Type "no sound" — should show Audio Issues fixes
- [ ] Type "ram not detected" — should show RAM / Memory Issues fixes
- [ ] Type "something completely random" — should fall back to General Troubleshooting

### Personalised Fixes
- [ ] Select a device with a known GPU (e.g. "NVIDIA RTX 3050")
- [ ] Type "gpu glitching" and get fix
- [ ] Fixes mentioning "your GPU" should now say "your NVIDIA RTX 3050"
- [ ] Select a laptop device and type "reseat gpu"
- [ ] Fix should include the laptop disclaimer about professional service

---

## 4. Image Upload & AI Prediction

- [ ] Make sure the Flask server is running on port 8000
- [ ] Click "Choose File" and select a screenshot
- [ ] A preview of the image should appear
- [ ] Click "Analyse Image" — should show "Analysing..."
- [ ] Result should show one of: Artifacting, BIOS, BSOD, NormalScreen, NoSignal
- [ ] NormalScreen should show green text, others red
- [ ] Suggested fixes should appear below the prediction
- [ ] If a device is selected, fixes should be personalised to that device
- [ ] Try uploading a non-image file — should show an error

### Test each class (if you have sample images):
- [ ] A blue screen screenshot → should predict BSOD
- [ ] A black/no signal screen → should predict NoSignal
- [ ] A BIOS screen → should predict BIOS
- [ ] A normal desktop screenshot → should predict NormalScreen
- [ ] A glitchy/corrupted screen → should predict Artifacting

---

## 5. Security Checks

- [ ] Open browser DevTools → Application → Local Storage
- [ ] After login a JWT token should be stored
- [ ] After logout the token should be removed
- [ ] Try accessing http://localhost:5000/api/devices directly in browser (no token)
- [ ] Should receive: { "error": "No token provided" }
- [ ] Try accessing http://localhost:5000/api/device with a fake token
- [ ] Should receive: { "error": "Invalid token" }

---

## 6. Edge Cases

- [ ] Add a device, refresh the page — devices should persist
- [ ] Submit the device form with empty fields — should save with empty strings (not crash)
- [ ] Rapidly type in the model field — only one specs request should fire (debounce working)
- [ ] Click "Analyse Image" without selecting a file — should show "Please select an image first"
- [ ] Click "Get Fix" with an empty issue box — should show "Please describe your issue first"

---

## 7. Quick Smoke Test (Run This Before Your Demo)

1. Open http://localhost:5173
2. Register a new account
3. Login
4. Add a laptop — confirm specs auto-load
5. Select the device
6. Type "blue screen" and get fix — confirm personalised output
7. Upload a screenshot — confirm AI prediction returns
8. Delete the device — confirm it disappears
9. Logout — confirm token cleared
