import os

from flask import Flask

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('chatpush.settings')
    app.config.root_path = os.getcwd()
    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.cfg'):
            app.config.from_pyfile(config)

    from .routes import route_bp
    app.register_blueprint(route_bp)
    return app


app = create_app()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add(
        'Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
