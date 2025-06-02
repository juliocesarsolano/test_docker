from flask import Flask, request, jsonify
import joblib

# Cargar modelo entrenado localmente
model = joblib.load("model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return "API local de predicción de diabetes (sin MLflow)"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    features = data.get("features")

    if features is None:
        return jsonify({"error": "Se requiere el campo 'features'"}), 400

    try:
        prediction = model.predict([features])
        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


# Icono favicon
from flask import send_from_directory
import os

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
