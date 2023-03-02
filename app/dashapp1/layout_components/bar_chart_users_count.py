from dash import dcc
import dash_bootstrap_components as dbc


bar_chart_users_count = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(
                    id="bar-chart-users-count",
                    config={"displayModeBar": False},
                )
            ],
        ),
    ],
    class_name="mb-2",
)
