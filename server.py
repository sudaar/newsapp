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
    newses = []
    for news_dict in news_dict_all['articles']:
        news = dict()
        news['title'] = news_dict['title']
        news['url'] = news_dict['url']
        newses.append(news)
    return render_template('index.html', newses=newses)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=1300)

