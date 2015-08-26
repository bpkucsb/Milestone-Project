from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route("/index_post")
def index_post():
  return "echo:" + request.args.get('stock_ticker','')

if __name__ == '__main__':
  app.debug=True
  app.run(port=33507)
