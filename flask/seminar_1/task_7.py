# Задание №7
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from datetime import datetime
from flask import render_template
from task_6 import app


@app.route('/news/')
def news():
    news_block = [
        {
            'title': 'Новость первая',
            'description': 'В г. Троицк Челябинской области прибыл известный актёр Сергей Безруков.',
            'date_time': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
        },
        {
            'title': 'Новость вторая',
            'description': 'Аномальные дожди!',
            'date_time': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
        },
        {
            'title': 'Новость тетья',
            'description': 'На фоне пандемии в 2020 году...',
            'date_time': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
        }
    ]

    return render_template('news.html', news_block=news_block)


if __name__ == '__main__':
    app.run()
