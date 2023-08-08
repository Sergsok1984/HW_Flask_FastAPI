# 7. Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
#    Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
#    Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask
from flask import render_template

app = Flask(__name__)

news = [
        {
            'title': 'Первая новость',
            'description': 'Сегодня холодно',
            'date': '2022-01-01'
        },
        {
            'title': 'Вторая новость',
            'description': 'Сегодня идет снег',
            'date': '2022-01-02'
        },
        {
            'title': 'Третья новость',
            'description': 'Сегодня морозное утро',
            'date': '2022-01-03'
        }]


@app.route('/news/')
def get_news():
    return render_template('task_7.html', news_list=news)


if __name__ == '__main__':
    app.run(debug=True)
