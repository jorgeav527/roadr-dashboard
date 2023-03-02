from dash import dcc
import dash_bootstrap_components as dbc


bar_chart_users_vehicles = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(
                    id="bar-chart-users-vehicles",
                    style={
                        "maxHeight": "600px",
                        "maxWidth": "600px",
                        "overflow": "scroll",
                    },
                    config={"displayModeBar": "hover"},
                )
            ],
        ),
    ],
    class_name="mb-2",
)
