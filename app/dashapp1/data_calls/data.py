from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pandas as pd

# Connecting with the database.
MONGO_URL = "mongodb+srv://roadr_dev:7juzcxuvMpMlyfHO@devcluster.8igvo.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URL)
try:
    # The ping command is cheap and does not require auth.
    print(client.admin.command("ping"))
except ConnectionFailure:
    print("Server not available")

db_test = client["test"]

# Users
df_users = pd.DataFrame(list(db_test["users"].find()))
df_vehicles = pd.DataFrame(list(db_test["vehicles"].find()))
df_services = pd.DataFrame(list(db_test["services"].find()))

# specialist = df_users["isSpecialist"].value_counts()[True]
# client = df_users["isClient"].value_counts()[True]
