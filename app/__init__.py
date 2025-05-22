from flask import Flask
from flask_login import LoginManager
from .users import users
from .user_model import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    user = users.get(user_id)
    if user:
        return User(user_id, user['role'])
    return None

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # TODO: заменить на .env

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .routes import main
    app.register_blueprint(main)

    return app




