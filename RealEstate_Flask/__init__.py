"""
The flask application package.
"""

#import numpy as np
from flask import Flask
#import pickle
app = Flask(__name__)

'''@app.route('/submit',methods=['POST'])

def predict():
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2) 
    return render_template('displand.html', prediction_text='Appreciation value Rs. {}'.format(output))


model = pickle.load(open('model.pkl', 'rb'))'''
import RealEstate_Flask.views
