from fastapi import APIRouter
from app.database import requests_collection, users_collection
from app.models import BloodRequestCreate, AcceptRequest  # <--- IMPORTED FROM MODELS
from datetime import datetime
from app.routes.websocket import manager
import json  # <--- NEW: Needed to send data packets

router = APIRouter()

@router.post("/request-blood") 
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
# NEW: Handle the "I'm Coming" Button Click (WITH GPS!)
# ---------------------------------------------------------

@router.post("/accept-request")
async def accept_blood_request(data: AcceptRequest):
    print(f"✅ HERO FOUND: {data.donor_name} is coming from {data.latitude}, {data.longitude}")
    
    # 1. Create a Data Packet (JSON)
    # This bundles the name and location together
    response_data = {
        "event": "donor_coming",
        "name": data.donor_name,
        "lat": data.latitude,
        "lng": data.longitude
    }

    # 2. Notify the Hospital Admin via WebSocket
    # We send the packet as a STRING so the frontend can parse it
    try:
        await manager.send_personal_message(
            json.dumps(response_data), 
            "hospital_admin"
        )
    except:
        print("Hospital not connected via WebSocket")

    return {"message": "Thank you! The hospital sees your location now."}