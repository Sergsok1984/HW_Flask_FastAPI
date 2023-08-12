# 6. Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
#    При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на
#    страницу с ошибкой в случае некорректного возраста.

from flask import Flask, request, render_template, abort

app = Flask(__name__)


@app.errorhandler(403)
@app.route('/age/', methods=['GET', 'POST'])
def get_age():
    if request.method == 'POST':
        username = request.form.get('name')
        age = int(request.form.get('age'))
        if age < 18:
            return abort(403)
        return f'Имя: {username}, Возраст: {age}'
    return render_template('task6.html')


@app.errorhandler(403)
def forbidden(e):
    print(e)
    return render_template('403.html'), 403


if __name__ == '__main__':
    app.run(debug=True)
