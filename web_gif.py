from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)

def gif_search_function(search_term):
    g = giphypop.Giphy()
    results = g.search(search_term) #insert search term
    return results

@app.route('/')
def index():  #must be right underneath
    return render_template('index.html')

@app.route('/about')
def about():  #must be right underneath
    return render_template('about.html')

@app.route('/results')
def results():
    gif_search = request.values.get('gif_search')
    gif_list = gif_search_function(gif_search)
    return render_template('results.html', gif_search=gif_search, gif_list=gif_list) #, gifs=gifs)


app.run(debug=True)