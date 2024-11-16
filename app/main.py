import os
from flask import Flask, render_template, request, flash

from app.forms import Answer
from forms import Calc

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = "SECRET_KEY"


@app.route('/', methods=['GET', 'POST'])
def calculator():
    numbers = Calc()
    calc = Answer.answer
    asw = calc
    x1 = request.form.get('numbers1')
    x2 = request.form.get('numbers2')
    x1 = float(x1)
    x2 = float(x2)
    print(x1+x2)
    flash(f'Ответ: {x1+x2}', 'success')
    return render_template('index.html', numbers1=numbers, answer=asw)


if __name__=="__main__":
    app.run(debug=True)
