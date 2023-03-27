import pickle
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import math

def load_models():

    root = "/home/sihartist/Desktop/"
    
    svm = "fraud-detection/models/svm.pkl"
    rf = "fraud-detection/models/R_forest.pkl"
    cnn = "fraud-detection/models/cnn.h5"

    SVM = pickle.load(open(root + svm,"rb"))
    RF = pickle.load(open(root + rf,"rb"))
    CNN = tf.keras.models.load_model(root + cnn)

    algorithms = {'SVM':SVM, 'CNN':CNN, 'RF':RF}
    names = {'SVM':'Support Vector Machine', 'CNN':'Convolutional Neural Network', 'RF':'Random Forest'}

    return algorithms, names


"""
Row should be a dictionary
"""
def preprocess(row):

    root = "/home/sihartist/Desktop/"
    
    encoder_path = "fraud-detection/preprocessing/dict_all.obj"
    scalerfile = 'fraud-detection/preprocessing/scaler.sav'

    # loading scaler
    min_max_scaler = pickle.load(open(root + scalerfile, 'rb'))

    # loading encoder dictionary
    file = open(root + encoder_path,'rb')
    dict_encoder = pickle.load(file)
    file.close()

    # treating nan values
    row.drop(['V11','V14','V20','V5','V17','V18','V15', 'CLASS'], inplace=True)

    # updating types
    row['V10'] = float(row['V10'])
    row['V9'] = float(row['V9'])
    row['V24'] = float(row['V24'])

    row['V23'] = pd.to_datetime(row['V23'],format="%d/%m/%Y")
    row['V8'] = pd.to_datetime(row['V8'],format="%d/%m/%Y %H:%M:%S")

    row['V6'] = pd.to_datetime(row['V6'],format="%d/%m/%Y")
    row['V7'] = pd.to_datetime(row['V7'],format="%d/%m/%Y")

    # preprocess dates
    date_cols = ['V6','V7','V23','V8']
    years = {}
    date_rows = {}

    for l in date_cols:
        date_rows[l+'_month'] = row[l].month
        date_rows[l+'_day'] = row[l].day
        years[l+'_year'] = row[l].year
        row.pop(l)

    cos_cols = list(date_rows.keys())
    sin_cols = list(date_rows.keys())


    for i in range(len(cos_cols)):
        cos_cols[i] = 'COS(' + cos_cols[i] + ')'
        sin_cols[i] = 'SIN(' + sin_cols[i] + ')'

    # Normalize date cols
    date_row_scaled = min_max_scaler.transform(np.array(list(date_rows.values())).reshape(-1,8))
    date_row_scaled = date_row_scaled.reshape(8)

    cos_row_scaled = dict(zip(cos_cols, date_row_scaled))
    sin_row_scaled = dict(zip(sin_cols, date_row_scaled))

    date_row_cos = pd.Series(cos_row_scaled)
    date_row_sin = pd.Series(sin_row_scaled)
    date_row_cos = date_row_cos.apply(lambda x: math.cos(x))
    date_row_sin = date_row_sin.apply(lambda x: math.sin(x))

    year_row = pd.Series(years)

    new_row = pd.concat([row, date_row_cos, date_row_sin, year_row], axis=0)

    # encoding
    for col in dict_encoder.keys():
        if(new_row[col] in dict_encoder[col].keys()):
            new_row.replace(dict_encoder[col], inplace=True)
        else:
            new_row[col] = -1

    return new_row