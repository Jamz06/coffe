# -*- coding: utf-8 -*-

from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
# from flask_admin import Admin



# Navbar
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Separator



# Инициализация flask
app = Flask(__name__)
# Подключение конфигурций из config.py
app.config.from_object(Config)

# Создание экземпляра SQLAlchemy для ORM
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Инициализация расширения LoginManager
login = LoginManager(app)
# Указание на функцию, куда отправлять незарегистрированных
login.login_view = 'login'
# Переопределение сообщения для незареганых
login.login_message = "Пожалуйста, войдите чтобы перейти к просмотру."

# Инициализация расширения Bootstrap
bootstrap = Bootstrap(app)

# Инициализация Админки
#admin = Admin(app)



nav = Nav()

nav.init_app(app)

@nav.navigation()
def mynavbar():
    return Navbar(
        'Территория чая и кофе',
        View(
            'Главная',
            'index'
        ),
        View(
            'Выход',
            'logout'
        )

    )

# Подключение остальных
from app import routes, models, errors 

#, admin


