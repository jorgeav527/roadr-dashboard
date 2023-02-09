from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import pymongo
from bson.objectid import ObjectId
from flask_login import current_user

# # Connect to server on the cloud
# client = pymongo.MongoClient(
#     "mongodb+srv://roadr_dev:7juzcxuvMpMlyfHO@devcluster.8igvo.mongodb.net/?retryWrites=true&w=majority"
# )
# # test the connection
# # db = client.test
# # print(db)
# # exit()

# # Go into the database I created
# db = client["dev"]
# # Go into one of my database's collection (table)
# collection = db["users"]
# # Testing collections in users
# testing = collection.find()
# print(list(testing))

layout = html.Div(
    id="main",
    children=[
        html.H1(id="username"),
        html.H1("Stock Tickers"),
        dcc.Dropdown(
            id="dropdown",
            options=["Gold", "MediumTurquoise", "LightGreen"],
            value="Gold",
            clearable=False,
        ),
        dcc.Graph(id="graph"),
        dcc.Store(id="user-store"),
    ],
)
