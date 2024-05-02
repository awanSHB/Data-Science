import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained machine learning model
with open('./model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = request.get_json()  # Get JSON data from the request
        print(input_data)
        # Convert the input data to a DataFrame and rename columns to match training data
        df = pd.DataFrame([input_data])
        df.columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                      'BMI', 'DiabetesPedigreeFunction', 'Age']

        # Make predictions using the loaded model
        prediction = loaded_model.predict(df)
        print(prediction)

        return {'prediction': prediction.tolist()}  # Convert prediction to a Python list before returning as JSON


if __name__ == '__main__':
    app.run(debug=True)
