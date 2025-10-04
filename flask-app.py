
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import json


# Load your trained model
with open("model_log.pkl", "rb") as f:
    model = pickle.load(f)


# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    try:

        if request.method=='POST':

            form_data_dict = request.form.to_dict()
            for key in form_data_dict:
                form_data_dict[key] = [form_data_dict[key]]
            df = pd.DataFrame(form_data_dict)
            print(df)
            prediction = model.predict(df)
            
            return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

# # PS D:\ml-demo> curl -X POST http://127.0.0.1:5000/predict `  -H "Content-Type: application/json" `  -d @D:\ml-demo\data.json