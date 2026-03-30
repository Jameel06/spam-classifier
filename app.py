import streamlit as st
from model import predict_message

# Page Config
st.set_page_config(
    page_title="Spam Classifier",
    page_icon="📩",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #A0A0A0;
    margin-bottom: 25px;
}
.box {
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
}
.footer {
    text-align: center;
    font-size: 13px;
    color: gray;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📩 Spam Message Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Detect spam & financial scam messages using Machine Learning</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📌 About")
    st.write("""
    This app detects whether a message is spam or not using Machine Learning.

    🔹 Model: Logistic Regression  
    🔹 Vectorizer: TF-IDF  
    🔹 Use case: Financial scam detection  
    """)

    st.markdown("---")
    st.write("👨‍💻 Created by Mohd Jameel")

# Input Box
user_input = st.text_area("📥 Enter your message:", height=150)

# Example Buttons
st.write("### 💡 Try Examples")
col1, col2 = st.columns(2)

with col1:
    if st.button("Spam Example"):
        user_input = "Earn ₹50,000 per week from home. No investment required!"

with col2:
    if st.button("Normal Example"):
        user_input = "Hey, are we meeting tomorrow?"

# Analyze Button
if st.button("🔍 Analyze Message"):
    if user_input.strip():

        with st.spinner("Analyzing..."):
            result, confidence = predict_message(user_input)

        st.markdown("---")

        # Result Display
        if "Spam" in result:
            st.markdown(f'<div class="box" style="background-color:#FF4B4B;">🚨 {result}</div>', unsafe_allow_html=True)
        elif "Uncertain" in result:
            st.markdown(f'<div class="box" style="background-color:#FFA500;">⚠️ {result}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="box" style="background-color:#2ECC71;">✅ {result}</div>', unsafe_allow_html=True)

        # Confidence
        st.write("### 📊 Confidence Score")
        st.progress(int(confidence * 100))
        st.write(f"{confidence*100:.2f}% confidence")

    else:
        st.warning("⚠️ Please enter a message")

# Footer
st.markdown("""
<div class="footer">
Built with ❤️ using Machine Learning & Streamlit<br>
<b>Portfolio Project | Spam Detection System</b>
</div>
""", unsafe_allow_html=True)
