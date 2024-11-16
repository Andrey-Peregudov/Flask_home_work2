from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from wtforms import FloatField, SubmitField
from flask import request

class Calc(FlaskForm):
    numbers1 = FloatField('Число 1', validators=[DataRequired()])
    numbers2 = FloatField('Число 2', validators=[DataRequired()])
    submit = SubmitField('Ответ')
class Answer(Calc):
    def answer(self):
        x = self.numbers1
        n = self.numbers2
        c = request.form(x) + request.form(n)
        return c