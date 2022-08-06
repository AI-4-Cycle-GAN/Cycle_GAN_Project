from convert_to_art import generate_art_from_image
from config import *
import streamlit as st
from PIL import Image
import numpy as np

def layout():
    st.title("Facial Expression Recognition System")
    st.sidebar.title("Facial Expression Recognition System")
    st.sidebar.header("Upload File")

def run_web_app():
    selection = layout()
    image_file = st.sidebar.file_uploader("Upload Image", type = ALLOWED_IMAGE_EXTENSIONS, key = "f1")
    if image_file is not None:
        image = np.array(Image.open(image_file).convert("RGB"))
        image, art = generate_art_from_image(image)
        st.subheader("Uploaded Image")
        st.header("Generated Art")
        st.image(art)

if __name__=="__main__":
    run_web_app()