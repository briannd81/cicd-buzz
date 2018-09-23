import os
import signal
from flask import Flask, render_template
from buzz import generator
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

app = Flask(__name__)
app.secret_key = 'development key'

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

@app.route("/unitconversion")
def unitconversion():
    form = MyForm()
    return render_template('submit.html', form=form)

@app.route("/submit")
def submit():
    return "submit page"
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
