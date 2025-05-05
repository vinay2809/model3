import streamlit as st
import joblib  # or pickle, if your model is stored that way

# Load your model
model = joblib.load("your_model.pkl")

st.title("Prediction App")

user_input = st.text_input("Enter input:")

if st.button("Predict"):
    result = model.predict([user_input])
    st.success(f"Prediction: {result[0]}")
