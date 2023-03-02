from dash import html
import dash_bootstrap_components as dbc


# print(get_asset_url("roadrLogo.svg"), _get_paths())

side_bar = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.NavbarBrand(
                    "Roadr",
                    class_name="fs-4 m-auto",
                    href="https://roadr.com/",
                    external_link=False,
                    style={
                        "textDecoration": "none",
                        "text-align": "center",
                    },
                ),
                dbc.Nav(
                    [
                        dbc.NavLink(
                            [html.I(className="fa-solid fa-circle-user")],
                            href="/user-admin/",
                            active="exact",
                            style={
                                "font-size": "2em",
                                "text-align": "center",
                            },
                        ),
                        html.Hr(),
                        dbc.NavLink(
                            [html.I(className="fa-solid fa-house")],
                            href="/dashboard-company/",
                            active="exact",
                            style={
                                "font-size": "1.5em",
                                "text-align": "center",
                            },
                        ),
                        dbc.NavLink(
                            [html.I(className="fa-solid fa-people-robbery")],
                            href="/dashboard-users/",
                            active="exact",
                            style={
                                "font-size": "1.5em",
                                "text-align": "center",
                            },
                        ),
                        dbc.NavLink(
                            [html.I(className="fa-solid fa-arrows-down-to-people")],
                            href="/dashboard-third-parties/",
                            active="exact",
                            style={
                                "font-size": "1.5em",
                                "text-align": "center",
                            },
                        ),
                        dbc.NavLink(
                            [html.I(className="fa-solid fa-globe")],
                            href="/geo-ref/",
                            active="exact",
                            style={
                                "font-size": "1.5em",
                                "text-align": "center",
                            },
                        ),
                        dbc.NavLink(
                            [html.I(className="fa-solid fa-money-bill-trend-up")],
                            href="/revenue/",
                            active="exact",
                            style={
                                "font-size": "1.5em",
                                "text-align": "center",
                            },
                        ),
                        dbc.NavLink(
                            [html.I(className="fa-solid fa-bell")],
                            href="/notifications/",
                            active="exact",
                            style={
                                "font-size": "1.5em",
                                "text-align": "center",
                            },
                        ),
                        dbc.NavLink(
                            [html.I(className="fa-solid fa-question")],
                            href="/page-1/",
                            active="exact",
                            style={
                                "font-size": "1.5em",
                                "text-align": "center",
                            },
                        ),
                        dbc.NavLink(
                            [html.I(className="fa-solid fa-exclamation")],
                            href="/404/",
                            active="exact",
                            style={
                                "font-size": "1.5em",
                                "text-align": "center",
                            },
                        ),
                    ],
                    vertical=True,
                    pills=True,
                ),
            ]
        )
    ],
    color="light",
    style={"fontFamily": "Inter"},
)

offcanvas = html.Div(
    [
        dbc.Offcanvas(
            side_bar,
            id="offcanvas-scrollable",
            scrollable=True,
            is_open=False,
            style={"width": "145px"},
        ),
    ]
)
