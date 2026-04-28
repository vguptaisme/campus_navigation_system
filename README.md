# 📍 TIET Campus Navigator

A high-fidelity, real-time navigation system for **Thapar Institute of Engineering and Technology (TIET)**. This project combines a modern React frontend with a robust Python backend to provide students and visitors with an interactive, location-aware campus guide.

---

## 🌟 Key Features

### 🗺️ High-Fidelity Schematic Map
Experience the campus through the **official FROSH 2024 schematic**, perfectly calibrated for real-world geographical coordinates. No more guessing where a building is!

### 🛰️ Live GPS Tracking & Auto-Pan
Built-in support for browser-based geolocation. 
- **Blue Dot Visualization:** See your real-time position on the map.
- **Accuracy Radius:** Visual feedback on GPS signal strength.
- **Auto-Follow:** The map automatically pans and centers on you as you walk through campus.

### 🛣️ Smart Turn-by-Turn Navigation
Don't just see a line; know where to turn!
- **Dijkstra’s Algorithm:** Calculates the mathematically shortest walking path.
- **Intelligent Directions:** Provides "Turn Left", "Turn Right", or "Continue Straight" instructions based on road geometry.
- **Directional Arrows:** Visual arrows on the map segments show the flow of travel.

---

## 🛠️ Technology Stack

### **Frontend**
- **React 18 & TypeScript:** For a type-safe, component-based UI.
- **Leaflet & React-Leaflet:** The industry standard for interactive web maps.
- **TailwindCSS:** For a premium, dark-mode-first aesthetic with glassmorphism effects.
- **Lucide React:** For sleek, modern iconography.

### **Backend**
- **Python 3.x:** Handling all geographical data processing.
- **FastAPI:** A high-performance web framework for the navigation API.
- **Uvicorn:** ASGI server for lightning-fast request handling.
- **Custom Graph Engine:** Built using Python's `heapq` for optimized Dijkstra pathfinding.

---

## 📂 Project Structure

To maintain a clean and scalable architecture, the project is strictly separated:

```text
├── backend/                # Python FastAPI Server
│   ├── main.py             # Consolidated Navigation API
│   └── data/               # Geospatial Data Storage
│       └── tiet_campus_map.csv
├── frontend/               # React TypeScript Interface
│   ├── src/                # Source code
│   └── public/             # Static assets (Schematic Maps)
└── README.md               # Documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### 2. Backend Setup
```bash
cd backend
pip install fastapi uvicorn pydantic
python main.py
```
The API will be available at `http://localhost:8000`.

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:5173` to start navigating!

---

## 🔮 Future Enhancements
- [ ] **PWA Support:** Installable on Android/iOS for a native app experience.
- [ ] **Category Search:** Quick-filters for Hostels, Depts, and Food Courts.
- [ ] **Parking Management:** Real-time occupancy tracking for campus parking lots.
- [ ] **Offline Maps:** Basic functionality without internet access.

---

## 👥 Contributors
- **Thapar University Project Team**
- **vguptaisme** (Project Lead)

---

© 2026 TIET Campus Navigation System. All rights reserved.
