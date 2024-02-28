import streamlit as st
import pandas as pd
import pydeck as pdk
from dataloader import load_csv_files

def main():
  # Load data
  df_state_coords = pd.read_csv('datasets/state_coords.csv')
  df_zip_coords = load_zip_coordinates()

  df_dict = load_csv_files()
  df_customers = df_dict['df_customers']
  df_sellers = df_dict['df_sellers']
  df_customers = rename_customers(df_customers)
  df_sellers = rename_sellers(df_sellers)

  # Create 4 dataframes
  df_customers_state = merge_df(df_customers, df_state_coords, "state")
  df_customers_zip = merge_df(df_customers, df_zip_coords, "zip")
  df_sellers_state = merge_df(df_sellers, df_state_coords, "state")
  df_sellers_zip = merge_df(df_sellers, df_zip_coords, "zip")

  display_maps(df_customers_state, df_customers_zip, df_sellers_state, df_sellers_zip)

def load_zip_coordinates():
  df_zip_coords = pd.read_csv('datasets/olist_geolocation_dataset.csv')
  df_zip_coords.dropna(subset=["geolocation_state", "geolocation_city"], inplace=True)
  df_zip_coords.rename(columns={
    "geolocation_zip_code_prefix": "zip",
    "geolocation_lat": "lat",
    "geolocation_lng": "lon"
  }, inplace=True)
  df_zip_coords = df_zip_coords.groupby("zip"). \
    agg({"lat": "mean", "lon": "mean"}). \
    reset_index()
  return df_zip_coords

def rename_customers(df_customers):
  df_customers.rename(
    columns={ 'customer_state': 'state', 'customer_zip_code_prefix': 'zip' },
    inplace=True
  )
  return df_customers

def rename_sellers(df_sellers):
  df_sellers.rename(
    columns={ 'seller_state': 'state', 'seller_zip_code_prefix': 'zip' },
    inplace=True
  )
  return df_sellers

def merge_df(df, df_coords, key):
  df_counts = df[key].value_counts().reset_index()
  df_counts = df_counts.merge(df_coords, how="left", on=key)
  return df_counts

def display_maps(df_customers_state, df_customers_zip, df_sellers_state, df_sellers_zip):
  tab1, tab2 = st.tabs(["Customers", "Sellers"])

  with tab1:
    color = { "name": "purple", "RGBA": [180, 0, 200, 140] }
    plot_basis = st.radio(
      "Choose the basis for plotting:",
      ["State", "Zip Code Prefix"],
      key="customers"
    )
    if plot_basis == "State":
      display_map(df_customers_state, "state", color)
    else:
      display_map(df_customers_zip, "zip", color)

  with tab2:
    color = { "name": "green", "RGBA": [0, 200, 0, 140] }
    plot_basis = st.radio(
      "Choose the basis for plotting:",
      ["State", "Zip Code Prefix"],
      key="sellers"
    )
    if plot_basis == "State":
      display_map(df_sellers_state, "state", color)
    else:
      display_map(df_sellers_zip, "zip", color)

def display_map(df_counts, on, color):
  radius_coef = (500_000 if on=="state" else 100_000) / df_counts['count'].max()
  layer = pdk.Layer(
    "ScatterplotLayer",
    df_counts,
    get_position=["lon", "lat"],
    get_radius=f"count * {radius_coef}",
    get_color=color["RGBA"],
    pickable=True,
    opacity=0.8,
  )
  # mouse over
  title = "State" if on == "state" else "Zip Code Prefix"
  tooltip = {
      "html": f"<b>{title}</b> {{{on}}}<br><b>Count:</b> {{count}}",
      "style": {
        "backgroundColor": color["name"],
        "color": "white"
      }
  }
  # Initial view state
  view_state = pdk.ViewState(
    latitude=df_counts["lat"].mean(),
    longitude=df_counts["lon"].mean(),
    zoom=3,
    pitch=0,
  )
  r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip)
  st.pydeck_chart(r)

  # Display the data
  if on == "state":
    st.dataframe(df_counts)
  else:
    st.write(f"Top 10 Zip Code Prefixes (There are {df_counts.shape[0]} unique zip code prefixes)")
    st.dataframe(df_counts.head(10))


if __name__ == '__main__':
  main()
