from dash import dcc
import dash_bootstrap_components as dbc
from datetime import date

bar_chart_users_by_date = dbc.Card(
    [
        dbc.CardHeader(
            [
                dcc.DatePickerRange(
                    start_date=date(2022, 8, 5),
                    end_date=date(2022, 8, 25),
                    className="mb-2 dbc",
                ),
                dcc.Dropdown(
                    id="dropdown-for-date",
                    options=[
                        {"label": "Day", "value": "D"},
                        {"label": "Month", "value": "M"},
                        {"label": "Year", "value": "Y"},
                    ],
                    value="M",
                    className="mb-2 dbc",
                    style={"width": "150px"},
                ),
            ],
            className="d-flex flex-wrap align-items-start justify-content-between",
        ),
        dbc.CardBody(
            dcc.Graph(
                id="bar-chard-users-by-date",
                style={
                    # "maxHeight": "600px",
                    "maxWidth": "800px",
                    "overflow": "scroll",
                },
                config={"displayModeBar": "hover"},
            )
        ),
    ],
    class_name="mb-2",
)
