import motor.motor_asyncio

# --- DIRECT CONNECTION STRING (No .env needed for now) ---
# I have constructed this using the credentials from your screenshot.
MONGO_URL = "mongodb+srv://vikashkumar9504168773:Queue1234@cluster1.brit6sy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

# Connect to the Database
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

# Connect to "hemolink_db"
db = client.hemolink_db

# Define Collections
users_collection = db.get_collection("users")
requests_collection = db.get_collection("requests")