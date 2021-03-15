from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return "Mission Planning"


@app.route('/list_prof/<typ>')
def training(typ):
    param = dict()
    param['text'] = "Миссия Колонизация Марса"
    param['typ'] = typ
    param['sec_text'] = 'Список профессий'
    param['small_text'] = "И на Марсе будут яблони цвести!"
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.6')