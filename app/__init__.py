import dash
from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required
import dash_bootstrap_components as dbc

from config import BaseConfig


def create_app():
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    register_dashapps(server)
    register_extensions(server)
    register_blueprints(server)

    return server


def register_dashapps(app):
    from app.dashapp1.layout import layout
    from app.dashapp1.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }
    dbc_css = (
        "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
    )

    dashapp1 = dash.Dash(
        __name__,
        server=app,
        url_base_pathname="/dashboard-users/",
        assets_folder=get_root_path(__name__) + "/static/assets",
        meta_tags=[meta_viewport],
        external_stylesheets=[dbc.themes.CYBORG, dbc_css, dbc.icons.FONT_AWESOME],
        suppress_callback_exceptions=True,
    )

    with app.app_context():
        dashapp1.title = "Roadr Dash-Board"
        dashapp1.layout = layout
        register_callbacks(dashapp1)

    _protect_dashviews(dashapp1)


def _protect_dashviews(dashapp):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.config.url_base_pathname):
            dashapp.server.view_functions[view_func] = login_required(
                dashapp.server.view_functions[view_func]
            )


def register_extensions(server):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate

    db.init_app(server)
    login.init_app(server)
    login.login_view = "main.login"
    migrate.init_app(server, db)


def register_blueprints(server):
    from app.user.views import server_bp

    server.register_blueprint(server_bp)
