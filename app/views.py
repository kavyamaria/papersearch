# views.py

from flask import render_template,request
from ranking import *
import sys

from app import app


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/results/", methods=['POST'])
def display_results():
    #Moving forward code
    original = request.form['query']
    query2 = original.replace(" ", "+")
    topic = request.form['topic']
    results=getScores(query2,topic)
    return render_template('results.html', query=query2,results=results, original=original)
