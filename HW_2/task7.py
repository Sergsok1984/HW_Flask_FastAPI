# 7. Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
#    При нажатии на кнопку будет произведено перенаправление на страницу с результатом,
#    где будет выведено введенное число и его квадрат.

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        result = number ** 2
        return redirect(url_for('calc_square', result=result, number=number))
    return render_template('task7.html')


@app.route('/calc_square/')
def calc_square():
    num = request.args.get('number')
    res = request.args.get('result')
    return f'Квадрат числа {num} равен: {res}'


if __name__ == '__main__':
    app.run(debug=True)
