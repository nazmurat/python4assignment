from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests as requests
from forms import CheckForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:9666@localhost:5432/postgres2'
db = SQLAlchemy(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crypto_name = db.Column(db.String(20), nullable=False)
    header = db.Column(db.Text, nullable=False)
    paragraph = db.Column(db.Text, nullable=False)

    def __init__(self, crypto_name, header, paragraph):
        self.crypto_name = crypto_name
        self.header = header
        self.paragraph = paragraph


class Coin:
    def __init__(self, sum1):
        self.sum1 = sum1

    def get_res(self, coin_name):
        for i in range(len(coin_name)):
            if coin_name[i] == ' ' or coin_name[i] == '.':
             coin_name = coin_name.replace(' ', '-')

        result_list = []
        tc = self.sum1
        while True:
            url_api = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit={tc}&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false'
            responce = requests.get(url=url_api)
            data = responce.json()
            for i in range(0, tc):
                result_list.append({
                    'id': data['data']['cryptoCurrencyList'][i]['id'],
                    'name': data['data']['cryptoCurrencyList'][i]['name'],

                })
            print(result_list)
            for i in range(0, tc):
                if 'name' == 'Bitcoin' in result_list:
                    print(result_list.get('id'))
            coin_id = 0
            for i in range(len(result_list)):
                if result_list[i]['name'] == coin_name.lower().title():
                    coin_id = result_list[i]['id']
            urls = f'https://api.coinmarketcap.com/content/v3/news?coins={coin_id}'
            res = requests.get(url=urls)
            data_news = res.json()
            data_news_json = []
            for i in range(0, len(data_news['data'])):
                data_news_json.append({
                    'News title': data_news['data'][i]['meta']['title'],
                    'Text': data_news['data'][i]['meta']['subtitle']
                })
            return data_news_json


@app.route('/')
@app.route('/coin', methods=['GET', 'POST'])
def coin():
    form = CheckForm()

    head = []
    para = []

    if form.validate_on_submit():
        cryptoName = (str(form.crypto_name.data)).lower()
        coin = Coin(10)
        res = coin.get_res(cryptoName)

        exists = check(cryptoName)

        for i in range(0, len(res) - 1):
            head.append(res[i]['News title'])
            para.append(res[i]['Text'])

            if not exists:
                new_article = Articles(f'{cryptoName}', f'{head[i]}', f'{para[i]}')
                db.session.add(new_article)
                db.session.commit()

    return render_template('coin.html', form=form, head=head, para=para)


def check(cryptoName):
    for row in db.session.query(Articles).filter_by(crypto_name=cryptoName):
        if row.crypto_name == cryptoName:
            return True
    return False


if __name__ == '__main__':
    app.run(debug=True)
