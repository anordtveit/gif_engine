from flask import Flask, render_template, request
from googlefinance import getQuotes
app = Flask(__name__)

def get_stock_price(ticker):
    quotes = getQuotes(ticker)
    price = quotes[0]['LastTradePrice']
    return "the price of {} is {}".format(ticker, price)

@app.route('/')
def index():  #must be right underneath
    name = request.values.get('name', 'Nobody')
    greeting = "Hello {}".format(name)
    return render_template('index.html', greeting = greeting)

@app.route('/about')
def about():  #must be right underneath
    return render_template('about.html')

@app.route('/results')
def results():
    stock = request.values.get('stock')
    price = get_stock_price(stock)
    gifs =["one", "two", "three"]
    return render_template('results.html', price=price, gifs=gifs)



# @app.route('/<username>')
# def profile():  #must be right underneath
#     user = get_suer(username)
#     return render_template('profile.html')

app.run(debug=True)