# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Regexp

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class CustomerForm(FlaskForm):
    phone = StringField('Телефон', validators=[Regexp('^8[0-9]{10}')])
    comment = StringField('Коментарий')


class OperationForm(FlaskForm):
    phone = StringField('Телефон')



