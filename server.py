# server.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=jp&'
           'apiKey=74d7dc960a7f4b0f962a7f5a24516298')
    response = requests.get(url)
    news_dict_all = response.json()

    #text = news_dict["articles"][0]['title']
    news_title = []
    for news in news_dict_all["articles"]:
        news_title.append(news['title'])

    news_title_text = ""
    for news in news_dict_all["articles"]:
        news_title_text += news['title'] + '<br>'
    return str(news_title_text)



if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0',port=1300)