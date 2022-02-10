from dash import Dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

import flask
import flask_login


def create_app(server, url_prefix=""):
    app = Dash(__name__, server=server, url_base_pathname=url_prefix+"/")
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

    from .layouts import foo
    from .layouts import bar

    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname'),
    )
    def display_page(pathname):
        if not flask_login.current_user.is_authenticated:
            return "403"
        path = pathname.removeprefix(url_prefix).removeprefix("/").split("/")
        if path[0] == "foo":
            return foo.create_layout(*path)
        elif path[0] == "bar":
            return bar.create_layout(*path)
        else:
            return 'Page not found'
