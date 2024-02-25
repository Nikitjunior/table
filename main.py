from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



@app.route('/index')
def index():
    title = "Заготовка"
    return render_template('base.html', title=title)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    if sex == "male":
        color = "red"
        if int(age) < 21:
            color = "orange"
            picture = "child.jpg"
    else:
        color = "blue"
        if int(age) < 21:
            color = "skyBlue"
            picture = "child.jpg"
    if int(age) >= 21:
        picture = "adult.jpg"

    return render_template("table.html", title="Цвет каюты", color=color, picture=picture)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
