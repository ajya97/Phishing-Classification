# 🛡️ PhishGuard AI - Intelligent Phishing URL Detection System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.x-black.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

### 🚀 An End-to-End Machine Learning Project for Real-Time Phishing URL Detection

**Predict whether a website URL is Safe or Phishing using Machine Learning and a Flask Web Application.**

</div>

---

# 📌 Project Overview

PhishGuard AI is a complete end-to-end Machine Learning application that detects phishing websites by analyzing URL-based features. The system extracts multiple characteristics from a URL, feeds them into a trained machine learning model, and predicts whether the URL is legitimate or malicious.

Unlike traditional phishing datasets that require website HTML or DNS information, this project focuses on **features that can be extracted directly from a URL**, making predictions fast and suitable for real-time applications.

---

# ✨ Features

* ✅ End-to-End Machine Learning Pipeline
* ✅ Automatic URL Feature Extraction
* ✅ Multiple Machine Learning Models
* ✅ Best Model Selection
* ✅ Flask Web Application
* ✅ Real-Time URL Prediction
* ✅ Probability Score
* ✅ Model Evaluation Reports
* ✅ Unit Testing with PyTest
* ✅ Clean Project Structure
* ✅ Modular Python Code
* ✅ Production-Ready Folder Structure

---

# 📂 Project Structure

```text
phishing-classification/

│
├── app/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│
├── reports/
│
├── src/
│   ├── config.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── predict.py
│   ├── evaluate.py
│   └── utils.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── run.py
```

---

# ⚙️ Technology Stack

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* XGBoost
* LightGBM
* CatBoost

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib

### Web Framework

* Flask

### Testing

* PyTest

---

# 📊 Dataset

The model is trained on a phishing URL dataset containing:

* URL
* Label
* URL Length
* Number of Dots
* HTTPS
* IP Address Presence
* Number of Subdirectories
* Number of Parameters
* Suspicious Keywords
* TLD
* Special Character Count
* Digit Count
* Shannon Entropy

---

# 🧠 URL Features Used

The system automatically extracts features such as:

* URL Length
* Number of Dots
* HTTPS Usage
* IP Address Detection
* Number of Subdirectories
* Query Parameters
* Suspicious Keywords
* Top Level Domain (TLD)
* Special Character Count
* Digit Count
* Shannon Entropy

No manual feature engineering is required during prediction.

---

# 🤖 Machine Learning Models

The project trains and compares multiple algorithms.

* Logistic Regression
* Decision Tree
* Random Forest
* Extra Trees
* XGBoost
* LightGBM
* CatBoost

The model with the best validation performance is automatically saved.

---

# 📈 Model Evaluation

Evaluation metrics include:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC Curve
* Confusion Matrix
* Classification Report

Generated reports are stored inside the **reports/** directory.

---

# 🌐 Web Application

The web application allows users to:

* Enter a website URL
* Detect phishing instantly
* View prediction confidence
* Display Safe or Phishing result

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/phishguard-ai.git
```

Move into the project directory:

```bash
cd phishguard-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Train the Model

```bash
python src/train.py
```

---

# 📊 Evaluate the Model

```bash
python src/evaluate.py
```

---

# 🌍 Run the Application

```bash
python run.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# 💻 Example Prediction

Input

```text
https://paypal-login-security.xyz/login
```

Output

```text
Prediction : Phishing

Confidence : 98.67%
```

---

# 🧪 Running Tests

Run all tests

```bash
pytest
```

Run model tests

```bash
pytest tests/test_model.py
```

Run API tests

```bash
pytest tests/test_api.py
```

Run preprocessing tests

```bash
pytest tests/test_preprocessing.py
```

---

# 📁 Generated Files

```text
models/
    best_model.pkl

reports/
    confusion_matrix.png
    roc_curve.png
    evaluation_metrics.csv
    classification_report.txt
```

---

# 📌 Future Improvements

* Browser Extension
* REST API
* Explainable AI (SHAP)
* Batch URL Prediction
* Docker Support
* Cloud Deployment
* User Authentication
* Prediction History
* Dark Mode Interface
* Threat Intelligence Integration

---

# 🎯 Skills Demonstrated

* Machine Learning
* Feature Engineering
* Model Evaluation
* Python Programming
* Flask Development
* Data Preprocessing
* Software Testing
* Project Architecture
* Git & GitHub
* Clean Code Practices

---

# 📸 Screenshots

Add screenshots here after running the application.

```text
screenshots/

home.png

prediction.png

result.png
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ajeet Yadav**

Machine Learning Engineer | Python Developer | AI Enthusiast

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile

Email: [your-email@example.com](mailto:your-email@example.com)

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

**Made with ❤️ using Python, Machine Learning, and Flask**

</div>
