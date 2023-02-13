from flask import Flask,jsonify
from flask_restful import Resource, Api
import pandas as pd
import joblib
import pickle
import numpy as np # working with arrays
import pandas as pd



app = Flask(__name__)
api = Api(app)


#http://127.0.0.1:5000/test/data1

tree_model = pickle.load(open("models/D_Tree.pkl","rb"))
rf_model = pickle.load(open("models/R_forest.pkl","rb"))


def pred(data,algo):
    test=[139,265803.35,0.00,0.00,751669.39,1017472.74, 0 , 1,0,0,0 ,0 ]
    test1=[319,1033878.67,1033878.67,0.0,0.0,0.0,0,0,0,0,1,0]
    to_predict = np.array(test1).reshape(1,12)

    result=[]
    if(algo=="DT"):
        result = tree_model.predict(to_predict)
    elif(algo=="RF"):
        result = rf_model.predict(to_predict)
    
    print(" TEST ",result[0])

    return result[0]
    
  
class Search(Resource):

    def get(self, data,algo):
        print(algo)
        res=pred(data,algo)

        if res==1:
            return jsonify(
                {
                    'result':True,
                    'msg':"Yes, A fraud is detected !!"
                }
            )
        else:
          return jsonify(
                {
                    'result':False,
                    'msg':"NO fraud detected !!"
                }
            )



api.add_resource(Search, '/test/<string:data>/<string:algo>')


if __name__ == '__main__':
    app.run(debug=True)







# Setps to run project
# cd api 
# python3 -m venv venv
# source venv/bin/activate
# pip install flask ... 
# activate env: venv\scripts\activate
# run server:  py app.py




