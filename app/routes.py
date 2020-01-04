from flask import render_template, flash, redirect, url_for, request, send_from_directory
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app
from app.forms import LoginForm, RegisterForm, IndexForm
from app.models import *

current_user: User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильное имя пользователя или пароль!')
            return redirect(url_for('login'))
        login_user(user, remember=True)
        next_page = request.args.get('redirect')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        flash('Вход успешен!')
        return redirect(next_page)
    return render_template('user/login.html', title='Вход', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('Вы вышли из системы!')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, is_admin=False, score=0)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрированы!')
        return redirect(url_for('login'))
    return render_template('user/register.html', title='Регистрация', form=form)


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = IndexForm()
    if form.validate_on_submit():
        return redirect(url_for('game'))
    elif request.method == 'GET':
        form.language = 0
    return render_template('index.html', form=form)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/game/<int:game_id>')
def game(game_id):
    return render_template('game.html', game_id=game_id)


@app.route('/api/get_initial_config')
def get_initial_config():
    return
