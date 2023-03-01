from flask import Flask,jsonify
from flask_restful import Resource, Api
import pandas as pd
import joblib
import pickle
import numpy as np # working with arrays
import pandas as pd

global filename
global algo

root = "/home/sihartist/Desktop/"
svm = "fraud-detection/algo/models/svm.pkl"
rf = "fraud-detection/api/model.pkl"
cnn = "fraud-detection/algo/models/cnn.pkl"

filename = root + cnn
algo = 'CNN'

app = Flask(__name__)
api = Api(app)


#http://127.0.0.1:5000/test/data1


def choose_algo(name):
    global filename
    global algo
    algo = name
    if name == 'CNN':
        filename = root + cnn
    elif name =='Random Forest':
        filename = root + rf
    elif name=='SVM':
        filename = root + svm
    else:
        filename = root + rf
        algo = 'Random Forest'


loaded_model = pickle.load(open(filename,"rb"))

def pred(data):
    test=[139,265803.35,0.00,0.00,751669.39,1017472.74, 0 , 1,0,0,0 ,0 ]
    test1=[319,1033878.67,1033878.67,0.0,0.0,0.0,0,0,0,0,1,0]
    to_predict = np.array(test).reshape(1,12)

    result = loaded_model.predict(to_predict)
    print(" TEST ",result[0])

    return result[0]
    
  
class Search(Resource):

    def get(self, data):
        res=pred(data)

        if res==1:
            return jsonify(
                {
                    'result':True,
                    'msg':"Yes, A fraud is detected !!",
                    'algo': algo
                }
            )
        else:
          return jsonify(
                {
                    'result':False,
                    'msg':"NO fraud detected !!",
                    'algo': algo
                }
            )



api.add_resource(Search, '/test/<string:data>')


if __name__ == '__main__':
    # 'CNN' , 'RF', 'SVM'
    choose_algo('RF')
    app.run(debug=True)







# Setps to run project
# cd api 
# python3 -m venv venv
# source venv/bin/activate
# pip install flask ... 
# activate env: venv\scripts\activate
# run server:  py app.py




