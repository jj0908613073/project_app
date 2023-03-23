# -*- coding: UTF-8 -*-
import numpy as np
#import model
from flask import render_template
from flask import Flask, request, jsonify
from flask_cors import CORS

from app.model import predict
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/model')
def model():
    return render_template("model.html")

@app.route('/calculate',methods=['POST'])
def calculate():
    text1 = request.form.get('text1')
    text2 = request.form.get('text2')
    texts = text1 + text2

    result = predict(str(text1),str(text2))
    print(request.form.get('text1'))
    print(request.form.get('text2'))
    print(result)
    return render_template("model.html", result = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',  port=80, debug=False)