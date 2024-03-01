import streamlit as st
from components.recency import display_recency
from components.frequency import display_frequency


def main():
    st.title("RFM Analysis")

    st.header("Recency")
    display_recency()

    st.header("Frequency")
    display_frequency()


if __name__ == "__main__":
    main()
