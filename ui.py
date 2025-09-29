import streamlit as st

def render_header():
    st.title("🔮 Personality Predictor")
    st.write("Enter your daily behavior to predict whether you are an Introvert or Extrovert.")


def render_input_form():
    with st.form(key='input_form'):
        time_alone = st.slider("Hours spent alone daily", 0, 11, 4)
        stage_fear = st.selectbox("Stage fear?", ["Yes", "No"])
        social_events = st.slider("Social event attendance (0-10)", 0, 10, 5)
        going_out = st.slider("Days go outside per week", 0, 7, 3)
        drained = st.selectbox("Drained after socializing?", ["Yes", "No"])
        friends = st.slider("Number of close friends", 0, 15, 5)
        posts = st.slider("Social media posts per day", 0, 10, 3)
        submit = st.form_submit_button("Predict")
        if submit:
            return {
                'Time_spent_Alone': time_alone,
                'Stage_fear': stage_fear,
                'Social_event_attendance': social_events,
                'Going_outside': going_out,
                'Drained_after_socializing': drained,
                'Friends_circle_size': friends,
                'Post_frequency': posts
            }
    return None


def render_prediction(label, probability):
    st.subheader("Prediction Result")
    st.write(f"**Personality**: {label}")
    # st.write(f"**Confidence**: {probability * 100:.1f}%")
    if label == "Introvert":
        st.info("You are likely an Introvert. 🌱")
    else:
        st.success("You are likely an Extrovert. 🎉")
