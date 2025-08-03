# 🔥 Electric Motor Temperature Prediction (Lite Version)

This project predicts the **Permanent Magnet (PM) temperature** in an electric motor using machine learning (Random Forest Regression).  
This lightweight version is optimized for **evaluation and deployment**, trained on a **10,000-row subset** of the original dataset for faster performance and smaller model size.

---

## 🚀 Tech Stack
- Python 3.12
- Flask (Backend Web Framework)
- Scikit-learn (Model Training)
- Joblib (Model Serialization)
- HTML/CSS (Frontend)
- VS Code (IDE)

---

## 🧠 Problem Statement
Electric motors generate heat during operation, and predicting the **PM temperature** helps in:
- Avoiding overheating
- Optimizing performance
- Extending motor lifespan

---

## 📊 Features Used for Prediction

| Feature Name         | Description                             |
|----------------------|-----------------------------------------|
| `u_q`                | Voltage component in q-axis             |
| `coolant`            | Coolant temperature (°C)                |
| `stator_winding`     | Stator winding temperature (°C)         |
| `u_d`                | Voltage component in d-axis             |
| `stator_tooth`       | Stator tooth temperature (°C)           |
| `motor_speed`        | Motor speed (rpm)                       |
| `i_d`                | Current in d-axis                       |
| `i_q`                | Current in q-axis                       |
| `stator_yoke`        | Stator yoke temperature (°C)            |
| `ambient`            | Ambient temperature (°C)                |
| `torque`             | Motor torque (Nm)                       |

The model predicts: **`pm` – Permanent Magnet temperature (°C)**

---

## 🏗️ Project Structure

```
ElectricMotorTempPrediction_Lite/
├── app.py                         # Flask application
├── model/
│   └── model.save                # Trained ML model (included)
├── templates/
│   ├── index.html                # Input form
│   └── result.html               # Result display
├── static/
│   └── css/
│       └── style.css             # Optional: UI styling
├── notebook/
│   └── Rotor_motor_temp_detection.ipynb  # Model training
├── data_small.csv               # 10,000-row training dataset
├── requirement.txt              # Python dependencies
└── README.md                    # You’re here!
```

---

## 📦 Installation & Running

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ElectricMotorTempPrediction_Lite.git
cd ElectricMotorTempPrediction_Lite
```

### ✅ Step 2: Install Dependencies

```bash
pip install -r requirement.txt
```

### ✅ Step 3: Run the Flask App

```bash
python app.py
```

Then go to `http://127.0.0.1:5000/` in your browser.

---

## 📸 Screenshots

> *(Add your screenshots folder or embed image links if available)*

---

## 📽️ Demo Video

> [📹 Watch Demo Video](https://drive.google.com/...)  
> _(Replace with your actual demo video link)_

---

## 📁 Dataset Info

The original dataset contains 100,000+ rows.  
This version uses a 10,000-row subset for efficient local training and deployment.

---

## 🧠 Model Info

- Algorithm: Random Forest Regressor
- Training Set Size: 10,000 rows
- Output: PM Temperature (`pm`)
- Accuracy: _(Add R² score if known)_

---

## ✍️ Author

- **Your Name**  
- Final Year B.Tech Project – [Your College Name], 2025

---

## ✅ Submission Notes

This version:
- Includes a trained model (`model/model.save`)
- Does **not** depend on Google Drive or gdown
- Works **entirely offline**
- Suitable for quick demo and academic evaluation

---
