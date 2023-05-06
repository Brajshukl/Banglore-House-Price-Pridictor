from flask import Flask, render_template, request
import pandas as pd
import sklearn
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True, port=5001)