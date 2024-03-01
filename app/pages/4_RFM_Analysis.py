import streamlit as st
from components.recency import display_recency


def main():
    st.title("RFM Analysis")
    st.header("Recency")
    display_recency()


if __name__ == "__main__":
    main()
