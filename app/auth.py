from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from .users import users
from .user_model import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = users.get(username)

        if user and user['password'] == password:
            user_obj = User(username, user['role'])
            login_user(user_obj)
            return redirect(url_for('main.dashboard'))
        else:
            return render_template('login.html', error='Неверный логин или пароль')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

