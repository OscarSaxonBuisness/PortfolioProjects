# PC Diagnostics

A full-stack AI-powered web application for diagnosing PC hardware and software issues.

## Tech Stack
- Frontend: React 18 + TypeScript (port 5173)
- Backend: Node.js + Express (port 5000)
- Database: MongoDB + Mongoose
- AI Service: Python Flask + PyTorch (port 8000)

## How to Run

### Backend
```bash
cd Backend
npm install
npm run dev
```

### Frontend
```bash
cd Frontend
npm install
npm run dev
```

### AI Service
```bash
cd AI-Service
pip install -r requirements.txt
python predict.py
```

## API Endpoints
- POST /api/auth/register
- POST /api/auth/login
- GET /api/devices
- POST /api/device
- DELETE /api/device/:id
- GET /api/specs
- POST /api/upload
