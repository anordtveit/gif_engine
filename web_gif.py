# This is the masterfile for the gif seach engine
# Import librarys below
from flask import Flask, render_template, request
import giphypop
import os

# Initiate the flask app
app = Flask(__name__)

# define a function that searches the Giphypop API with the giphypop library
def gif_search_function(search_term):
    g = giphypop.Giphy() # Giphypop API
    results = g.search(search_term) #returns a list of with data including href 
    return results

# Index represents the home-page
@app.route('/')
def index(): 
    return render_template('index.html') #points to the index.html web-page.

# The about web-page contains information about the authors of the page
@app.route('/about')
def about():  
    return render_template('about.html') #points to the about.html web-page.

# The result-page returns results of the search to the user.
@app.route('/results')
def results():
    gif_search = request.values.get('gif_search') #Reads and assigns the content of the form to the gif_search variable
        # Custom made error catching, couldn't quite get the error-catching to work. Checks if the gif_search term is empty
        # If the gif_search term is empty it sends and empty list to the result-page, else it conducts the gif-search with the gif_seach_function above
    if gif_search == "":
        gif_list = []
    else:
        gif_list = gif_search_function(gif_search)
        
    return render_template('results.html', gif_search=gif_search, gif_list=gif_list) #points to the result web-page and send requested information to this page so that it is customized

# app.run(debug=True)
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)