from dash import dcc
import dash_bootstrap_components as dbc

from .header import header
from .swith_users import swith_users
from .cards_users import (
    card_total_users,
    card_active_users,
    card_verify_users,
    card_deleted_users,
)
from .cards_social import (
    card_facebook,
    card_instagram,
    card_linkedin,
    card_twiter,
)
from .bar_chart_users_by_date import bar_chart_users_by_date
from .bar_chart_user_preference_signup import bar_chart_user_preference_signup
from .bar_chart_users_count import bar_chart_users_count
from .bar_chart_users_vehicles import bar_chart_users_vehicles
from .scatter_chart_users_vehicles_services import scatter_chart_users_vehicles_services

dashboard_users = [
    dbc.Row(
        [
            dbc.Col(header),
        ],
        class_name="mb-3",
    ),
    dbc.Row(
        [
            dbc.Col([swith_users], xl=2, lg=2, md=12, class_name="mb-2"),
            dbc.Col(
                [
                    dbc.Row(
                        [
                            dbc.Col([card_total_users], xl=3, lg=3, md=3, sm=6, xs=6),
                            dbc.Col([card_active_users], xl=3, lg=3, md=3, sm=6, xs=6),
                            dbc.Col([card_verify_users], xl=3, lg=3, md=3, sm=6, xs=6),
                            dbc.Col([card_deleted_users], xl=3, lg=3, md=3, sm=6, xs=6),
                        ],
                        class_name="mb-2",
                    ),
                    dbc.Row(
                        [
                            dbc.Col([card_instagram], xl=3, lg=3, md=3, sm=6, xs=6),
                            dbc.Col([card_twiter], xl=3, lg=3, md=3, sm=6, xs=6),
                            dbc.Col([card_linkedin], xl=3, lg=3, md=3, sm=6, xs=6),
                            dbc.Col([card_facebook], xl=3, lg=3, md=3, sm=6, xs=6),
                        ],
                        class_name="mb-2",
                    ),
                ],
                xl=10,
                lg=10,
                md=12,
            ),
        ],
        class_name="mb-2",
    ),
    dbc.Row(
        [
            dbc.Col([bar_chart_users_by_date], xl=6, lg=6, md=6, sm=12, xs=12),
            dbc.Col([bar_chart_users_count], xl=3, lg=3, md=3, sm=12, xs=12),
            dbc.Col([bar_chart_user_preference_signup], xl=3, lg=3, md=3, sm=12, xs=12),
        ],
        class_name="mb-2",
    ),
    dbc.Row(
        [
            dbc.Col([bar_chart_users_vehicles], xl=6, lg=6, md=6, sm=12, xs=12),
            dbc.Col(
                [scatter_chart_users_vehicles_services], xl=6, lg=6, md=6, sm=12, xs=12
            ),
        ],
        class_name="mb-2",
    ),
    dcc.Store(id="user-store"),
]
