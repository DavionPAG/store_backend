from flask import Flask
from data import catalog
import json



app = Flask('Main')

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
  return json.dumps(catalog)


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

app.run(debug=True)