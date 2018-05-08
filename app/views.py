# views.py

from flask import render_template,request
from ranking import *
import sys

from app import app

# function that renders the landing page
@app.route("/")
def index():
    return render_template('index.html')

# function that takes user input, gets the top ten corresponding articles,
# and displays them to the user
@app.route("/results/", methods=['POST'])
def display_results():
    #Moving forward code
    original = request.form['query']
    query2 = original.replace(" ", "+")
    topic = request.form['topic']
    results=getScores(query2,topic)
    return render_template('results.html', query=query2,results=results, original=original)
