# TIET Campus Navigator

This project is about using certain python libraries such as **FastAPI**, **uvicorn**, and **React-Leaflet** in order to make a real-time campus navigation system for **Thapar Institute of Engineering and Technology (TIET)**.

## 🚀 Features
* **Interactive Schematic Map:** Uses the official FROSH 2024 campus map.
* **Live GPS Tracking:** High-precision real-time location tracking on the campus schematic.
* **Shortest Path Calculation:** Uses Dijkstra's algorithm to find the quickest route between landmarks.
* **Turn-by-Turn Directions:** Intelligent road-based instructions (Left, Right, Straight).
* **Consolidated Backend:** Single-file Python backend for easy deployment.

## 🛠️ Technology Stack
* **Frontend:** React, TypeScript, Leaflet, TailwindCSS.
* **Backend:** Python, FastAPI.
* **Data:** CSV-based graph network of campus roads and locations.

## 📂 Project Structure
* `backend/main.py`: The full Python navigation engine.
* `tiet_campus_map.csv`: The geographical data of Thapar campus.
* `frontend/`: The interactive map interface.
