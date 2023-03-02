from dash import dcc
import dash_bootstrap_components as dbc


bar_chart_user_preference_signup = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(
                    id="bar-chart-user-preference-signup",
                    config={"displayModeBar": False},
                )
            ],
        ),
    ],
    class_name="mb-2",
)
