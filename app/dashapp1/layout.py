from dash import dcc
from dash import html
import pandas as pd
import pymongo
import dash_bootstrap_components as dbc

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

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "8rem",
    "padding": "2rem 1rem",
    "border-right": "1px solid #f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H4("Roadr", className=""),
        html.Hr(),
        html.P("", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(
    id="main",
    children=[
        html.H4(id="username"),
        dcc.Dropdown(
            id="dropdown",
            options=["Gold", "MediumTurquoise", "LightGreen"],
            value="Gold",
            clearable=False,
        ),
        dcc.Graph(id="graph"),
        dcc.Store(id="user-store"),
    ],
    style=CONTENT_STYLE,
)

layout = html.Div([dcc.Location(id="url"), sidebar, content])
