import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from components.captions import cap_payment_amount
from utils.dataloader import load_csv_files


def display_payment_amount(state=""):
    # Load data
    df_dict = load_csv_files()
    df = df_dict["df_order_payments"].copy()
    df = df[["order_id", "payment_value"]]

    if state:
        df = __filter_df(df_dict, df, state)

    # Display charts
    st.title(f'Payment Amount {"in " + state if state else ""}')
    __display_histogram(df)
    cap_payment_amount()
    __display_box_plot(df)


def __filter_df(df_dict, df, state):
    df_orders = df_dict["df_orders"]
    df_customers = df_dict["df_customers"]
    df = pd.merge(
        df,
        df_orders[["order_id", "customer_id"]],
        on="order_id",
        how="left",
    )
    df = pd.merge(
        df,
        df_customers[["customer_id", "customer_state"]],
        on="customer_id",
        how="left",
    )
    df = df[df["customer_state"] == state]
    df.drop(columns=["customer_id", "customer_state"], inplace=True)
    return df


def __display_histogram(df):
    plt.figure(figsize=(8, 4))
    plt.hist(df["payment_value"], bins=50, edgecolor="k")
    plt.xlabel("Payment Value")
    plt.ylabel("Frequency")
    plt.title("Payment Value Distribution")

    st.pyplot(plt)


def __display_box_plot(df):
    plt.figure(figsize=(10, 2))
    plt.boxplot(df["payment_value"], vert=False, patch_artist=True)

    plt.xscale("log")  # Set the x-axis to a logarithmic scale
    plt.xlabel("Payment Value (Log Scale)")  # Update the x-axis label
    plt.title("Box Plot of Payment Value")

    # Display the box plot
    st.pyplot(plt.gcf())
