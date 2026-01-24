# 🩸 HemoLink: Real-Time Emergency Blood Network

**🚑 Live Hospital Dashboard:** [https://hemolink-live.onrender.com/hospital](https://hemolink-live.onrender.com/hospital)  
**👤 Live Donor App:** [https://hemolink-live.onrender.com](https://hemolink-live.onrender.com)  

*(Note: Please allow GPS location access for the app to function properly)*

---

## 💡 The Problem
During critical medical emergencies, finding a specific blood type nearby can take hours. Existing lists are often outdated, and there is no way to track if a donor is actually coming.

## 🚀 The Solution
HemoLink is a **Hyper-Local Emergency Response System** (think "Uber for Blood").
1.  **Hospital** triggers an SOS for a specific blood type (e.g., O+).
2.  **Server** uses Geo-Spatial querying (MongoDB 2dsphere) to find donors within 5km.
3.  **Donors** receive an instant WebSocket alert.
4.  **Live Tracking:** When a donor accepts, the hospital sees their location update in real-time on the map.

## 🛠️ Tech Stack
* **Backend:** Python (FastAPI), Uvicorn
* **Database:** MongoDB Atlas (Geo-Spatial Indexing)
* **Real-Time:** WebSockets (Bi-directional communication)
* **Frontend:** HTML5, JavaScript, Leaflet.js (OpenStreetMap)
* **Deployment:** Render Cloud

---

## 🧪 How to Test the Demo
To see the **Live Tracking** magic, you need two devices (or two browser windows):

1.  **Device A (Laptop):** Open the [Hospital Dashboard](https://hemolink-live.onrender.com/hospital). This represents the Control Room.
2.  **Device B (Phone):** Open the [Donor App](https://hemolink-live.onrender.com). Click **"Join Network"**.
3.  **Action:** Click **"BROADCAST SOS"** on the Laptop.
4.  **Result:** The Phone buzzes. Click **"I'm Coming"**, and watch the **Blue Marker** appear on the Laptop map!

---

## 💻 How to Run This Project Locally
If you want to download and run this code on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/vikash7762/hemolink-live.git](https://github.com/vikash7762/hemolink-live.git)
    cd hemolink-live
    ```

2.  **Create a virtual environment (Optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    * Create a `.env` file in the root folder.
    * Add your MongoDB Connection String: `MONGO_URI=your_mongodb_url_here`

5.  **Run the server:**
    ```bash
    uvicorn app.main:app --reload
    ```
6.  Open `http://127.0.0.1:8000` in your browser.

---
*Built by [Vikash] • 2026*