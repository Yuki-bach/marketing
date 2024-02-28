import streamlit as st
import pandas as pd
import pydeck as pdk

def display_map(df, df_state_coords):
  # Merge the data with the coordinates
  df_counts = df.state.value_counts().reset_index()
  df_counts.columns = ['state', 'count']
  df_counts = df_counts.merge(df_state_coords, how='left', on='state')

  radius_coef = 500_000 / df_counts['count'].max()

  layer = pdk.Layer(
    "ScatterplotLayer",
    df_counts,
    get_position=["lon", "lat"],
    get_radius=f"count * {radius_coef}",
    get_color=[180, 0, 200, 140],
    pickable=True,
    opacity=0.8,
  )
  # mouse over
  tooltip = {
    "html": "<b>State:</b> {state}<br><b>Count:</b> {count}",
    "style": {
      "backgroundColor": "purple",
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
  st.dataframe(df_counts)

def main():
  # Load the state coordinates
  df_state_coords = pd.read_csv('datasets/state_coords.csv')

  # Create the tabs
  tab1, tab2 = st.tabs(["Customers", "Sellers"])
  with tab1:
    df_customers = pd.read_csv('datasets/olist_customers_dataset.csv')
    df_customers.rename(columns={'customer_state': 'state'}, inplace=True)
    display_map(df_customers, df_state_coords)
  with tab2:
    df_sellers = pd.read_csv('datasets/olist_sellers_dataset.csv')
    df_sellers.rename(columns={'seller_state': 'state'}, inplace=True)
    display_map(df_sellers, df_state_coords)

if __name__ == '__main__':
  main()
