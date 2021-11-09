
import os
from flask import Flask, g
from flask_jwt_extended import JWTManager, current_user


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        PASSWORD='1234',
        JWT_TOKEN_LOCATION=["headers", "cookies"],
        JWT_SECRET_KEY="top secret",
        JWT_ACCESS_TOKEN_EXPIRES=False,
    )

    jwt = JWTManager(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        return {
            "username": "admin",
        }

    from server import auth
    app.register_blueprint(auth.bp)

    from server import index
    app.register_blueprint(index.bp)
    app.add_url_rule('/', endpoint='index')

    @auth.bp.before_app_request
    def load_logged_in_user():
        if current_user is not None:
            g.user = current_user
        else:
            g.user = None

    return app


app = create_app()
