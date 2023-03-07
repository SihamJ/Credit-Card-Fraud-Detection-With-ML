import pickle
import tensorflow as tf

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