from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import uuid
import random

app = FastAPI(title="Mock Cab Booking MCP Server")

# Request model
class CabBookingRequest(BaseModel):
    pickup: str
    destination: str
    time: str  # ISO format preferred, e.g. "2025-07-24T15:00:00"

# Response model
class CabBookingResponse(BaseModel):
    booking_id: str
    confirmation_time: str
    pickup: str
    destination: str
    time: str
    otp: str
    status: str

# Booking endpoint
@app.post("/book_cab", response_model=CabBookingResponse)
def book_cab(request: CabBookingRequest):
    booking_id = str(uuid.uuid4())[:8]  # Short UUID
    otp = str(random.randint(1000, 9999))
    confirmation_time = datetime.now().isoformat()

    return CabBookingResponse(
        booking_id=booking_id,
        confirmation_time=confirmation_time,
        pickup=request.pickup,
        destination=request.destination,
        time=request.time,
        otp=otp,
        status="confirmed"
    )
