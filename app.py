
import streamlit as st
from utils import load_model, preprocess_input, predict_personality
from ui import render_header, render_input_form, render_prediction

# Set page config with light theme
st.set_page_config(page_title="Personality Predictor", layout="centered", initial_sidebar_state="auto")

# Render the app header
render_header()

# Load model
model = load_model("./models/model.pkl")

# Render input form and collect user inputs
user_input = render_input_form()

# When user submits, preprocess and predict
if user_input is not None:
    X = preprocess_input(user_input)
    prediction, prob = predict_personality(model, X)
    render_prediction(prediction, prob)