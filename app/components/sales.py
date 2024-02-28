import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from matplotlib.ticker import FuncFormatter
from dataloader import load_csv_files


def display_sales(state=""):
    df = __get_df(state)

    st.title(f'Total Sales {"in " + state if state else ""}')
    __plot_sales(df)


def __get_df(state=""):
    df_dict = load_csv_files()
    df_order_payments = df_dict["df_order_payments"]
    df_orders = df_dict["df_orders"]

    df = pd.merge(
        df_orders[["order_id", "customer_id", "order_purchase_timestamp"]],
        df_order_payments[["order_id", "payment_value"]],
        how="left",
        on="order_id",
    )
    if state:
        df_customers = df_dict["df_customers"]
        df = pd.merge(
            df,
            df_customers[["customer_id", "customer_state"]],
            how="left",
            on="customer_id",
        )
        df = df[df["customer_state"] == state]
        df.drop(columns=["customer_state"], inplace=True)

    return df


def __plot_sales(df):
    df_tmp = df.copy()
    df_tmp["order_purchase_timestamp"] = (
        df_tmp["order_purchase_timestamp"].dt.strftime("%Y/%m")
    )
    df_counts = df_tmp["order_purchase_timestamp"].value_counts().sort_index()
    df_total_sales = (
        df_tmp.groupby("order_purchase_timestamp")["payment_value"]
        .sum()
        .sort_index()
    )

    _, ax1 = plt.subplots(figsize=(20, 10))

    # line chart for "payment_value"
    ax1.plot(
        df_total_sales.index,
        df_total_sales.values,
        label="Total Sales",
        color="#03A9F4",
    )
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Total Sales", color="#03A9F4")
    ax1.tick_params(axis="y")

    # Customize y-axis to display in thousands
    def thousands_formatter(x, pos):
        return "%1.0fk" % (x * 1e-3)

    formatter = FuncFormatter(thousands_formatter)
    ax1.yaxis.set_major_formatter(formatter)
    ax1.set_xticklabels(df_total_sales.index, rotation=45)
    for i, v in enumerate(df_total_sales.values):
        label = "{:.1f}k".format(v / 1000)
        plt.text(i, v + 50, label, ha="center", va="bottom", fontsize=14)

    # bar chart for "order_purchase_timestamp"
    ax2 = ax1.twinx()
    ax2.bar(
        df_counts.index, df_counts.values, alpha=0.5,
        label="Counts", color="purple"
    )
    ax2.set_ylabel("Counts", color="purple")
    ax2.tick_params(axis="y")

    # label for bar chart
    max_count = df_counts.values.max()
    max_value = df_counts.values.max()
    offset_value = max_value * 0.07
    offset_percent = max_value * 0.01
    total_count = df_counts.values.sum()
    for i, v in enumerate(df_counts.values):
        plt.text(
            i, v + offset_value, str(v), ha="center", va="bottom", fontsize=14
        )
        plt.text(
            i,
            v + offset_percent,
            str(round(v / total_count * 100, 2)) + "%",
            ha="center",
            va="bottom",
            fontsize=14,
        )
    ax2.set_ylim(0, max_count * 2)

    # Display legend
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc="upper left")

    # Display plot in Streamlit
    st.pyplot(plt.gcf())
