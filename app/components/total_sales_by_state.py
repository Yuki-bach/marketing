import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from matplotlib.ticker import FuncFormatter
from utils.dataloader import load_csv_files


def display_total_sales_by_state():
    # Load data
    df_dict = load_csv_files()
    df_orders = df_dict["df_orders"]
    df_order_payments = df_dict["df_order_payments"]
    df_customers = df_dict["df_customers"]

    df = pd.merge(
        df_orders[["order_id", "customer_id"]],
        df_order_payments[["order_id", "payment_value"]],
        on="order_id",
    )
    df = pd.merge(
        df,
        df_customers[["customer_id", "customer_state"]],
        on="customer_id",
    )
    total_sales_by_state = (
        df.groupby("customer_state")["payment_value"].sum().sort_values(ascending=False)
    )

    # streamlit
    st.subheader("Total Sales by Customer State")
    __plot(total_sales_by_state)


def __plot(total_sales_by_state):
    _, ax = plt.subplots(figsize=(6, 2))
    total_sales_by_state.plot(kind="bar", color="skyblue")
    plt.xticks(rotation=45)
    plt.xlabel("Customer State")
    plt.ylabel("Total Sales (R$)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Customize y-axis to display in millions
    def millions_formatter(x, pos):
        return "%1.0fM" % (x * 1e-6)

    formatter = FuncFormatter(millions_formatter)
    ax.yaxis.set_major_formatter(formatter)
    st.pyplot(plt.gcf())
