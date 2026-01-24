# 🩸 HemoLink: Real-Time Emergency Blood Network

**Live Demo:** [https://hemolink-live.onrender.com](https://hemolink-live.onrender.com)  
*(Note: Please allow GPS location access for the app to function)*

## 💡 The Problem
During critical medical emergencies, finding a specific blood type nearby can take hours. Existing lists are often outdated, and there is no way to track if a donor is actually coming.

## 🚀 The Solution
HemoLink is a **Hyper-Local Emergency Response System** (like Uber for Blood).
1.  **Hospital** triggers an SOS for a specific blood type (e.g., O+).
2.  **Server** uses Geo-Spatial querying to find donors within 5km.
3.  **Donors** receive an instant WebSocket alert.
4.  **Live Tracking:** When a donor accepts, the hospital can track their location in real-time on the map.

## 🛠️ Tech Stack
* **Backend:** Python (FastAPI), Uvicorn
* **Database:** MongoDB Atlas (2dsphere Geo-Spatial Indexing)
* **Real-Time:** WebSockets (Bi-directional communication)
* **Frontend:** HTML5, JavaScript, Leaflet.js (OpenStreetMap)
* **Deployment:** Render Cloud

## 📸 Screenshots
*(Add your screenshots of the Red Alert and Blue Tracking Marker here)*

## ⚡ How to Run Locally
1.  Clone the repo:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/hemolink-live.git](https://github.com/YOUR_USERNAME/hemolink-live.git)
    cd hemolink-live
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the server:
    ```bash
    uvicorn app.main:app --reload
    ```
4.  Open `http://127.0.0.1:8000`

---
*Built by Vikash Kumar • 2026*