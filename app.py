from flask import Flask, render_template, request, redirect
import simplejson as json
import requests, datetime
import pandas as pd
from bokeh.plotting import output_file, show
from bokeh.charts import TimeSeries

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route("/index_post")
def index_post():
  year_prev_month = (datetime.datetime.now()-datetime.timedelta(days=31)).strftime('%Y-%m')
  
  stock_ticker = request.args.get('stock_ticker','')
  quandl='https://www.quandl.com/api/v3/datasets/WIKI/'+stock_ticker+'.json?column_index=4&start_date='+year_prev_month+'-01'
  r = requests.get(quandl + '?api_key=_AnN7yvqekPoP7s1yPJ4')
  data = json.loads(r.text)
  stock = pd.DataFrame(data['dataset']['data'],columns=['date','close_val'])

  output_file("timeseries.html")
  PlotData = dict(close_val=stock['close_val'],date=stock['date'].astype('datetime64'))
  p = TimeSeries(PlotData,index='date',title=stock_ticker,ylabel='Stock Closing Value')

  show(p)
  
  return render_template("timeseries.html")

if __name__ == '__main__':
  app.debug=True
  app.run(port=33507)
