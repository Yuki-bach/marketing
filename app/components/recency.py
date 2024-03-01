import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from dataloader import load_csv_files


def display_recency():
    # Load the data
    df_dict = load_csv_files()
    df_orders = df_dict["df_orders"].copy()
    df_customers = df_dict["df_customers"].copy()

    df_recency = get_df_recency(df_orders, df_customers)

    # streamlit
    col1, col2, _ = st.columns([3, 1, 1])
    with col1:
        st.write("Recency Dataframe:")
        st.dataframe(df_recency, height=320)
    with col2:
        st.write("Recency Stats:")
        st.write(df_recency.Recency.describe())

    __display_histogram(df_recency)


def get_df_recency(df_orders, df_customers):
    df_tmp = pd.merge(
        df_orders[["customer_id", "order_purchase_timestamp"]],
        df_customers[["customer_id", "customer_unique_id"]],
        on="customer_id",
    )
    # Get the last purchase date for each customer
    df_recency = (
        df_tmp[["customer_unique_id", "order_purchase_timestamp"]]
        .groupby("customer_unique_id")["order_purchase_timestamp"]
        .max()
        .reset_index()
    )
    df_recency.columns = ["customer_unique_id", "MaxPurchaseDate"]

    # Calculate Recency
    df_recency["Recency"] = (
        df_recency["MaxPurchaseDate"].max() - df_recency["MaxPurchaseDate"]
    ).dt.days

    return df_recency


def __display_histogram(df):
    bins = st.slider(
        "Select the number of bins", min_value=1, max_value=50, value=10, key="recency"
    )

    plt.figure(figsize=(10, 6))
    plt.hist(df["Recency"], bins=bins, edgecolor="k", color="purple")
    plt.xlabel("Recency (days)")
    plt.ylabel("Frequency")
    plt.title("Recency Distribution")

    st.pyplot(plt)
