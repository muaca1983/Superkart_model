from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# Load serialized model pipeline
MODEL_PATH = os.path.join(os.path.dirname(__file__), "superkart_model.joblib")
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "SuperKart Model Deployment API is Running!"})

@app.route("/v1/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        df_input = pd.DataFrame([data])
        prediction = model.predict(df_input)
        return jsonify({"prediction": float(prediction[0])}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/v1/predictbatch", methods=["POST"])
def predict_batch():
    try:
        data = request.get_json()
        df_input = pd.DataFrame(data)
        predictions = model.predict(df_input)
        return jsonify({"predictions": predictions.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)
