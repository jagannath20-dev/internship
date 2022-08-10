# importing the necessary dependencies
from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
import os
import pickle
from flask_cors import CORS, cross_origin
import numpy as np


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
# Initialising the model
model1 = pickle.load(open("finalized_mode4.sav","rb"))





@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()


def predict():
    '''
    for rendering results on HTML
        '''
    features = [int(x) for x in request.form.values()]

    # re-arranging the list as per data set
    feature_list = [features[4]] + features[:4] + features[5:11][::-1] + features[11:17][::-1] + features[17:][::-1]
    features_arr = [np.array(feature_list)]

    prediction1 = model1.predict(features_arr)

    print(features_arr)
    print("prediction value: ", prediction1)





    result = ""
    if prediction1 == 1:
        result = "The credit card holder will be Defaulter in the next month"
    else:
        result = "The Credit card holder will not be Defaulter in the next month"


    return render_template('index.html', prediction_text = result)


if __name__ == '__main__':
    app.run(debug=True)

