# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

from werkzeug.urls import url_parse

from app import app

from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неверный логин или пароль')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)

        # В адресе, может быть ссылка на запрошенную страницу
        # Парсим, и пишем в переменную next_page
        next_page = request.args.get('next')
        # Если нет аргумента next, или он содержит полный URL, с указанием домена
        # то перенаправляем на index (мало-ли чего мне в next вставят:) )
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', title='Вход', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
