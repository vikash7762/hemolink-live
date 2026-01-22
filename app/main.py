from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import users_collection
from app.models import UserCreate
from app.routes import requests, websocket
import os

app = FastAPI()

# 1. SECURITY: Allow connections from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. CONNECT ROUTERS (The Logic)
app.include_router(requests.router)
app.include_router(websocket.router)

# 3. SERVE FRONTEND (The Visuals)
# This tells FastAPI: "If someone asks for a file, look in the frontend folder"
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Home Page -> Serve index.html (Donor App)
@app.get("/")
async def read_root():
    return FileResponse('frontend/index.html')

# Hospital Page -> Serve hospital.html (Doctor Dashboard)
@app.get("/hospital")
async def read_hospital():
    return FileResponse('frontend/hospital.html')

# Register Endpoint (Kept here for easy access)
@app.post("/register")
async def register_user(user: UserCreate):
    user_data = user.dict()
    result = await users_collection.insert_one(user_data)
    return {"message": "User Registered successfully", "id": str(result.inserted_id)}