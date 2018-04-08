# server.py
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=jp&'
           'apiKey=74d7dc960a7f4b0f962a7f5a24516298')
    response = requests.get(url)
    news_dict_all = response.json()

    news_titles = []
    for news in news_dict_all["articles"]:
        news_titles.append(news['title'])

    return render_template('index.html', news_titles=news_titles)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=1300)
