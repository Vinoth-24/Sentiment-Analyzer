# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import re
import numpy as np
from functions import *
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

def processing(review):
    final_review = normalize_and_lemmaize(review) # Cleaned text to predict
    tfidf = transformer.fit_transform(loaded_vec.fit_transform(np.array([final_review]))) # Converting to vectors
    return tfidf

def prediction(processed):
    pred=loaded_model.predict(processed) 
    return pred
    
# load log model
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb')) # Log model

#Load tf-idf model
transformer = TfidfTransformer()
loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("feature.pkl", "rb")))


app_log = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        processed = processing(data)
        my_prediction = prediction(processed)
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
