from dash import html
import dash_bootstrap_components as dbc

swith_users = dbc.Card(
    [
        dbc.CardHeader(
            html.H5("Select:", className="card-title mb-0"),
        ),
        dbc.CardBody(
            dbc.Checklist(
                options=[
                    {"label": "Client", "value": "isClient"},
                    {"label": "Specialist", "value": "isSpecialist"},
                ],
                value=["isClient", "isSpecialist"],
                id="swith-users",
                switch=True,
                className="ml-2",
            ),
        ),
    ]
)
