# 9. Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
#    и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
#    Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def base():
    context = {
        'title': 'Главная',
        'date_time': datetime.now().strftime('%A, %H:%M, %d.%m.%Y')
    }
    return render_template('base_task_9.html', **context)


@app.route('/clothes/')
def clothes():
    title = 'Одежда'
    goods = {
        'Рубашка мужская': 3000,
        'Блузка женская': 2000,
        'Футболка детская': 1000,
    }
    return render_template('clothes.html', title=title, goods=goods)


@app.route('/shoes/')
def shoes():
    title = 'Обувь'
    goods = {
        'Ботинки мужские': 9000,
        'Туфли женские': 11000,
        'Кроссовки детские': 4000,
    }
    return render_template('shoes.html', title=title, goods=goods)


@app.route('/jackets/')
def jackets():
    title = 'Куртки'
    goods = {
        'Куртка мужская': 20000,
        'Плащ женский': 25000,
        'Пуховик детский': 15000,
    }
    return render_template('jackets.html', title=title, goods=goods)


if __name__ == '__main__':
    app.run(debug=True)
