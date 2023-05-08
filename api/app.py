from flask import Flask,jsonify
from flask_restful import Resource, Api
import pandas as pd
import pickle
import numpy as np # working with arrays
import pandas as pd
from flask import request
import requests
import utils.index as ut
import os

root = os.path.dirname(__file__)
print("root ",root)



app = Flask(__name__)
api = Api(app)


# Load models
algorithms, names = ut.load_models(root)

# Load scaler and label encoder
min_max_scaler, dict_encoder = ut.load_preprocess(root)


def predict(data,algo): 
    model = algorithms[algo]
    to_predict = np.array(data).reshape(1,len(data))
    result = model.predict(to_predict)
    print('::result::', result[0])
    return result[0]
    

def send_response(prediction,res):
    res['RESULTID']= "ProceedWithSuccess"                 
    res['ERRORCODE']= "00000"              
    res['ERRORDESC']= "PROCESSED_SUCCESSFULLY"
    res['IS_FRAUD']= bool(prediction)
    return res

class Get_Fraud_result(Resource):

    def get(self,algo):
        print("algooo",algo)
        response = {
            'KEYVALUES': "",               
            'RQUID': "",                     
            'RESULTID': "",                 
            'ERRORCODE': "",                  
            'ERRORDESC': ""            
            #'IS_FRAUD': False
        }  
       
        try:
            body = request.json
            transaction=pd.Series(body)
            transaction = ut.preprocess(transaction, min_max_scaler, dict_encoder)
            #print('::after preproccesing::', transaction)
            print('::::', len(transaction))

            prediction_result=predict(transaction,algo)
            response=send_response(prediction_result,response)
            return response
        
        except Exception as e:
            response['RESULTID']= "SystemError"                 
            response['ERRORCODE']= "00001"              
            response['ERRORDESC']= "SYSTEM_ERROR"
            return response
        
       
api.add_resource(Get_Fraud_result, '/test/<string:algo>')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")



# Setps to run project
# cd api 
# python3 -m venv venv
# source venv/bin/activate
# pip install flask ... 
# activate env: venv\scripts\activate
# run server:  py app.py




