import streamlit as st
from utils.image_utils import get_image

def display_brazil_state_map():
  image = get_image("../images/brazil_state_map.png")
  st.image(
      image,
      caption="Map of administrative divisions of Brazil (https://en.wikipedia.org/wiki/Federative_units_of_Brazil)"
  )
