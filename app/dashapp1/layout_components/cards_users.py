from dash import html
import dash_bootstrap_components as dbc

CARD_ICON_USERS = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}

card_total_users = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("0", className="card-title", id="total-users"),
                    html.P(
                        "Total Users",
                        className="card-text",
                    ),
                ]
            )
        ),
        dbc.Card(
            html.Div(className="fa-solid fa-users", style=CARD_ICON_USERS),
            className="bg-primary",
        ),
    ],
    className="shadow mb-2",
)
card_active_users = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("0", className="card-title", id="active-users"),
                    html.P(
                        "Active Users",
                        className="card-text",
                    ),
                ]
            )
        ),
        dbc.Card(
            html.Div(className="fa-solid fa-user-shield", style=CARD_ICON_USERS),
            className="bg-primary",
        ),
    ],
    className="shadow mb-2",
)
card_verify_users = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("0", className="card-title", id="verify-users"),
                    html.P(
                        "Verified Users",
                        className="card-text",
                    ),
                ]
            )
        ),
        dbc.Card(
            html.Div(className="fa-solid fa-user-check", style=CARD_ICON_USERS),
            className="bg-primary",
        ),
    ],
    className="shadow mb-2",
)
card_deleted_users = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("0", className="card-title", id="deleted-users"),
                    html.P(
                        "Deleted Users",
                        className="card-text",
                    ),
                ]
            )
        ),
        dbc.Card(
            html.Div(className="fa-solid fa-user-slash", style=CARD_ICON_USERS),
            className="bg-primary",
        ),
    ],
    className="shadow mb-2",
)
