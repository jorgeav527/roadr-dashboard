from datetime import datetime as dt

from dash import Input, Output, State, html
from flask_login import current_user
import pandas_datareader as pdr
import plotly.graph_objects as go


def register_callbacks(dashapp):
    @dashapp.callback(
        Output("user-store", "data"),
        Input("dropdown", "value"),
        State("user-store", "data"),
    )
    def cur_user(args, data):
        if current_user.is_authenticated:
            return current_user.username

    @dashapp.callback(Output("username", "children"), Input("user-store", "data"))
    def username(data):
        if data is None:
            return ""
        else:
            return f"Hello {data}"

    @dashapp.callback(Output("graph", "figure"), Input("dropdown", "value"))
    def display_color(color):
        fig = go.Figure(
            data=go.Bar(
                y=[2, 3, 1], marker_color=color  # replace with your own data source
            )
        )
        return fig

    @dashapp.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname == "/":
            return html.P("This is the content of the home page!")
        elif pathname == "/page-1":
            return html.P("This is the content of page 1. Yay!")
        elif pathname == "/page-2":
            return html.P("Oh cool, this is page 2!")
        # If the user tries to reach a different page, return a 404 message
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ],
            className="p-3 bg-light rounded-3",
        )
