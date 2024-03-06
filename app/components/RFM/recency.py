import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from components.captions import cap_recency
from utils.dataloader import load_csv_files


def display_recency():
    # Load the data
    df_dict = load_csv_files()
    df_orders = df_dict["df_orders"].copy()
    df_customers = df_dict["df_customers"].copy()

    df_recency = get_df_recency(df_orders, df_customers)

    # streamlit
    col1, col2 = st.columns([5, 2])
    with col1:
        st.write("Recency Dataframe:")
        st.dataframe(df_recency, height=320)
    with col2:
        st.write("Recency Stats:")
        st.write(df_recency.Recency.describe())
    code = """
            # How to calculate Recency
            df_recency["Recency"] = (
                df_recency["LatestPurchaseDate"].max() - df_recency["LatestPurchaseDate"]
            ).dt.days
      """
    st.code(code, language="python")
    __display_histogram(df_recency)
    cap_recency()


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
    df_recency.columns = ["customer_unique_id", "LatestPurchaseDate"]

    # Calculate Recency
    df_recency["Recency"] = (
        df_recency["LatestPurchaseDate"].max() - df_recency["LatestPurchaseDate"]
    ).dt.days

    return df_recency


def __display_histogram(df):
    bins = st.slider(
        "Select the number of bins", min_value=1, max_value=50, value=10, key="recency"
    )

    plt.figure(figsize=(8, 4))
    plt.hist(df["Recency"], bins=bins, edgecolor="k")
    plt.xlabel("Recency (days)")
    plt.ylabel("Frequency")
    plt.title("Recency Distribution")

    st.pyplot(plt.gcf())
    plt.close()
