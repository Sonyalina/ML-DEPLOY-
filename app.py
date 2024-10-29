import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
from sklearn.linear_model import LinearRegression
app = Flask(__name__)

model=pickle.load(open('model_save','rb'))
@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    Weight = float(request.form.get('Weight', 0.0))
    Height = float(request.form.get('Height',0.0))
    input_data = [[Weight, Height]]
    print(input_data)
    prediction = model.predict(input_data)
    print(prediction)
    output=round(prediction[0], 2)
    print(output)
    
    
    if output < float(18.5):
        return render_template('index1.html',prediction_text =f'This is your BMI {output}.\n!!you are Underweight !!'.format(output))
    elif output >= float(18.5) and output <= float(25) :
        return render_template('index1.html',prediction_text =f'This is your BMI {output}.\n!! you are Healthy weight range !!'.format(output))
    else:
        return render_template('index1.html',prediction_text =f'This is your BMI {output}.\n!! you are Overweight !!'.format(output))

if __name__ == "__main__":
    app.run(debug=True, port=5000)