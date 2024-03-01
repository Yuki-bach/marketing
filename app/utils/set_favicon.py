import os
import streamlit as st
from PIL import Image


def set_favicon():
    script_dir = os.path.dirname(__file__)
    rel_path = "../images/asu_icon.png"
    abs_file_path = os.path.join(script_dir, rel_path)
    image = Image.open(abs_file_path)
    st.set_page_config(page_icon=image)
