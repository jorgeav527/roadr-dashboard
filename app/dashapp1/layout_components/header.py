from dash import html
import dash_bootstrap_components as dbc

new_admin_user = dbc.Row(
    [
        dbc.Col(
            dbc.NavbarBrand(
                "User Name",
                id="username",
                class_name="mx-2 display-6",
            ),
        ),
        dbc.Col(
            [
                dbc.Button(
                    [
                        html.I(className="fa-solid fa-user-plus me-2"),
                        "Admin Staff",
                    ],
                    id="open",
                    n_clicks=0,
                    outline=True,
                    size="md",
                    color="danger",
                    class_name="me-2",
                ),
            ],
            width="auto",
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header")),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="", n_clicks=0)
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

header = dbc.Navbar(
    [
        # Use row and col to control vertical alignment of logo / brand
        dbc.Row(
            [
                # dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                dbc.Col(
                    dbc.Button(
                        html.I(className="fa-solid fa-right-from-bracket"),
                        id="open-offcanvas-scrollable",
                        n_clicks=0,
                        color="dark",
                        outline=True,
                    ),
                ),
                dbc.Col(
                    dbc.NavbarBrand(
                        "Roadr",
                        class_name="ms-2 fs-4",
                        href="https://roadr.com/",
                        external_link=False,
                        style={"textDecoration": "none"},
                    )
                ),
            ],
            align="center",
            className="g-0 ms-2",
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0, class_name="me-2"),
        dbc.Collapse(
            new_admin_user,
            id="navbar-collapse",
            is_open=False,
            navbar=True,
        ),
    ],
    color="dark",
    dark=True,
)
