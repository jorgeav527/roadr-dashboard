from dash import dcc
import dash_bootstrap_components as dbc

from .header import header

dashboard_user_admin = [
    dbc.Row(
        [
            dbc.Col(header),
        ],
        className="mb-2",
    ),
    dcc.Store(id="user-store"),
]
