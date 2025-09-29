# utils.py
import joblib
import pandas as pd
import streamlit as st

@st.cache_resource
def load_model(path: str):
    return joblib.load(path)

def preprocess_input(data: dict) -> pd.DataFrame:
    # Build a single-row DF
    df = pd.DataFrame([data])

    # Map Yes/No to 1/0
    df['Stage_fear'] = df['Stage_fear'].map({'Yes': 1, 'No': 0})
    df['Drained_after_socializing'] = df['Drained_after_socializing'].map({'Yes': 1, 'No': 0})


    feature_order = [
        'Time_spent_Alone',
        'Stage_fear',
        'Social_event_attendance',
        'Going_outside',
        'Friends_circle_size',
        'Post_frequency'
    ]

    # Reorder and return
    return df[feature_order]

def predict_personality(model, X: pd.DataFrame):
    # Make sure to pass a numpy array if your model expects that:
    arr = X.values
    prob = model.predict_proba(arr)[:, 1][0]
    label = "Introvert" if prob > 0.5 else "Extrovert"
    return label, prob
