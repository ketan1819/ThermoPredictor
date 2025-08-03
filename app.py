from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# === Load model and scaler ===
MODEL_PATH = os.path.join('model', 'model.save')
SCALER_PATH = os.path.join('model', 'scaler.save')

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# === Home page ===
@app.route('/')
def home():
    return render_template('index.html')

# === Prediction route ===
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Input order must match model training features
        input_order = [
            'u_q', 'coolant', 'stator_winding', 'u_d', 'stator_tooth',
            'motor_speed', 'i_d', 'i_q', 'stator_yoke', 'ambient', 'torque'
        ]

        # Collect inputs from form
        input_features = [float(request.form[feature]) for feature in input_order]

        # Convert to numpy array and scale
        input_array = np.array(input_features).reshape(1, -1)
        scaled_input = scaler.transform(input_array)

        # Make prediction
        prediction = model.predict(scaled_input)[0]

        return render_template('result.html', prediction=round(prediction, 2))

    except Exception as e:
        return f"❌ Error occurred: {str(e)}"

# === Local test only ===
if __name__ == '__main__':
    app.run(debug=True)
