import os, signal, math
from flask import Flask, render_template, flash, request
from buzz import generator
from tools import temp_conversion
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField

DEBUG = True
app = Flask(__name__)
app.secret_key = 'development key'

TEMP_UNITS = [('Kelvin', 'Kelvin'), ('Celsius', 'Celsius'), ('Fahrenheit', 'Fahrenheit'), ('Rankine', 'Rankine')]

class MyForm(Form):
    
    input_temp = TextField('Input Temperature', validators=[validators.required()])
    input_unit = SelectField('Input Unit', choices=TEMP_UNITS, validators=[validators.required()])
    target_unit = SelectField('Target Unit', choices=TEMP_UNITS, validators=[validators.required()])
    student_response = TextField('Student Response', validators=[validators.required()])


signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

def check_student_answer(input_temp, input_unit, target_unit, student_response):

    if input_unit == 'Celsius':
      if target_unit == 'Fahrenheit':
        converted_value=temp_conversion.celsius_to_fahrenheit(input_temp)
      elif target_unit == 'Kelvin':
        converted_value=temp_conversion.celsius_to_kelvin(input_temp)
      elif target_unit == 'Rankine':
        converted_value=temp_conversion.celsius_to_rankine(input_temp)
    elif input_unit == 'Fahrenheit':
      if target_unit == 'Celsius':
        converted_value=temp_conversion.fahrenheit_to_celsius(input_temp)
      elif target_unit == 'Kelvin':
        converted_value=temp_conversion.fahrenheit_to_kelvin(input_temp)
      elif target_unit == 'Rankine':
        converted_value=temp_conversion.fahrenheit_to_rankine(input_temp)
    elif input_unit == 'Kelvin':
      if target_unit == 'Celsius':
        converted_value=temp_conversion.kelvin_to_celsius(input_temp)
      elif target_unit == 'Fahrenheit':
        converted_value=temp_conversion.kelvin_to_fahrenheit(input_temp)
      elif target_unit == 'Rankine':
        converted_value=temp_conversion.kelvin_to_rankine(input_temp)
    elif input_unit == 'Rankine':
      if target_unit == 'Celsius':
        converted_value=temp_conversion.rankine_to_celsius(input_temp)
      elif target_unit == 'Fahrenheit':
        converted_value=temp_conversion.rankine_to_fahrenheit(input_temp)
      elif target_unit == 'Kelvin':
        converted_value=temp_conversion.rankine_to_kelvin(input_temp)
    else:
        converted_value=None

    return 'correct' if math.ceil(converted_value) == math.ceil(student_response) else ("incorrect. The correct answer is " + str(converted_value))

@app.route("/temp", methods=['GET', 'POST'])
def temp():
    form = MyForm(request.form)
    if request.method == 'POST':
        if form.validate():
            flash("The student response is " + check_student_answer(float(request.form['input_temp']), request.form['input_unit'], request.form['target_unit'], float(request.form['student_response'])))
        else:
            flash('All fields required.')

    return render_template('temp.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
