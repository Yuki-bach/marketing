import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from utils.dataloader import load_csv_files


def display_order_count_by_state():
    # Load data
    df_dict = load_csv_files()
    df_customers = df_dict["df_customers"]
    df_customers_by_state = df_customers["customer_state"].value_counts()

    # matplotlib
    __plot(df_customers_by_state)

    # streamlit
    st.header("Order Count by Customer State")
    st.pyplot(plt.gcf())


def __plot(df_customers_by_state):
    plt.figure(figsize=(6, 3))
    df_customers_by_state.plot(kind="bar", color="skyblue")
    plt.xticks(rotation=45)
    plt.xlabel("Customer State")
    plt.ylabel("Order Count")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
    # memo: I tried to use st.bar_chart, but the state is alphabetically sorted.
