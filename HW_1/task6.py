# 6. Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
#    Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
#    Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/students/')
def get_table():
    students = [{'firstname': 'Андрей', 'lastname': 'Петров', 'age': 20, 'rate': 3},
                {'firstname': 'Михаил', 'lastname': 'Сидоров', 'age': 30, 'rate': 4},
                {'firstname': 'Николай', 'lastname': 'Иванов', 'age': 40, 'rate': 5}
                ]

    return render_template('task_6.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
