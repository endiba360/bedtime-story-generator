from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
# Define the database and collections
db = client["bedtime_story_generator"]
users_collection = db["users"]  # For user data
stories_collection = db["stories"]  # For storing generated stories
