from flask import Flask, render_template, request, redirect
import simplejson as json
import requests, datetime
import pandas as pd
from bokeh.plotting import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html, components
from bokeh.charts import TimeSeries
from bokeh import embed

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route("/plot")
def plot():
  year_prev_month = (datetime.datetime.now()-datetime.timedelta(days=31)).strftime('%Y-%m')
  
  stock_ticker = request.args.get('stock_ticker','')

  columns = map(str,request.args.getlist('column'))
  
  quandl='https://www.quandl.com/api/v3/datasets/WIKI/'+stock_ticker+'.json?start_date='+year_prev_month+'-01'
  r = requests.get(quandl + '?api_key=_AnN7yvqekPoP7s1yPJ4')
  data = json.loads(r.text)
  stock = pd.DataFrame(data['dataset']['data'],columns=map(str,data['dataset']['column_names']))
  stock['Date']=stock['Date'].astype('datetime64')
  columns.append('Date')
  
  #output_file("timeseries.html")

  p = TimeSeries(stock[columns],index='Date',title=stock_ticker,ylabel='value',legend=True)

  script, div = embed.components(p,CDN)

  #head = """ <link rel="stylesheet" href="http://cdn.pydata.org/bokeh/release/bokeh-0.9.0.min.css" type="text/css" /> <script type="text/javascript" src="http://cdn.pydata.org/bokeh/release/bokeh-0.9.0.min.js"> </script> <script type="text/javascript"> Bokeh.set_log_level("info"); </script> """

  #show(p)

  #  return head, script, div
  
  return render_template("timeseries.html",script=script,div=div)

if __name__ == '__main__':
  app.debug=True
  app.run(port=33507)
