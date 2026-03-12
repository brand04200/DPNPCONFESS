import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CONFESSION_CHANNEL_ID = os.getenv("CONFESSION_CHANNEL_ID")

print("TOKEN loaded:", TOKEN is not None)
print("CONFESSION_CHANNEL_ID loaded:", CONFESSION_CHANNEL_ID is not None)