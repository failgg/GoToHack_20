from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

from app import app
from app.models import *

app.jinja_env.globals['bootstrap_is_hidden_field'] = lambda field: isinstance(field, HiddenField)


class IndexForm(FlaskForm):
    language = SelectField('Выберите язык программирования:', choices=[('cpp', 'C++'), ('python', 'Python 3')])
    submit = SubmitField('Начать игру')


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

    @staticmethod
    def validate_username(_, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Логин уже занят')
