from flask import Flask, jsonify, request
from flask_restful import Api
import pickle
import numpy as np # working with arrays
import pandas as pd
from utils import *

# Load models
algorithms, names = load_models()


## API
app = Flask(__name__)
api = Api(app)


"""
POST Json example:

raw:
{"algo": "RF", "transaction": [31, 281, 22, 010112, 500, 01/05/2009, 01/05/2011, 02/07/2009 21:21:42, 010112, 6011, 21140121124C, 6, 071181, 0,
 01000002, 01000002, 26/12/2009, 952, 384, VERSUS BANK 2 PLATEAUX REGION LAGUNECI ]}

clean:
{"algo": "RF", "transaction": [4,	2,	23,	1,	285328,	33443,	19,	2976,	44,	20238,	3,	1,	573908,	1,	384,	4,	-0.52504918247254,	-0.93775213214708,	
0.20129852008866,	0.980307111357288,	0.20129852008866,	0.980307111357288,	-0.52504918247254,	-0.93775213214708,	2009,	2009,	2009,	2009]}


"""

def preprocess(row):



@app.route("/predict",  methods = ['POST'])
def pred():

    try:
        content = request.get_json()
    except:
        return jsonify(
            {
                'isFraud' : -1,
                'message' : 'Failed to load Json. Please make sure the format is correct.'
            }
        )

    try:
        model = algorithms[content['algo']]
    except:
        return jsonify(
            {
                'isFraud' : -1,
                'message' : 'Model ' + content['algo'] + 'unavailable. Please choose one of the following: ' + algorithms.keys()
            }
        )

    try:
        transaction = content['transaction']
    except:
        return jsonify(
            {
                'isFraud' : -1,
                'message' : 'Please provide transaction data.'
            }
        )
    
    try:
        to_predict = np.array(transaction).reshape(1,27)
        res = model.predict(to_predict)
    except:
        return jsonify(
            {
                'isFraud' : -1,
                'message' : 'Failed to predict result, please make sure the data is in the correct format (Float array, length of 27).'
            }
        )
    
    return jsonify(
        {
            'isFraud': int(res),
            'message':"Predicted with " + names[content['algo']]
        }
    )


if __name__ == '__main__':    
    app.run(debug=True)







# Setps to run project
# cd api 
# python3 -m venv venv
# source venv/bin/activate
# pip install flask ... 
# activate env: venv\scripts\activate
# run server:  py app.py




