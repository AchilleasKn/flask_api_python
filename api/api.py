import pickle
import flask
from flask import request
from sklearn.linear_model import LogisticRegression

app = flask.Flask(__name__)

# Load our trained model from a file we created earlier
with open("iris_model.pkl", 'rb') as file:  
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    # grabbing a set of wine features from the request's body
    feature_array = request.get_json()['feature_array']

    # our model rates the wine based on the input array
    prediction = model.predict([feature_array]).tolist()
    
    # preparing a response object and storing the model's predictions
    response = {}
    response['prediction'] = prediction
    
    # sending our response object back as json
    return flask.jsonify(response)



# script initialization
if __name__ == '__main__':
    app.run(debug=True, port ='5000',host='0.0.0.0')
