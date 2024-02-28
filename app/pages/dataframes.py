import pandas as pd
import streamlit as st

df_customers = pd.read_csv('datasets/olist_customers_dataset.csv')
df_geolocation = pd.read_csv('datasets/olist_geolocation_dataset.csv')
df_order_items = pd.read_csv('datasets/olist_order_items_dataset.csv')
df_order_payments = pd.read_csv('datasets/olist_order_payments_dataset.csv')
df_order_reviews = pd.read_csv('datasets/olist_order_reviews_dataset.csv')
df_orders = pd.read_csv('datasets/olist_orders_dataset.csv')
df_products = pd.read_csv('datasets/olist_products_dataset.csv')
df_sellers = pd.read_csv('datasets/olist_sellers_dataset.csv')
df_product_category_name = pd.read_csv('datasets/product_category_name_translation.csv')

def main():
  display_df_shapes()
  display_dfs()

def display_df_shapes():
  st.write('There are 8 dataframes in this dataset.')
  df_shapes = {
    "df_customers": df_customers.shape,
    "df_geolocation": df_geolocation.shape,
    "df_order_items": df_order_items.shape,
    "df_order_payments": df_order_payments.shape,
    "df_order_reviews": df_order_reviews.shape,
    "df_orders": df_orders.shape,
    "df_products": df_products.shape,
    "df_sellers": df_sellers.shape,
    "df_product_category_name": df_product_category_name.shape
  }
  df_shapes = pd.DataFrame(list(df_shapes.items()), columns=['DataFrame', 'Shape'])
  st.table(df_shapes)

def display_dfs():
  st.header('df_customers')
  st.dataframe(df_customers)

  st.header('df_geolocation')
  st.dataframe(df_geolocation)

  st.header('df_order_items')
  st.dataframe(df_order_items)

  st.header('df_order_payments')
  st.dataframe(df_order_payments)

  st.header('df_order_reviews')
  st.dataframe(df_order_reviews)

  st.header('df_orders')
  st.dataframe(df_orders)

  st.header('df_products')
  st.dataframe(df_products)

  st.header('df_sellers')
  st.dataframe(df_sellers)

  st.header('df_product_category_name')
  st.dataframe(df_product_category_name)

if __name__ == '__main__':
  main()
