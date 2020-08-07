"""App factory"""

# Required imports
from flask import Flask
from flask_login import LoginManager

login_manager=LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(username):
  return UserModel.query(email)


def create_app():
    """
    Return the flask app instance

    Params:
      - none
    Return:
      - app: The flask app instance
    """
    app = Flask(__name__)

    login_manager.init_app(app)

    from .users import api
    app.register_blueprint(api.bp)

    from .firebase import auth
    app.register_blueprint(auth.bp)

    return app
