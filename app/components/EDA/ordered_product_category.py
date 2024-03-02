import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from components.captions import cap_top10_ordered_product_categories
from utils.dataloader import load_csv_files


def display_ordered_product_category(state=""):
    # Load 3 data
    df_dict = load_csv_files()
    df_order_items = df_dict["df_order_items"]
    df_products = df_dict["df_products"]
    df_product_category_name = df_dict["df_product_category_name"]
    df = __merge_df(df_products, df_product_category_name, df_order_items)
    if state:
        df = __filter_by_state(df_dict, df, state)

    # count
    counts = df["product_category_name_english"].value_counts()
    counts_head = counts.head(10)
    category_num = df_product_category_name.shape[0]

    __plot(counts_head)

    # Display using streamlit
    st.title(f"Top 10 Ordered Product Categories  {'in ' + state if state else ''}")
    st.write(f"There are {category_num} categories in total.")
    st.pyplot(plt.gcf())
    cap_top10_ordered_product_categories()
    st.dataframe(counts, height=200)


def __filter_by_state(df_dict, df, state):
    df_tmp = df.copy()
    df_orders = df_dict["df_orders"]
    df_customers = df_dict["df_customers"]

    df_tmp = pd.merge(
        df_tmp,
        df_orders[["order_id", "customer_id"]],
        how="left",
        on="order_id",
    )
    df_tmp = pd.merge(
        df_tmp,
        df_customers[["customer_id", "customer_state"]],
        how="left",
        on="customer_id",
    )

    df_tmp = df_tmp[df_tmp["customer_state"] == state]
    df_tmp.drop(columns=["customer_state"], inplace=True)
    return df_tmp


def __merge_df(df_products, df_product_category_name, df_order_items):
    df = pd.merge(
        df_products[["product_id", "product_category_name"]],
        df_product_category_name,
        how="left",
        on="product_category_name",
    )
    df = pd.merge(
        df,
        df_order_items[["order_id", "product_id"]],
        how="left",
        on="product_id",
    )
    return df


def __plot(counts_head):
    plt.figure(figsize=(8, 4))
    counts_head.plot(kind="bar")
    plt.xticks(rotation=45)
    plt.xlabel("Product Category")
    plt.ylabel("Count")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
