from dash import dcc
import dash_bootstrap_components as dbc

from .layout_components.side_bar import offcanvas
from .layout_components.content import content


layout = dbc.Container(
    [
        dcc.Location(id="url"),
        dbc.Row(
            [
                dbc.Col(offcanvas, width=0),
                dbc.Col(content, width=12),
            ]
        ),
    ],
    fluid=True,
    style={"fontFamily": "Inter"},
)
