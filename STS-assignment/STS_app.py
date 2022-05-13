#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from flask import Flask, request, render_template
import pickle


# In[ ]:


app = Flask(__name__) #instantiate the flask app

model = pickle.load(open('C:\My data\STS-assignment\STS_Model.pkl','rb')) #load the ML model which is ready with us for deployment

@app.route('/') # route to home page.Home directiory is given by '/'
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    distance = model.wmdistance(text1.lower(), text2.lower())
    output = round(distance,2)
    return render_template('index.html',prediction_text = "Semantic Score $ {}".format(output))

if __name__ == '__main__':
    app.run(debug = True)

