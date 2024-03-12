import streamlit as st
from utils.image_utils import get_image

def display_brazil_state_map():
  if 'show_map' not in st.session_state:
    st.session_state['show_map'] = False

  def toggle_map_display():
    st.session_state['show_map'] = not st.session_state['show_map']

  if st.button(
    'Show Map' if not st.session_state['show_map'] else 'Close Map',
    on_click=toggle_map_display
  ):
    pass

  if st.session_state['show_map']:
    image = get_image("../images/brazil_state_map.png")
    st.image(
      image,
      caption="Map of administrative divisions of Brazil (https://en.wikipedia.org/wiki/Federative_units_of_Brazil)"
    )
