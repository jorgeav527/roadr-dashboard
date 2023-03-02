from dash import dcc
import dash_bootstrap_components as dbc
import plotly.express as px


def blank_fig():
    fig = px.scatter(x=None, y=None)
    fig.update_layout(
        title="Pick a Car Maker[Model]",
        xaxis=dict(title=""),
        yaxis=dict(title=""),
        template="plotly_dark",
        margin=dict(l=50, r=50, t=70, b=0),
        autosize=True,
        height=250,
    )
    return fig


scatter_chart_users_vehicles_services = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(
                    id="scatter-chart-users-vehicles-services-amount",
                    figure=blank_fig(),
                    config={"displayModeBar": False},
                ),
                dcc.Graph(
                    id="scatter-chart-users-vehicles-services-duration",
                    figure=blank_fig(),
                    config={"displayModeBar": False},
                ),
                dcc.Graph(
                    id="scatter-chart-users-vehicles-services-distance",
                    figure=blank_fig(),
                    config={"displayModeBar": False},
                ),
            ],
        ),
    ],
    class_name="mb-2",
)
