# 3. Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/sum/<int:num_a>+<int:num_b>/')
def get_sum(num_a, num_b):
    return f'{num_a} + {num_b} = {num_a + num_b}'


if __name__ == '__main__':
    app.run(debug=True)
