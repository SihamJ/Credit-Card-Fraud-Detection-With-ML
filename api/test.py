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

def pred(data):
    test=[139,265803.35,0.00,0.00,751669.39,1017472.74, 0 , 1,0,0,0 ,0 ]
    test1=[319,1033878.67,1033878.67,0.0,0.0,0.0,0,0,0,0,1,0]
    to_predict = np.array(test1).reshape(1,12)

    loaded_model = pickle.load(open("model.pkl","rb"))
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



api.add_resource(Search, '/test/<string:data>')






if __name__ == '__main__':
    app.run(debug=True)








