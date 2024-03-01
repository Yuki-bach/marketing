import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from utils.dataloader import load_csv_files


def display_frequency():
    # Load data
    df_dict = load_csv_files()
    df_orders = df_dict["df_orders"].copy()
    df_customers = df_dict["df_customers"].copy()

    df_frequency = get_df_frequency(df_orders, df_customers)

    # Display charts
    col1, col2, _ = st.columns([4, 2, 1])
    with col1:
        st.write("Frequency Dataframe:")
        st.dataframe(df_frequency, height=320)
    with col2:
        st.write("Frequency Stats:")
        st.write(df_frequency.Frequency.describe())
    __display_histogram(df_frequency)


def get_df_frequency(df_orders, df_customers):
    df_tmp = pd.merge(
        df_orders[["customer_id", "order_purchase_timestamp"]],
        df_customers[["customer_id", "customer_unique_id"]],
        on="customer_id",
    )
    df_frequency = (
        df_tmp[["customer_unique_id", "order_purchase_timestamp"]]
        .groupby("customer_unique_id")
        .order_purchase_timestamp.count()
        .reset_index()
    )
    df_frequency.columns = ["customer_unique_id", "Frequency"]

    return df_frequency


def __display_histogram(df):
    bins = st.slider(
        "Select the number of bins",
        min_value=1,
        max_value=50,
        value=10,
        key="frequency",
    )

    plt.figure(figsize=(10, 6))
    plt.hist(df["Frequency"], bins=bins, edgecolor="k", color="purple")
    plt.xlabel("Frequency")
    plt.title("Frequency Distribution")

    st.pyplot(plt)
