import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Image Forgery Detection")

st.title("🔍 Image Forgery Detection (Demo)")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Simulate detection (placeholder logic)
    st.write("Running forgery detection...")
    
    # Placeholder logic
    st.warning("⚠️ This is a demo. No real detection is done.")
    st.success("Prediction: Image is likely Authentic (placeholder)")

    # Example extension: show image array
    # st.write(np.array(image))
