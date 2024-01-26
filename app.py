import dash

FONT_AWESOME = ["https://use.fontawesome.com/releases/v5.10.2/css/all.css"]

def create_app():
    app = dash.Dash(__name__, external_stylesheets=FONT_AWESOME)
    app.scripts.config.serve_locally = True
    server = app.server
    return app
