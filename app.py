import streamlit as st
from model import predict_message

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

    🔹 Model: Multinomial Naive Bayes  
    🔹 Vectorizer: TF-IDF (n-grams)  
    🔹 Built with Streamlit  

    💡 Detects financial scam messages too!
    """)

# Title
st.title("📩 Spam Message Classifier")
st.caption("AI-powered message detection system")

st.info("💡 Try: 'Earn ₹50,000 per week from home'")

# Input
user_input = st.text_area("📥 Enter your message:", height=150)

if st.button("🔍 Analyze Message"):
    if user_input.strip() != "":
        
        with st.spinner("Analyzing..."):
            result, confidence = predict_message(user_input)

        st.markdown("---")

        # Result display
        if "Spam" in result:
            st.error(result)
        elif "Uncertain" in result:
            st.warning(result)
        else:
            st.success(result)

        # Confidence
        st.write("### 📊 Confidence Score")
        st.progress(int(confidence * 100))
        st.write(f"{confidence*100:.2f}%")

    else:
        st.warning("⚠️ Please enter a message")

st.markdown("---")
st.caption("Built with ❤️ by Mohd Jameel")