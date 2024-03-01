import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from dataloader import load_csv_files


# main function
def display_review_score(product_category=""):
    # Load data
    df_dict = load_csv_files()
    df_order_reviews = df_dict["df_order_reviews"].copy()
    df_order_items = df_dict["df_order_items"].copy()
    df_products = df_dict["df_products"].copy()
    df_product_category_name = df_dict["df_product_category_name"].copy()

    df = __merge_df(
        df_order_reviews, df_order_items, df_products, df_product_category_name
    )

    if product_category != "":
        df = df[df["product_category_name_english"] == product_category]

    __plot_bar_chart(df, product_category)


def display_order_count_by_product_category():
    # Load data
    df_dict = load_csv_files()
    df_order_reviews = df_dict["df_order_reviews"].copy()
    df_order_items = df_dict["df_order_items"].copy()
    df_products = df_dict["df_products"].copy()
    df_product_category_name = df_dict["df_product_category_name"].copy()

    df = __merge_df(
        df_order_reviews, df_order_items, df_products, df_product_category_name
    )

    __plot_bar_chart_order_count_by_product_category(df)


def __merge_df(df_order_reviews, df_order_items, df_products, df_product_category_name):
    df = pd.merge(
        df_order_reviews[["order_id", "review_score"]],
        df_order_items[["order_id", "product_id"]],
        how="left",
        on="order_id",
    )
    df = pd.merge(
        df,
        df_products[["product_id", "product_category_name"]],
        how="left",
        on="product_id",
    )
    df = pd.merge(
        df,
        df_product_category_name[
            ["product_category_name", "product_category_name_english"]
        ],
        how="left",
        on="product_category_name",
    )
    return df


def __plot_bar_chart(df, product_category):
    review_scores_counts = df["review_score"].value_counts().sort_index()

    # matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(review_scores_counts.index, review_scores_counts.values)
    plt.xlabel("Review Score")
    plt.ylabel("Number of Reviews")

    # streamlit
    st.title(
        f'Distribution of Review Scores {"for " + product_category if product_category else ""}'
    )
    st.pyplot(plt.gcf())


def __plot_bar_chart_order_count_by_product_category(df):
    st.title("Order Count by Product Category")
    category_num = st.slider(
        "Select the number of categories to display",
        min_value=5,
        max_value=71,  # 71 categories
        value=10,
        key="frequency",
    )

    order_count_by_product_category = (
        df["product_category_name_english"].value_counts().head(category_num)
    )

    # matplotlib
    plt.figure(figsize=(10, 6))
    plt.barh(
        order_count_by_product_category.index[::-1],
        order_count_by_product_category.values[::-1],
    )
    plt.xlabel("Number of Orders")
    plt.ylabel("Product Category")

    # streamlit
    st.pyplot(plt.gcf())
