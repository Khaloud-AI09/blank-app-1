import streamlit as st
from PIL import Image
import numpy as np

# 1. Page Config (The Aesthetic Part)
st.set_page_config(page_title="LeafyCheck", page_icon="🌿")

# Custom CSS for that "Cute" look
st.markdown("""
    <style>
    .main { background-color: #FAF5F1; } /* Off-white background */
    h1 { color: #848469; font-family: 'Alice', serif; } /* Sage Green */
    .stButton>button { border-radius: 20px; background-color: #848469; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 LeafyCheck: Plant Thirst Detector")
st.write("Upload a photo of your plant to see if it needs a drink!")

# 2. File Uploader
uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Your Plant Friend', use_column_width=True)
    
    st.write("🪄 *Analyzing the leaves...*")
    
    # 3. Logic Placeholder 
    # (In a full setup, you'd insert your Teachable Machine link here)
    # For now, let's pretend it detected 'Thirsty'
    
    result = "Thirsty" # This would come from your model prediction
    
    if result == "Thirsty":
        st.warning("🥀 Your plant looks a bit thirsty! Time for some water.")
    else:
        st.success("✨ Your plant is perky and happy! Keep it up.")