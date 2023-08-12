# 8. Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
#    При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением,
#    где будет выведено "Привет, {имя}!".

from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = b'8bd34648247e5880cdda559c0e18c99bf1ef90582cb3e5beeafb3b760f0917d5'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('form'))
    return render_template('task8.html')


if __name__ == '__main__':
    app.run(debug=True)
