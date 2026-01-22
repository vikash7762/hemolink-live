from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# -------------------------------------------
# 1. Location Schema (GeoJSON Standard)
# This handles the map coordinates.
# -------------------------------------------
class Location(BaseModel):
    type: str = "Point"
    # IMPORTANT: MongoDB expects [Longitude, Latitude]
    coordinates: List[float] 

# -------------------------------------------
# 2. User Schema (The Donor)
# This defines what data we need to register a user.
# -------------------------------------------
class UserCreate(BaseModel):
    name: str
    phone: str
    blood_group: str  # e.g., "O+", "A-"
    location: Location
    is_active: bool = True  # If False, they won't get alerts

# -------------------------------------------
# 3. Request Schema (The Emergency)
# This defines what data we need to ask for blood.
# -------------------------------------------
class BloodRequestCreate(BaseModel):
    requester_name: str
    blood_group_needed: str
    location: Location