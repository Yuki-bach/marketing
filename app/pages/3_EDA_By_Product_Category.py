import streamlit as st
from components.review_score import display_review_score, display_order_count_by_product_category
from utils.dataloader import load_csv_files


def main():
    # Load data
    df_dict = load_csv_files()

    display_order_count_by_product_category()

    # User input
    product_categories = df_dict["df_product_category_name"][
        "product_category_name_english"
    ].unique()
    product_category = st.selectbox(
        "Choose the state for plotting:", product_categories, key="product_category_box"
    )

    # Set button
    submit_button = st.button("Show Charts", key="product_category_btn")
    if submit_button:
        display_review_score(product_category)


if __name__ == "__main__":
    main()
