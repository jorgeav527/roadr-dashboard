from datetime import datetime as dt

from dash import Input, Output, State, html
import dash_bootstrap_components as dbc
from flask_login import current_user
import pandas as pd
import plotly.express as px

from .data_calls.data import df_users, df_vehicles, df_services
from .data_calls.scrapy_instagram import get_instagram_followers
from .layout_components.dashboard_user_admin import dashboard_user_admin
from .layout_components.dashboard_company import dashboard_company
from .layout_components.dashboard_users import dashboard_users
from .layout_components.dashboard_third_parties import dashboard_third_parties
from .layout_components.dashboard_geo_ref import dashboard_geo_ref
from .layout_components.dashboard_revenue import dashboard_revenue
from .layout_components.dashboard_notifications import dashboard_notifications


def register_callbacks(dashapp):
    @dashapp.callback(
        Output("offcanvas-scrollable", "is_open"),
        Input("open-offcanvas-scrollable", "n_clicks"),
        State("offcanvas-scrollable", "is_open"),
    )
    def toggle_offcanvas_scrollable(n1, is_open):
        if n1:
            return not is_open
        return is_open

    @dashapp.callback(
        Output(component_id="user-store", component_property="data"),
        Input(component_id="swith-users", component_property="value"),
        State(component_id="user-store", component_property="data"),
    )
    def cur_user(value, data):
        """
        When the "swith-users" is triger when the page is load.
        Output the current user name into the "user-store".
        ->Inputs
            value:str = the value of the swith-users.
        ()State
            data:{} = a key value pair to save the current user.
        <-Output
            data:{} = outputed and save the users name.
        """
        if current_user.is_authenticated:
            return current_user.username

    @dashapp.callback(
        Output(component_id="username", component_property="children"),
        Input(component_id="user-store", component_property="data"),
    )
    def username(data):
        """
        Get the user name of the user and return a string.
        ->Inputs
            data:str = the name of the person.
        <-Output
            children:[] = outputed and name user.
        """
        if data is None:
            return ""
        else:
            return f"Hello! {data}"

    @dashapp.callback(
        Output(component_id="page-content", component_property="children"),
        Input(component_id="url", component_property="pathname"),
    )
    def render_page_content(pathname):
        """
        Render the page selected in the routes.
        ->Inputs
            data:str = the path to be redirected.
        <-Output
            children:[] = the page content.
        """
        if pathname == "/user-admin/":
            return dashboard_user_admin
        elif pathname == "/dashboard-users/":
            return dashboard_users
        elif pathname == "/dashboard-company/":
            return dashboard_company
        elif pathname == "/dashboard-third-parties/":
            return dashboard_third_parties
        elif pathname == "/geo-ref/":
            return dashboard_geo_ref
        elif pathname == "/revenue/":
            return dashboard_revenue
        elif pathname == "/notifications/":
            return dashboard_notifications
        elif pathname == "/page-1/":
            return html.Div(
                [
                    dbc.Button(
                        html.I(className="fa-solid fa-right-from-bracket"),
                        id="open-offcanvas-scrollable",
                        n_clicks=0,
                        color="dark",
                        outline=True,
                    ),
                    html.H1("Some page", className="text-warning"),
                    html.Hr(),
                    html.P(f"The pathname {pathname} was not recognised..."),
                ],
                className="p-3 bg-light rounded-3",
            )
        # If the user tries to reach a different page, return a 404 message
        else:
            return html.Div(
                [
                    dbc.Button(
                        html.I(className="fa-solid fa-right-from-bracket"),
                        id="open-offcanvas-scrollable",
                        n_clicks=0,
                        color="dark",
                        outline=True,
                    ),
                    html.H1("404: Not found", className="text-danger"),
                    html.Hr(),
                    html.P(f"The pathname {pathname} was not recognised..."),
                ],
                className="p-3 bg-light rounded-3",
            )

    @dashapp.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        # This to toggle the sandwich for the navigation bar.
        if n:
            return not is_open
        return is_open

    @dashapp.callback(
        Output("modal", "is_open"),
        [Input("open", "n_clicks"), Input("close", "n_clicks")],
        [State("modal", "is_open")],
    )
    def toggle_modal(n1, n2, is_open):
        # This to open a modal.
        if n1 or n2:
            return not is_open
        return is_open

    @dashapp.callback(
        [
            Output(component_id="total-users", component_property="children"),
            Output(component_id="active-users", component_property="children"),
            Output(component_id="verify-users", component_property="children"),
            Output(component_id="deleted-users", component_property="children"),
            Output(component_id="bar-chart-users-count", component_property="figure"),
            Output(
                component_id="bar-chart-user-preference-signup",
                component_property="figure",
            ),
        ],
        Input(component_id="swith-users", component_property="value"),
    )
    def counting_users(columns):
        """
        Getting the total, active, verified and deleted users filtered by type of user.
        Build and output a barchart to get the total, active, verified and deleted users.
        Build and output a barchart the prefer platform for signup.
        ->Inputs
            swith-users:[] = a list of the type of users [isClient, isSpecialist].
        <-Output
            total-users:int = the total number of users.
            active-users:int = the total number of active users.
            verify-users:int = the total verified numbers of users.
            deleted-users:int =  the total of deleted numbers of users.
            bar-chart-users-count:obj = a bar chart figure.
            bar-chart-user-preference-signup:obj = a bar chart figure.
        """
        total = 0
        active = 0
        deleted = 0
        verified = 0
        df_signups_per_prefer_platform = pd.DataFrame(
            columns=["registerType", "signups"]
        )
        user_colors = px.colors.sequential.Oranges_r
        signup_colors = px.colors.sequential.Oranges_r
        for col in columns:
            df_type_of_user = df_users[df_users[col]]
            _count = df_users[col].sum()
            _active = df_type_of_user["isActive"].sum()
            _verified = df_type_of_user["isValidCertification"].sum()
            _deleted = df_type_of_user["isDeleted"].sum()
            _df_signups_per_prefer_platform = (
                df_type_of_user.groupby("registerType")["_id"]
                .count()
                .reset_index(name="signups")
            )
            df_signups_per_prefer_platform = pd.concat(
                [df_signups_per_prefer_platform, _df_signups_per_prefer_platform]
            )
            total += _count
            active += _active
            verified += _verified
            deleted += _deleted

        data = {
            "names": [
                "Total",
                "Active",
                "Verified",
                "Deleted",
            ],
            "counts": [total, active, verified, deleted],
        }
        df_inter = pd.DataFrame(data)
        df_signups_per_prefer_platform_grouped = (
            df_signups_per_prefer_platform.groupby("registerType")["signups"]
            .sum()
            .reset_index(name="signups")
        )

        fig_bar_chard_users_count = px.bar(
            df_inter,
            x="names",
            y="counts",
            color="names",
            color_discrete_sequence=[
                user_colors[i] for i in range(0, len(user_colors), 3)
            ][:4],
            text_auto=True,
        )
        fig_bar_chard_users_count.update_layout(
            bargap=0.5,
            title="By State:",
            xaxis=dict(title=""),
            yaxis=dict(title=""),
            template="plotly_dark",
            showlegend=False,
            margin=dict(l=0, r=25, t=70, b=0),
            autosize=True,
            height=250,
        )
        fig_bar_chart_user_preference_signup = px.bar(
            df_signups_per_prefer_platform_grouped,
            x="signups",
            y="registerType",
            color="registerType",
            orientation="h",
            height=250,
            text_auto=True,
            color_discrete_sequence=[
                signup_colors[i] for i in range(0, len(signup_colors), 3)
            ][:3],
        )
        fig_bar_chart_user_preference_signup.update_layout(
            bargap=0.5,
            title="By Platform:",
            xaxis=dict(title=""),
            yaxis=dict(title=""),
            template="plotly_dark",
            showlegend=False,
            margin=dict(l=0, r=25, t=70, b=0),
            autosize=True,
            height=250,
        )
        return (
            total,
            active,
            verified,
            deleted,
            fig_bar_chard_users_count,
            fig_bar_chart_user_preference_signup,
        )

    @dashapp.callback(
        Output(component_id="bar-chard-users-by-date", component_property="figure"),
        [
            Input(component_id="swith-users", component_property="value"),
            Input(component_id="dropdown-for-date", component_property="value"),
        ],
    )
    def counting_users_by_date(columns, value):
        """
        Build and output a bar chart to get all the users filtered by the type of user,
        and filtered by date (day, month and year).
        ->Inputs
            swith-users:[] = a list of the type of users [isClient, isSpecialist].
            dropdown-for-date:str = a string D for day, M for month and Y for year.
        <-Output
            bar-chard-users-by-date:obj = a bar chart figure.
        """
        df_copy = df_users.copy()
        _x = "Month" if value == "M" else "Year" if value == "Y" else "Day"
        df_monthly_users = pd.DataFrame(columns=["date", "_id"])
        for col in columns:
            df_type_of_user = df_copy[df_copy[col]]
            _df_monthly_users = (
                df_type_of_user.groupby(pd.Grouper(key="date", freq=f"{value}"))["_id"]
                .count()
                .reset_index()
            )
            df_monthly_users = pd.concat([df_monthly_users, _df_monthly_users])

        df_monthly_users = df_monthly_users.groupby("date")["_id"].sum().reset_index()
        df_monthly_users["growth_rate"] = df_monthly_users["_id"].pct_change()

        fig = px.bar(
            df_monthly_users,
            x="date",
            y="_id",
            color_discrete_sequence=["darkorange"],
            text_auto=True,
        )
        fig.add_scatter(
            x=df_monthly_users["date"],
            y=df_monthly_users["growth_rate"],
            mode="lines+markers",
            name="Growth Rate",
            line=dict(color="white", width=2),
        )
        fig.update_layout(
            title=f"By {_x}:",
            bargap=0.5,
            xaxis=dict(title="", rangeslider_visible=True),
            yaxis=dict(title=""),
            template="plotly_dark",
            margin=dict(l=50, r=50, t=70, b=0),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="top",
                y=1.1,
                xanchor="center",
                x=0.5,
            ),
            autosize=True,
            height=350,
            width=650,
        )

        return fig

    @dashapp.callback(
        Output(component_id="bar-chart-users-vehicles", component_property="figure"),
        Input(component_id="swith-users", component_property="value"),
    )
    def users_and_vehicles_counting(columns):
        """
        Build and output a horizontal bar chart to get the users vehicles filtered by the type of user,
        In the y axis the maker and model.
        ->Inputs
            swith-users:[] = a list of the type of users [isClient, isSpecialist].
        <-Output
            bar-chart-users-vehicles:obj = a bar chart figure.
        """
        df_copy_users = df_users.copy().rename(columns={"_id": "user_id"})
        df_copy_vehicles = df_vehicles.copy().rename(columns={"user": "user_id"})
        df_users_vehicles = pd.merge(
            df_copy_users, df_copy_vehicles, on="user_id", how="left"
        )
        df = pd.DataFrame(columns=["maker", "model", "user_id"])
        for col in columns:
            df_type_of_user = df_users_vehicles[df_users_vehicles[col]]
            _df = (
                df_type_of_user.groupby(["maker", "model"])["user_id"]
                .count()
                .reset_index()
            )

            df = pd.concat([df, _df])

        df = df.groupby(["maker", "model"])["user_id"].sum().reset_index()
        colors = px.colors.sequential.Oranges_r
        fig = px.bar(
            df,
            x="user_id",
            y="maker",
            color="model",
            color_discrete_sequence=colors,
            orientation="h",
            custom_data=["maker", "model", "user_id"],
        )
        fig.update_layout(
            title="By Car:",
            xaxis=dict(title="Users"),
            yaxis=dict(title="Maker-[Model]"),
            template="plotly_dark",
            margin=dict(l=50, r=50, t=70, b=0),
            showlegend=True,
            autosize=True,
            height=1000,
            width=600,
        )
        return fig

    @dashapp.callback(
        [
            Output(
                component_id="scatter-chart-users-vehicles-services-amount",
                component_property="figure",
            ),
            Output(
                component_id="scatter-chart-users-vehicles-services-duration",
                component_property="figure",
            ),
            Output(
                component_id="scatter-chart-users-vehicles-services-distance",
                component_property="figure",
            ),
        ],
        Input(component_id="bar-chart-users-vehicles", component_property="clickData"),
        prevent_initial_call=True,
    )
    def users_and_vehicles_tendencies(click_data):
        """
        Build and output a horizontal bar chart to get the users vehicles filtered by the type of user,
        In the y axis the maker and model.
        ->Inputs
            bar-chart-users-vehicles:[] = a list of the type of users [isClient, isSpecialist].
        <-Output
            bar-chart-users-vehicles:obj = a bar chart figure.
        """
        df_copy_users = df_users.copy().rename(columns={"_id": "user_id"})
        df_copy_vehicles = df_vehicles.copy().rename(columns={"user": "user_id"})
        df_copy_services = df_services.copy().rename(columns={"user": "user_id"})

        df_users_vehicles = pd.merge(
            df_copy_users, df_copy_vehicles, on="user_id", how="left"
        )
        df_users_vehicles_services = pd.merge(
            df_users_vehicles, df_copy_services, on="user_id", how="inner"
        )
        colors = px.colors.sequential.Oranges_r
        columns = [
            "user_id",
            "isClient",
            "isSpecialist",
            "model",
            "maker",
            "serviceType",
            "createdAt",
            "status",
            "duration",
            "distance",
            "tip",
            "amount",
        ]
        df_users_vehicles_services = df_users_vehicles_services[columns]
        selected_maker = click_data["points"][0]["customdata"][0]
        selected_model = click_data["points"][0]["customdata"][1]
        df_users_vehicles_services_filtered = df_users_vehicles_services[
            df_users_vehicles_services["maker"] == selected_maker
        ]
        fig_amount = px.scatter(
            df_users_vehicles_services_filtered,
            x="createdAt",
            y="amount",
            color="maker",
            color_discrete_sequence=["darkorange"],
        )
        fig_amount.update_layout(
            title=f"{selected_maker}[{selected_model}] By Amount:",
            xaxis=dict(title="Date"),
            yaxis=dict(title="Amount ($)"),
            template="plotly_dark",
            margin=dict(l=50, r=50, t=70, b=0),
            showlegend=False,
            autosize=True,
            height=250,
        )
        fig_duration = px.scatter(
            df_users_vehicles_services_filtered,
            x="createdAt",
            y="duration",
            color="maker",
            color_discrete_sequence=["darkorange"],
        )
        fig_duration.update_layout(
            title=f"{selected_maker}[{selected_model}] By Duration:",
            xaxis=dict(title="Date"),
            yaxis=dict(title="Duration (s)"),
            template="plotly_dark",
            margin=dict(l=50, r=50, t=70, b=0),
            showlegend=False,
            autosize=True,
            height=250,
        )
        fig_distance = px.scatter(
            df_users_vehicles_services_filtered,
            x="createdAt",
            y="distance",
            color="maker",
            color_discrete_sequence=["darkorange"],
        )
        fig_distance.update_layout(
            title=f"{selected_maker}[{selected_model}] By Distance:",
            xaxis=dict(title="Date"),
            yaxis=dict(title="Distance (km)"),
            template="plotly_dark",
            margin=dict(l=50, r=50, t=70, b=0),
            showlegend=False,
            autosize=True,
            height=250,
        )
        return fig_amount, fig_duration, fig_distance

    @dashapp.callback(
        Output(component_id="instagram-followers", component_property="children"),
        Input(component_id="swith-users", component_property="value"),
    )
    def social_users(columns):
        """
        Getting the total, active, verified users for instagram.
        ->Inputs
            swith-users:[] = a list of the type of users [isClient, isSpecialist].
        <-Output
            instagram-followers:int = the total number of users.
        """
        instagram_followers = get_instagram_followers()

        return instagram_followers
