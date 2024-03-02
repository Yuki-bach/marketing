import streamlit as st
from utils.image_utils import get_image


def set_favicon():
    image = get_image("../images/asu_icon.png")
    st.set_page_config(page_icon=image)
