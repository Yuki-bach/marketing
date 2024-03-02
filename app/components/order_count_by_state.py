import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from matplotlib.ticker import FuncFormatter
from utils.dataloader import load_csv_files


def display_order_count_by_state():
    # Load data
    df_dict = load_csv_files()
    df_customers = df_dict["df_customers"]
    df_customers_by_state = df_customers["customer_state"].value_counts()

    # matplotlib
    __plot(df_customers_by_state)

    # streamlit
    st.subheader("Order Count by Customer State")
    st.pyplot(plt.gcf())


def __plot(df_customers_by_state):
    _, ax = plt.subplots(figsize=(6, 2))
    df_customers_by_state.plot(kind="bar", color="skyblue")
    plt.xticks(rotation=45)
    plt.xlabel("Customer State")
    plt.ylabel("Order Count")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Customize y-axis to display in thousands
    def thousands_formatter(x, pos):
        return "%1.0fk" % (x * 1e-3)

    formatter = FuncFormatter(thousands_formatter)
    ax.yaxis.set_major_formatter(formatter)
    # memo: I tried to use st.bar_chart, but the state is alphabetically sorted.
