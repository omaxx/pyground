from dash import html


def create_layout(*path):
    layout = html.Div([f"Hello from Foo Dash: path = {path}"])

    return layout
