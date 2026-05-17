# app.py

import streamlit as st
import numpy as np
import joblib
import re

from urllib.parse import urlparse

# =========================================================
# LOAD MODELS
# =========================================================

rf_model = joblib.load("random_forest_model.pkl")
xgb_model = joblib.load("xgboost_model.pkl")

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Phishing Website Detection",
    page_icon="🔒",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    color: white;
    text-align: center;
    font-size: 48px !important;
}

.stTextInput > div > div > input {
    background-color: #262730;
    color: white;
    border-radius: 10px;
    border: 1px solid #00ADB5;
}

.stSelectbox > div > div {
    background-color: #262730;
    color: white;
}

.stButton > button {
    width: 100%;
    background-color: #00ADB5;
    color: white;
    font-size: 20px;
    font-weight: bold;
    border-radius: 10px;
    height: 3em;
    border: none;
}

.stButton > button:hover {
    background-color: #008C9E;
    color: white;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("🔒 Phishing Website Detection System")

st.markdown("""
<center>

AI-powered phishing website detector using  
Machine Learning & Ensemble Learning Models.

</center>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================================
# MODEL SELECTION
# =========================================================

model_choice = st.selectbox(
    "Select ML Model",
    ["Random Forest", "XGBoost"]
)

# =========================================================
# URL INPUT
# =========================================================

url = st.text_input(
    "🌐 Enter Website URL",
    placeholder="https://example.com"
)

# =========================================================
# FEATURE EXTRACTION FUNCTION
# =========================================================

def extract_features(url):

    features = []

    # 1. URL Length
    features.append(-1 if len(url) > 75 else 1)

    # 2. Shortening Service
    shortening_services = r"bit\.ly|goo\.gl|tinyurl|t\.co"

    features.append(
        -1 if re.search(shortening_services, url) else 1
    )

    # 3. Having @ Symbol
    features.append(-1 if "@" in url else 1)

    # 4. Double Slash Redirecting
    features.append(
        -1 if url.rfind('//') > 7 else 1
    )

    # 5. Prefix-Suffix
    features.append(
        -1 if '-' in urlparse(url).netloc else 1
    )

    # 6. Having Sub Domain
    domain = urlparse(url).netloc
    dots = domain.count('.')

    if dots == 1:
        features.append(1)
    else:
        features.append(-1)

    # 7. SSL Final State
    features.append(
        1 if url.startswith("https") else -1
    )

    # =====================================================
    # REMAINING FEATURES
    # =====================================================

    remaining_features = [0] * 22

    features.extend(remaining_features)

    return np.array(features).reshape(1, -1)

# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button("🔍 Analyze Website"):

    if url == "":

        st.warning("⚠ Please enter a website URL.")

    else:

        features = extract_features(url)

        # =================================================
        # MODEL PREDICTION
        # =================================================

        if model_choice == "Random Forest":
            prediction = rf_model.predict(features)

        else:
            prediction = xgb_model.predict(features)

        # =================================================
        # OUTPUT
        # =================================================

        st.write("")
        st.write("")

        if prediction[0] == 1:

            st.markdown("""
            <div class="result-box"
            style="background-color:#1B4332; color:white;">

            ✅ Legitimate Website

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result-box"
            style="background-color:#7F1D1D; color:white;">

            🚨 Phishing Website Detected

            </div>
            """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("---")

st.markdown("""
<center>

Made with ❤️ using Streamlit, Random Forest & XGBoost

</center>
""", unsafe_allow_html=True)