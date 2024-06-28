from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open("model_pickle1.pkl", "rb"))

# Define the predict function
def predict(oxy, pulse, clieus):
    result = np.array([[float(oxy), float(pulse), float(clieus)]])
    prediction = model.predict(result)
    print(prediction)
    return prediction.item()

# Define the API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict_endpoint():
    # Get the data from the request body
    data = request.json

    # Extract parameters
    oxy = data.get('oxy')
    pulse = data.get('pulse')
    clieus = data.get('clieus')

    # Perform prediction
    prediction = predict(oxy, pulse, clieus)

    # Prepare response
    result = {"prediction": prediction}

    # Return response as JSON
    return jsonify(result)

# Define a route for the root URL
@app.route('/')
def index():
    return 'Welcome to my Flask API!'

# Define a route for the favicon
@app.route('/favicon.ico')
def favicon():
    return '', 404

if __name__ == '__main__':
    app.run(port=8080, debug=True)
