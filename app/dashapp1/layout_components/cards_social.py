from dash import html
import dash_bootstrap_components as dbc

CARD_ICON_SOCIAL = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 20,
    "margin": "auto",
}

card_instagram = dbc.CardGroup(
    [
        dbc.Card(
            html.Div(className="fa-brands fa-instagram", style=CARD_ICON_SOCIAL),
            className="bg-primary",
        ),
        dbc.Card(
            html.P("0", className="card-text text-center", id="instagram-followers"),
        ),
    ],
    className="shadow",
)
card_twiter = dbc.CardGroup(
    [
        dbc.Card(
            html.Div(className="fa-brands fa-twitter", style=CARD_ICON_SOCIAL),
            className="bg-primary",
        ),
        dbc.Card(
            html.P("0", className="card-text text-center"),
        ),
    ],
    className="shadow mb-2",
)
card_linkedin = dbc.CardGroup(
    [
        dbc.Card(
            html.Div(className="fa-brands fa-linkedin", style=CARD_ICON_SOCIAL),
            className="bg-primary",
        ),
        dbc.Card(
            html.P("0", className="card-text text-center"),
        ),
    ],
    className="shadow mb-2",
)
card_facebook = dbc.CardGroup(
    [
        dbc.Card(
            html.Div(className="fa-brands fa-facebook", style=CARD_ICON_SOCIAL),
            className="bg-primary",
        ),
        dbc.Card(
            html.P("0", className="card-text text-center"),
        ),
    ],
    className="shadow mb-2",
)
