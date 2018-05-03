# views.py

from flask import render_template,request
from runquery import search,searchsig
import sys

from app import app


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    query2 = request.form['query'].replace(" ", "+")
    topic = request.form['topic']
    val2=searchsig(query2,topic)
    for k in val2.keys():
         query2 = k
         break

    return render_template('results.html', query=query2);
#
