import pandas as pd
import streamlit as st


@st.cache_data
def load_csv_files():
    df_dict = {}
    for key, path in csv_files.items():
        dtype = dtype_dict.get(key, {})
        df_dict[key] = pd.read_csv(path, dtype=dtype)

    df_dict["df_orders"]["order_purchase_timestamp"] = pd.to_datetime(
        df_dict["df_orders"]["order_purchase_timestamp"]
    )

    return df_dict


csv_files = {
    "df_customers": "datasets/olist_customers_dataset.csv",
    "df_geolocation": "datasets/olist_geolocation_dataset.csv",
    "df_order_items": "datasets/olist_order_items_dataset.csv",
    "df_order_payments": "datasets/olist_order_payments_dataset.csv",
    "df_order_reviews": "datasets/olist_order_reviews_dataset.csv",
    "df_orders": "datasets/olist_orders_dataset.csv",
    "df_products": "datasets/olist_products_dataset.csv",
    "df_sellers": "datasets/olist_sellers_dataset.csv",
    "df_product_category_name": "datasets/product_category_name_translation.csv",
}

dtype_dict = {
    "df_customers": {
        "customer_id": "string",
        "customer_unique_id": "string",
        "customer_zip_code_prefix": "uint32",
        "customer_city": "string",
        "customer_state": "category",
    },
    "df_geolocation": {
        "geolocation_zip_code_prefix": "uint32",
        "geolocation_lat": "float32",
        "geolocation_lng": "float32",
        "geolocation_city": "string",
        "geolocation_state": "category",
    },
    "df_order_items": {
        "order_id": "string",
        "order_item_id": "uint8",
        "product_id": "string",
        "seller_id": "string",
        "shipping_limit_date": "string",
        "price": "float32",
        "freight_value": "float32",
    },
    "df_order_payments": {
        "order_id": "string",
        "payment_sequential": "uint8",
        "payment_type": "category",
        "payment_installments": "uint8",
        "payment_value": "float32",
    },
    "df_order_reviews": {
        "review_id": "string",
        "order_id": "string",
        "review_score": "uint8",
        "review_comment_title": "string",
        "review_comment_message": "string",
        "review_creation_date": "string",
        "review_answer_timestamp": "string",
    },
    "df_orders": {
        "order_id": "string",
        "customer_id": "string",
        "order_status": "category",
        "order_purchase_timestamp": "string",
        "order_approved_at": "string",
        "order_delivered_carrier_date": "string",
        "order_delivered_customer_date": "string",
        "order_estimated_delivery_date": "string",
    },
    "df_products": {
        "product_id": "string",
        "product_category_name": "category",
        "product_name_lenght": "float32",
        "product_description_lenght": "float32",
        "product_photos_qty": "float32",
        "product_weight_g": "float32",
        "product_length_cm": "float32",
        "product_height_cm": "float32",
        "product_width_cm": "float32",
    },
    "df_sellers": {
        "seller_id": "string",
        "seller_zip_code_prefix": "uint32",
        "seller_city": "string",
        "seller_state": "category",
    },
    "df_product_category_name": {
        "product_category_name": "string",
        "product_category_name_english": "string",
    },
}
