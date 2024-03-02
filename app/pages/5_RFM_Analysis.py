import streamlit as st
from components.RFM.recency import display_recency
from components.RFM.frequency import display_frequency
from utils.set_favicon import set_favicon


def main():
    set_favicon()
    st.title("RFM Analysis")

    st.header("Recency")
    display_recency()

    st.header("Frequency")
    display_frequency()


if __name__ == "__main__":
    main()
