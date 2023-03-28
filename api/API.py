from flask import Flask, jsonify, request
from flask_restful import Api
import pickle
import numpy as np # working with arrays
import pandas as pd
from utils import *

# Load models
algorithms, names = load_models()

# Load scaler and encoder
root = "/home/sihartist/Desktop/"
encoder_path = "fraud-detection/preprocessing/dict_all.obj"
scalerfile = 'fraud-detection/preprocessing/scaler.sav'

# loading scaler
min_max_scaler = pickle.load(open(root + scalerfile, 'rb'))

# loading encoder dictionary
file = open(root + encoder_path,'rb')
dict_encoder = pickle.load(file)
file.close()


## API
app = Flask(__name__)
api = Api(app)


"""
POST Json example:



"""
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
        transaction = json.loads(content['transaction'])
        transaction = pd.Series(dict(transaction))
    except:
        return jsonify(
            {
                'isFraud' : -1,
                'message' : 'Please provide transaction data.'
            }
        )
        
    try:
        prep = content['preprocess']
        if(prep):
            transaction = preprocess(transaction, min_max_scaler, dict_encoder)
    except:
        return jsonify(
            {
                'isFraud' : -1,
                'message' : 'Failed to preprocess data. Please verify data format is correct.'
            }
        )
    try:
        res = model.predict(transaction)
    except:
        return jsonify(
            {
                'isFraud' : -1,
                'message' : 'Failed to predict result, please make sure the data is in the correct format.'
            }
        )
    
    return jsonify(
        {
            'isFraud': int(res[0]),
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




