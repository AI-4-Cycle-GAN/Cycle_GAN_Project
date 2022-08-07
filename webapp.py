from convert_to_art import generate_art_from_image
from config import *
import streamlit as st
from PIL import Image
import numpy as np

def layout():
    st.title("Generate Ukiyo-e Art From Images")
    st.sidebar.title("Generate Ukiyo-e Art From Images")

def run_web_app():
    selection = layout()
    image_file = st.sidebar.file_uploader("Upload Image", type = ALLOWED_IMAGE_EXTENSIONS, key = "f1")
    if image_file is not None:
        image = np.array(Image.open(image_file).convert("RGB"))
        image, art = generate_art_from_image(image)

        col1, col2 = st.columns(2)
        col1.subheader("Uploaded Image")
        col1.image(image, use_column_width = True)

        col2.subheader("Generated Art")
        col2.image(art, use_column_width = True)

        st.text("Note : Please bare with us regarding the artifacts. \nMaybe in the future a well trained model will generate even more beautiful art.")

if __name__=="__main__":
    run_web_app()