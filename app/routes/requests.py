from fastapi import APIRouter
from app.database import requests_collection, users_collection
from app.models import BloodRequestCreate
from datetime import datetime
from app.routes.websocket import manager
from pydantic import BaseModel

# --- CRITICAL CHANGE: We use "router", NOT "app" ---
router = APIRouter()

@router.post("/request-blood")  # <--- Make sure this says "router"
async def create_blood_request(request: BloodRequestCreate):
    # 1. Save the Request
    req_data = request.dict()
    req_data["created_at"] = datetime.utcnow()
    req_data["status"] = "pending"
    
    await requests_collection.insert_one(req_data)
    
    # 2. Find Nearby Donors
    nearby_donors = await users_collection.find({
        "blood_group": request.blood_group_needed,
        "is_active": True,
        "location": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": request.location.coordinates
                },
                "$maxDistance": 5000 
            }
        }
    }).to_list(length=100)
    
    # 3. Send Alerts
    donors_notified = []
    alert_message = f"URGENT: {request.blood_group_needed} blood needed!"
    
    for donor in nearby_donors:
        donor_id = str(donor["_id"])
        donors_notified.append(donor_id)
        await manager.send_personal_message(alert_message, donor_id)
    
    return {
        "message": "Request Created",
        "donors_found": len(nearby_donors),
        "nearby_donor_ids": donors_notified
    }

# ---------------------------------------------------------
# NEW: Handle the "I'm Coming" Button Click
# ---------------------------------------------------------

# 1. Define the input model
class AcceptRequest(BaseModel):
    request_id: str
    donor_id: str
    donor_name: str

# 2. The "I'm Coming" Endpoint (Updated to Notify Hospital)
@router.post("/accept-request")
async def accept_blood_request(data: AcceptRequest):
    print(f"✅ HERO FOUND: {data.donor_name} is on the way!")
    
    # NEW: Notify the Hospital Admin via WebSocket
    try:
        await manager.send_personal_message(
            f"✅ DONOR FOUND: {data.donor_name} is coming!", 
            "hospital_admin"
        )
    except:
        print("Hospital not connected via WebSocket (Is the Hospital Tab open?)")

    return {"message": "Thank you! The hospital has been notified."}