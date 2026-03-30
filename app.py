import streamlit as st
from model import predict_message

st.set_page_config(page_title="Spam Classifier", page_icon="📩")

# Title
st.title("📩 Spam Classifier")

# Input
user_input = st.text_area("Enter a message:")

# Button
if st.button("Analyze"):
    if user_input.strip():
        result, confidence = predict_message(user_input)

        # Result
        if "Spam" in result:
            st.error(result)
        elif "Uncertain" in result:
            st.warning(result)
        else:
            st.success(result)

        # Confidence
        st.write(f"Confidence: {confidence*100:.2f}%")
        st.progress(int(confidence * 100))

    else:
        st.warning("Please enter a message")
