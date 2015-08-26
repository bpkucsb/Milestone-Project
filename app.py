from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/index', methods=['POST'])
def index_post():

  text = request.form['text']
  return text

if __name__ == '__main__':
  app.debug=True
  app.run(port=33507)
