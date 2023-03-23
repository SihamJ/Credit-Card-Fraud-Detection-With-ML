from flask import Flask,jsonify
from flask_restful import Resource, Api
import pandas as pd
import pickle
import numpy as np # working with arrays
import pandas as pd
from flask import request


app = Flask(__name__)
api = Api(app)


#http://127.0.0.1:5000/test/data1
#test=[139,265803.35,0.00,0.00,751669.39,1017472.74, 0 , 1,0,0,0 ,0 ]
#test1=[319,1033878.67,1033878.67,0.0,0.0,0.0,0,0,0,0,1,0]


tree_model = pickle.load(open("models/D_Tree.pkl","rb"))
rf_model = pickle.load(open("models/R_forest.pkl","rb"))


def pred(data,algo):
    test_data=[  4,  2,  23,  1,  410878,  715848.0,  19,  2976,  44,  20339,  3,  1,  621524,  1,  
                384,  4,  0.654861,  0.654861, -1.0, -0.5,  0.959493, -0.978148,  2009,  2011,  2009,  2009 
           ]
    to_predict = np.array(test_data).reshape(1,26)

    result = rf_model.predict(to_predict)
    print(" TEST ",result[0])
    
    return result[0]
    

class Search(Resource):

    def get(self, data,algo):
        data = request.json 
        print("hi",data)
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
    app.run(host="0.0.0.0")



# Setps to run project
# cd api 
# python3 -m venv venv
# source venv/bin/activate
# pip install flask ... 
# activate env: venv\scripts\activate
# run server:  py app.py




