# 🛡️ Phishing Website Detection

A machine learning-based web application that detects whether a given website URL is legitimate or phishing. The system analyzes URL-based features and uses trained ML models such as Random Forest and XGBoost to classify websites.

---

## 🚀 Problem Statement

Phishing websites are fake websites created to steal sensitive user information such as passwords, banking details, and personal data. Manually identifying phishing URLs is difficult because attackers often use misleading domains, suspicious links, and copied website designs.

This project aims to solve this problem by building an automated phishing website detection system that can classify URLs as safe or phishing using machine learning.

---

## 🎯 Objective

The main objective of this project is to:

- Detect phishing websites using machine learning
- Extract important features from website URLs
- Classify URLs as legitimate or phishing
- Provide a simple web interface for users
- Reduce the risk of users visiting harmful websites

---

## 🛠️ Tech Stack

| Component | Technology Used |
|---|---|
| Programming Language | Python |
| Web Framework | Streamlit |
| Machine Learning Models | Random Forest, XGBoost |
| Data Handling | Pandas, NumPy |
| Model Storage | Pickle |
| Development | Jupyter Notebook |
| Deployment | Streamlit / Localhost |

---

## 📌 Features

- Detects phishing and legitimate websites
- Takes website URL as input
- Extracts URL-based features
- Uses trained Random Forest and XGBoost models
- Displays prediction result in a user-friendly interface
- Simple and lightweight Streamlit web app
- Helps improve online safety and awareness

---

## ⚙️ Workflow

1. User enters a website URL
2. System extracts important URL features
3. Extracted features are passed to the trained ML model
4. Model predicts whether the website is phishing or legitimate
5. Result is displayed on the web interface

---

## 📂 Project Structure

```text
phishing_detection/
│
├── Phishing_Website_Detection.ipynb   # Model training and analysis notebook
├── app.py                             # Streamlit web application
├── random_forest_model.pkl            # Trained Random Forest model
├── xgboost_model.pkl                  # Trained XGBoost model
├── requirements.txt                   # Required Python libraries
└── README.md                          # Project documentation
```

---

## 🤖 Machine Learning Models Used

### Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### XGBoost

XGBoost is a powerful gradient boosting algorithm known for high accuracy and performance in classification problems.

---

## 📊 Output

The system provides a prediction result such as:

- Legitimate Website
- Phishing Website

This helps users quickly identify whether a URL may be harmful or safe to visit.

---

## 📥 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/phishing_detection.git
cd phishing_detection
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

### 4. Open in Browser

After running the command, open the local URL shown in the terminal.

Usually:

```text
http://localhost:8501
```

---

## 📦 Requirements

The project requires the following Python libraries:

```text
streamlit
pandas
numpy
scikit-learn
xgboost
```

---

## 📌 How to Use

1. Open the Streamlit application
2. Enter a website URL
3. Click on the prediction button
4. View whether the website is phishing or legitimate

---

## ✅ Result

The project successfully detects phishing websites using trained machine learning models. It provides a simple and effective interface for checking suspicious URLs and helps users avoid online threats.

---

## 🔮 Future Scope

- Add real-time website content analysis
- Improve model accuracy using larger datasets
- Add browser extension support
- Deploy the application publicly
- Include domain age and SSL certificate verification
- Add detailed explanation for each prediction

---

## 👩‍💻 Developed By

Atulya Mishra

---

## 📄 License

This project is created for academic and learning purposes.
