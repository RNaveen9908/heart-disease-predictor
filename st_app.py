import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    h1 {
        text-align: center;
    }

    .stDataFrame {
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# Load Model
model = joblib.load("model.pkl")

# Heading
st.markdown("<h1>❤️ Heart Disease Prediction System</h1>", unsafe_allow_html=True)

# Center Table
col1, col2, col3 = st.columns([1,2,1])

with col2:

    age = st.number_input("Age", min_value=1, max_value=120, value=50)
    sex = st.selectbox("Sex", [0,1])
    cp = st.selectbox("Chest Pain Type", [0,1,2,3])
    trestbps = st.number_input("Resting Blood Pressure", value=120)
    chol = st.number_input("Cholesterol", value=200)
    fbs = st.selectbox("Fasting Blood Sugar", [0,1])
    restecg = st.selectbox("Rest ECG", [0,1,2])
    thalach = st.number_input("Max Heart Rate", value=150)
    exang = st.selectbox("Exercise Induced Angina", [0,1])
    oldpeak = st.number_input("Old Peak", value=1.0)
    slope = st.selectbox("Slope", [0,1,2])
    ca = st.selectbox("CA", [0,1,2,3,4])
    thal = st.selectbox("Thal", [0,1,2,3])

    input_df = pd.DataFrame({
        "age":[age],
        "sex":[sex],
        "cp":[cp],
        "trestbps":[trestbps],
        "chol":[chol],
        "fbs":[fbs],
        "restecg":[restecg],
        "thalach":[thalach],
        "exang":[exang],
        "oldpeak":[oldpeak],
        "slope":[slope],
        "ca":[ca],
        "thal":[thal]
    })

    st.dataframe(input_df)

    if st.button("Predict"):

        prediction = model.predict(input_df)

        if prediction[0] == 1:
            st.error("⚠️ Heart Disease Detected")
        else:
            st.success("✅ No Heart Disease Detected")