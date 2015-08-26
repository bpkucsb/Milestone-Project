from flask import Flask, render_template, request, redirect
import simplejson as json
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route("/index_post")
def index_post():
  stock_ticker = request.args.get('stock_ticker','')
  quandl='https://www.quandl.com/api/v3/datasets/WIKI/'+stock_ticker+'.json'
  r = requests.get(quandl + '?api_key=_AnN7yvqekPoP7s1yPJ4')
  data = json.loads(r.text)
  stock = pd.DataFrame[data['dataset']['data']]
  table = pd.concat([stock[stock[0]>'2015-08-01'][0],stock[stock[0]>'2015-08-01'][4]],axis=1)
  return stock_ticker

if __name__ == '__main__':
  app.debug=True
  app.run(port=33507)
