from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    api_key = '9e4eb3c8c89839f8f51d1467'

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}'

    response = requests.get(url)
    data = response.json()

    converted_amount = data['conversion_result']

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}'

    response = requests.get(url)
    data = response.json()

    rate = data['conversion_rate']

    return render_template('result1.html', amount=amount, from_currency=from_currency, to_currency=to_currency, converted_amount=converted_amount, rate=rate)

@app.route('/list', methods=['POST'])
def list():
    currency = request.form['currency']

    api_key = '9e4eb3c8c89839f8f51d1467'

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}'

    response = requests.get(url)
    data = response.json()

    rates = data['conversion_rates']
    return render_template('result2.html', currency=currency, rates=rates)

if __name__ == '__main__':
    app.run(debug=True)