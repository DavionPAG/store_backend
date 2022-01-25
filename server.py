from flask import Flask, request, abort
from data import catalog
import json
import random
from config import db
from flask_cors import CORS

app = Flask('Main')
CORS(app)

me = {
    'name': 'Davion',
    'last': 'Garcia',
    'age': 24,
    'address': {
        'street': 'Jump',
        'number': 24,
        'city': 'Merca'
    }
}


@app.route('/')
def home():
    return 'Yo!'


@app.route('/test')
def test():
    return 'Test'


@app.route('/about')
def about():
    return me['name'] + ' ' + me['last']


@app.route('/api/catalog')
def get_catalog():

    test = db.products.find({})
    print(test)

    return json.dumps(catalog)


@app.route('/api/catalog', methods=['post'])
def save_prod():
    prod = request.get_json()

    if not 'title' in prod or len(prod['title']) < 5:
        return abort(400, '"Title" required, and must be a least 5 chars')

    if not 'price' in prod or prod['price'] < 0:
        return abort(400, '"Price" required, and must be > 0')

    prod['_id'] = random.randint(1000, 100000)
    catalog.append(prod)

    return 'ok'


@app.route('/api/cheapest')
def get_cheapest():
    cheap = catalog[0]
    for prod in catalog:
        if prod['price'] < cheap['price']:
            cheap = prod
    return json.dumps(cheap)


@app.route('/api/product/<id>')
def get_id(id):
    for prod in catalog:
        if prod['_id'] == id:
            return prod


@app.route('/api/catalog/<cat>')
def get_by_cat(cat):
    filtered_list = []
    for prod in catalog:
        if prod['category'].lower() == cat.lower():
            filtered_list.append(prod)
    return json.dumps(filtered_list)


@app.route('/api/catalog/categories')
def get_cat():
    filtered_list = []
    for prod in catalog:
        if prod['category'] not in filtered_list:
            filtered_list.append(prod['category'])
    return json.dumps(filtered_list)


@app.route('/api/reports/prodCount')
def get_count():
    return json.dumps(len(catalog))


@app.route('/api/reports/total')
def get_total():
    total = 0
    for prod in catalog:
        total += prod["price"]*prod['stock']
    return json.dumps(total)


@app.route('/api/reports/highExpense')
def get_high_expense():
    high_expense = catalog[0]
    for prod in catalog:
        total = prod['price'] * prod['stock']
        highest = high_expense['price'] * high_expense['stock']
        if total > highest:
            high_expense = prod
    return json.dumps(high_expense)


app.run(debug=True)
