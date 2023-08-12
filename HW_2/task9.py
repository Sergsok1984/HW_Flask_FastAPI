# 9. Создать страницу, на которой будет форма для ввода имени и электронной почты,
#    при отправке которой будет создан cookie файл с данными пользователя.
#    Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
#    На странице приветствия должна быть кнопка "Выйти".
#    При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу
#    ввода имени и электронной почты.

from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = make_response(redirect('/welcome'))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return response
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')
    if name:
        return render_template('welcome.html', name=name)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
