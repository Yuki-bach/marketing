import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from utils.dataloader import load_csv_files
from components.captions import (
    cap_payment_type,
    cap_evolution_of_payment_type,
    order_price_by_payment_type,
    cap_evolution_of_payment_type_as_percent
)


# main function
def display_payment_type(state=""):
    # Load data
    df_dict = load_csv_files()
    df_order_payments = df_dict["df_order_payments"].copy()
    df_orders = df_dict["df_orders"].copy()
    if state:
        df_orders = __filter_by_state(df_dict, df_orders, state)
    df = __merge_df(df_order_payments, df_orders)

    # Display charts
    st.title(f'Payment Type {"in " + state if state else ""}')
    __plot_pie_chart(df_order_payments)
    cap_payment_type()

    st.title(f'Evolution of Payment Type {"in " + state if state else ""}')
    __plot_line_chart(df)
    __show_credit_card_metrics(df)
    cap_evolution_of_payment_type()

    st.title(f'Evolution of Payment Type as Percentages {"in " + state if state else ""}')
    __plot_stacked_bar_chart(df)
    cap_evolution_of_payment_type_as_percent()


    st.title(f'Order Price by Payment Type {"in " + state if state else ""}')
    __plot_box_plot(df)
    order_price_by_payment_type()


def __filter_by_state(df_dict, df_orders, state):
    df_customers = df_dict["df_customers"]
    df_orders = pd.merge(
        df_orders,
        df_customers[["customer_id", "customer_state"]],
        how="left",
        on="customer_id",
    )
    df_orders = df_orders[df_orders["customer_state"] == state]
    df_orders.drop(columns=["customer_state"], inplace=True)
    return df_orders


def __plot_pie_chart(df_order_payments):
    df_payment_type = df_order_payments["payment_type"].value_counts()
    plt.figure(figsize=(8, 4))
    plt.pie(df_payment_type, labels=df_payment_type.index, autopct="%1.1f%%")
    st.pyplot(plt.gcf())
    with st.container(border=True):
        st.markdown(
            """
            **boleto**: an official form of payment regulated by the Central Bank of
            Brazil that uses vouchers to pay
            """
        )


def __merge_df(df_order_payments, df_orders):
    df = df_order_payments.copy()
    df = pd.merge(
        df,
        df_orders[["order_id", "order_purchase_timestamp"]],
        on="order_id",
        how="left",
    )
    df["order_purchase_timestamp"] = df["order_purchase_timestamp"].dt.strftime("%Y/%m")
    return df


def __plot_line_chart(df):
    df_counts = (
        df.groupby(["order_purchase_timestamp", "payment_type"])
        .size()
        .unstack(fill_value=0)
    )

    plt.figure(figsize=(8, 4))

    # Plot a line for each payment type
    for payment_type in df_counts.columns:
        plt.plot(df_counts.index, df_counts[payment_type], lw=2, label=payment_type)

    plt.xticks(rotation=45)
    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.legend(title="Payment Type")
    st.pyplot(plt.gcf())


def __show_credit_card_metrics(df):
    df_tmp = df.copy()
    df_tmp["order_purchase_timestamp"] = pd.to_datetime(
        df_tmp["order_purchase_timestamp"]
    )
    df_tmp = df_tmp[df_tmp["payment_type"] == "credit_card"]
    total_count_2017 = df_tmp.query(
        "'2017-01-01' <= order_purchase_timestamp <= '2017-8-31'"
    ).shape[0]
    total_count_2018 = df_tmp.query(
        "'2018-01-01' <= order_purchase_timestamp <= '2018-8-31'"
    ).shape[0]

    with st.container(border=True):
        st.metric(
            label="Total count of Credit Card Usage in 2017 between January and August",
            value=total_count_2017,
        )
        st.metric(
            label="Total count of Credit Card Usage in 2018 between January and August",
            value=total_count_2018,
            delta=f"{total_count_2018 / total_count_2017 * 100:.2f}%",
        )

def __plot_stacked_bar_chart(df):
  df_counts = (
    df.groupby(["order_purchase_timestamp", "payment_type"])
    .size()
    .unstack(fill_value=0)
  )

  percentages = df_counts.div(df_counts.sum(axis=1), axis=0)
  cumulative = np.zeros(len(df_counts))

  plt.figure(figsize=(8, 4))

  # Plot a bar for each payment type
  for payment_type in percentages.columns:
    plt.bar(df_counts.index, percentages[payment_type], bottom=cumulative, label=payment_type)
    cumulative += percentages[payment_type]

  plt.xticks(rotation=45)
  plt.xlabel("Month")
  plt.ylabel("Percentage")
  plt.legend(title="Payment Type")
  plt.ylim(0, 1)
  st.pyplot(plt.gcf())

def __plot_box_plot(df):
    plt.figure(figsize=(8, 4))
    payment_types = df["payment_type"].unique()
    payment_values = [
        df.loc[df["payment_type"] == pt, "payment_value"] for pt in payment_types
    ]

    box = plt.boxplot(
        payment_values, labels=payment_types, vert=True, patch_artist=True
    )

    # Set color of boxes
    colors = plt.get_cmap("Set2")
    for i, patch in enumerate(box["boxes"]):
        patch.set_facecolor(colors(i))

    plt.boxplot(payment_values, labels=payment_types, vert=True)
    plt.yscale("log")
    plt.xlabel("Payment Type")
    plt.ylabel("Price (Log)")
    st.pyplot(plt.gcf())
