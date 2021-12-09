from dash import html


def create_layout(*path):
    layout = html.Div([f"Hello from Bar Dash: path = {path}"])

    return layout
