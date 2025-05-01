import os
from dotenv import load_dotenv
from os import getenv
import pymongo from pymongo

load_dotenv()

API_ID = int(os.getenv("29933911"))
API_HASH = os.getenv("7203358c613c038dbd69e84d969cc0bd")
BOT_TOKEN = os.getenv("7037167859:AAFQ1cdHGaim4FLOHtLPoOXptZM42hg5Ml0")
ALLOWED_USERS = [int(id) for id in os.getenv("ALLOWED_USERS").split("6489636766,")]
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://mongodbalox:rusmanto12@cluster0.1jwxyor.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
