import pandas as pd
import streamlit as st

csv_files = {
  "df_customers": 'datasets/olist_customers_dataset.csv',
  "df_geolocation": 'datasets/olist_geolocation_dataset.csv',
  "df_order_items": 'datasets/olist_order_items_dataset.csv',
  "df_order_payments": 'datasets/olist_order_payments_dataset.csv',
  "df_order_reviews": 'datasets/olist_order_reviews_dataset.csv',
  "df_orders": 'datasets/olist_orders_dataset.csv',
  "df_products": 'datasets/olist_products_dataset.csv',
  "df_sellers": 'datasets/olist_sellers_dataset.csv',
  "df_product_category_name": 'datasets/product_category_name_translation.csv'
}

@st.cache_resource
def load_csv_files():
  df_dict = {}
  for key, path in csv_files.items():
    df_dict[key] = pd.read_csv(path)

  # Convert order_purchase_timestamp to datetime
  df_dict['df_orders']['order_purchase_timestamp'] = pd.to_datetime(
    df_dict['df_orders']['order_purchase_timestamp']
  )

  return df_dict
