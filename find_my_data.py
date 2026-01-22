import asyncio
from app.database import client

async def check_connection():
    try:
        # 1. Ask MongoDB what databases exist
        print("🔍 Scanning MongoDB Cluster...")
        dbs = await client.list_database_names()
        
        print("\n✅ I CAN SEE THESE DATABASES:")
        for db in dbs:
            print(f" - {db}")
            
    except Exception as e:
        print(f"\n❌ Connection Failed: {e}")

# Run the check
if __name__ == "__main__":
    asyncio.run(check_connection())