from datetime import datetime as dt

from dash import Input, Output, State
from flask_login import current_user
import pandas_datareader as pdr
import plotly.graph_objects as go


def register_callbacks(dashapp):
    # @dashapp.callback(
    #     Output("my-graph", "figure"),
    #     Input("my-dropdown", "value"),
    #     State("user-store", "data"),
    # )
    # def update_graph(selected_dropdown_value, data):
    #     df = pdr.get_data_yahoo(
    #         selected_dropdown_value, start=dt(2017, 1, 1), end=dt.now()
    #     )
    #     return {
    #         "data": [{"x": df.index, "y": df.Close}],
    #         "layout": {"margin": {"l": 40, "r": 0, "t": 20, "b": 30}},
    #     }

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
