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

{"algo": "RF", "transaction": [139, 265803.35, 0.00, 0.00, 751669.39, 1017472.74, 0, 1, 0, 0, 0, 0 ]}

"""
@app.route("/data",  methods = ['POST'])
def pred():

    try:
        content = request.get_json()
    except:
        return jsonify(
            {
                'result' : -1,
                'message' : 'Failed to load Json. Please make sure the format is correct.'
            }
        )

    try:
        model = algorithms[content['algo']]
    except:
        return jsonify(
            {
                'result' : -1,
                'message' : 'Model ' + content['algo'] + 'unavailable. Please choose one of the following: ' + algorithms.keys()
            }
        )

    try:
        transaction = content['transaction']
    except:
        return jsonify(
            {
                'result' : -1,
                'message' : 'Please provide transaction data.'
            }
        )
    
    try:
        to_predict = np.array(transaction).reshape(1,12)
        res = model.predict(to_predict)
    except:
        return jsonify(
            {
                'result' : -1,
                'message' : 'Failed to predict result, please make sure the data is in the correct format (Float array, length of 12).'
            }
        )
    
    return jsonify(
        {
            'result': int(res),
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




