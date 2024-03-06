import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from matplotlib.ticker import FuncFormatter
from components.captions import cap_total_sales
from components.ask_ai import ask_ai
from utils.dataloader import load_csv_files


def display_sales(state=""):
    df = __get_df(state)

    st.title(f'Total Sales {"in " + state if state else ""}')
    __plot(df)
    cap_total_sales()
    __show_sales_metrics(df)


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


def __plot(df):
    # Prepare data
    df_tmp = df.copy()
    df_tmp["order_purchase_timestamp"] = df_tmp["order_purchase_timestamp"].dt.strftime(
        "%Y/%m"
    )
    df_counts = df_tmp["order_purchase_timestamp"].value_counts().sort_index()
    df_total_sales = (
        df_tmp.groupby("order_purchase_timestamp")["payment_value"].sum().sort_index()
    )

    # Create plot
    fig, ax1 = plt.subplots(figsize=(8, 4))
    __plot_line_chart(ax1, df_total_sales)
    ax2 = ax1.twinx()
    __plot_bar_chart(ax2, df_counts)

    # Display legend
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc="upper left")

    # Display plot in Streamlit
    st.pyplot(plt.gcf())

    # ask ai
    ask_ai(fig)


def __plot_line_chart(ax1, df_total_sales):
    color1 = plt.get_cmap("Set2")(0)

    ax1.plot(
        df_total_sales.index,
        df_total_sales.values,
        label="Total Sales (R$ in millions)",
        color=color1,
        lw=2,
    )
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Total Sales (R$ in millions)", color=color1)
    ax1.tick_params(axis="y")

    # Customize y-axis to display in millions
    def millions_formatter(x, pos):
        return "%1.01fm" % (x * 1e-6)

    formatter = FuncFormatter(millions_formatter)
    ax1.yaxis.set_major_formatter(formatter)
    ax1.set_xticklabels(df_total_sales.index, rotation=45)


def __plot_bar_chart(ax2, df_counts):
    color2 = plt.get_cmap("Set2")(1)

    ax2.bar(
        df_counts.index,
        df_counts.values,
        alpha=0.5,
        label="Order Counts",
        color=color2,
    )
    ax2.set_ylabel("Order Counts", color=color2)
    ax2.tick_params(axis="y")

    # Customize y-axis to display in millions
    def thousands_formatter(x, pos):
        return "%1.0fk" % (x * 1e-3)

    formatter = FuncFormatter(thousands_formatter)
    ax2.yaxis.set_major_formatter(formatter)

    # label for bar chart
    max_count = df_counts.values.max()
    ax2.set_ylim(0, max_count * 2)


def __show_sales_metrics(df):
    total_sales_2017 = df.query(
        "'2017-01-01' <= order_purchase_timestamp <= '2017-8-31'"
    )["payment_value"].sum()
    total_sales_2018 = df.query(
        "'2018-01-01' <= order_purchase_timestamp <= '2018-8-31'"
    )["payment_value"].sum()

    total_sales_2017_formatted = "R${:,.0f}".format(total_sales_2017)
    total_sales_2018_formatted = "R${:,.0f}".format(total_sales_2018)
    with st.container(border=True):
        st.metric(
            label="Total Sales in 2017 between January and August",
            value=total_sales_2017_formatted,
        )
        st.metric(
            label="Total Sales in 2018 between January and August",
            value=total_sales_2018_formatted,
            delta=f"{total_sales_2018 / total_sales_2017 * 100:.2f}%",
        )
