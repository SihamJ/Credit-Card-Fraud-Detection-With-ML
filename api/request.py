import requests
import time
import json
import sys
import pickle
import pandas as pd
from utils import *

if(len(sys.argv) < 2 ):
    print("\nUsage: python request.py [SVM|CNN|RF]+\n")
    exit(1)

algos = sys.argv[1:]

## PYTHON API
# Load scaler and encoder
root = "/home/sihartist/Desktop/"
encoder_path = "fraud-detection/preprocessing/dict_all.obj"
# scalerfile = 'fraud-detection/preprocessing/scaler.sav'

# loading scaler
# min_max_scaler = pickle.load(open(root + scalerfile, 'rb'))

# loading encoder dictionary
# file = open(root + encoder_path,'rb')
# dict_encoder = pickle.load(file)
# file.close()


# Raw data for test (don't forget to set preprocess to True)
raw_data = pd.read_json("/home/sihartist/Desktop/fraud-detection/dataset/clean_row.json",orient='index', dtype=str)
raw_data = raw_data.drop('CLASS')
dict_data = raw_data.to_dict()
raw_json_data = json.dumps(dict_data, indent=4)

# Preprocessed Data for test
# preprocessed_data = pickle.load(open("/home/sihartist/Desktop/fraud-detection/dataset/new_row.obj", "rb"))
# preprocessed_data = dict(preprocessed_data)
# preprocessed_json_data = json.dumps(preprocessed_data, indent=4)


# test with preprocessing
# t = time.time()
# response = requests.post('http://127.0.0.1:5000/predict', json={"algo": algo, "transaction": raw_json_data, "preprocess":True})
# t = time.time() - t
# print("\nPython time (with preprocessing): " + str(round(t,2)) + " s")

# message = json.loads(response.content.decode('utf-8'))
# print(message)


# test without preprocessing
# t = time.time()
# response = requests.post('http://127.0.0.1:5000/predict', json={"algo": algo, "transaction": preprocessed_json_data, "preprocess":False})
# t = time.time() - t
# print("\nPython time (without preprocessing): " + str(round(t,2)) + " s")

# message = json.loads(response.content.decode('utf-8'))
# print(message)



# JAVA API

print("\n")
for i in range(len(algos)):

    t = time.time()
    response = requests.post('http://127.0.0.1:8080/predict', json={ "algo": algos[i], "transaction": dict_data[0] })

    message = json.loads(response.content.decode('utf-8'))
    print(message)

    t = time.time() - t
    print("JAVA time: " + str(round(t,2)) + " s\n")

