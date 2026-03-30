import streamlit as st
from model import predict_message

# Page config
st.set_page_config(
    page_title="Spam Classifier",
    page_icon="📩",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.title("📌 About Project")
    st.write("""
    This app uses Machine Learning to detect spam messages.

    🔹 Model: Logistic Regression  
    🔹 Vectorizer: TF-IDF  
    🔹 Built with Streamlit  

    💡 Detect financial scam messages instantly!
    """)
    
    st.markdown("---")
    st.write("👨‍💻 Created by Mohd Jameel")

# Custom CSS (IMPROVED)
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #A0A0A0;
    margin-bottom: 25px;
}
.result-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    animation: fadeIn 0.5s ease-in-out;
}
.footer {
    text-align: center;
    font-size: 14px;
    color: gray;
    margin-top: 30px;
}
div.stButton > button {
    width: 100%;
    border-radius: 8px;
    font-size: 16px;
}
textarea {
    border-radius: 10px !important;
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📩 Spam Message Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered scam & spam detection system</div>', unsafe_allow_html=True)

# Info tip
st.info("💡 Try: 'Earn ₹50,000 per week from home. No investment required!'")

# Input
user_input = st.text_area("📥 Enter your message:", height=150)

# Example buttons (NEW 🔥)
col1, col2 = st.columns(2)

with col1:
    if st.button("📌 Try Spam Example"):
        user_input = "Invest ₹10,000 and earn ₹1 lakh instantly"

with col2:
    if st.button("📌 Try Normal Example"):
        user_input = "Hey, let's meet tomorrow for lunch"

# Button
if st.button("🔍 Analyze Message"):
    if user_input.strip() != "":
        
        with st.spinner("Analyzing message..."):
            result, confidence = predict_message(user_input)

        st.markdown("---")

        # Result Box
        if "Spam" in result:
            st.markdown(f"""
            <div class="result-box" style="background-color:#FF4B4B;">
            🚨 {result}
            </div>
            """, unsafe_allow_html=True)

        elif "Uncertain" in result:
            st.markdown(f"""
            <div class="result-box" style="background-color:#FFA500;">
            ⚠️ {result}
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown(f"""
            <div class="result-box" style="background-color:#2ECC71;">
            ✅ {result}
            </div>
            """, unsafe_allow_html=True)

        # Confidence Section
        st.write("### 📊 Confidence Score")
        st.progress(int(confidence * 100))
        st.write(f"{confidence*100:.2f}%")

    else:
        st.warning("⚠️ Please enter a message")

# Footer (YOUR STYLE IMPROVED 🔥)
st.markdown("---")
st.markdown(
    """
    <div class="footer">
    Built with ❤️ using Machine Learning & Streamlit <br><br>
    <b style="color:white;">Created by MOHD JAMEEL</b>
    </div>
    """,
    unsafe_allow_html=True
)
