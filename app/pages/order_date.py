import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from dataloader import load_csv_files

sns.set_theme(style='darkgrid')

def main():
  df_dict = load_csv_files()
  df_orders = df_dict['df_orders']
  df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'])

  plot_order_date(df_orders)
  plot_per_weekday(df_orders)
  plot_order_per_time_of_day(df_orders)

def plot_order_date(df_orders):
  df = df_orders.copy()
  df['order_purchase_timestamp'] = df['order_purchase_timestamp'].dt.strftime('%Y/%m')
  df_counts = df['order_purchase_timestamp'].value_counts().sort_index()

  # Create plot
  plt.figure(figsize=(10, 5))
  plt.plot(df_counts.index, df_counts.values, lw=4)
  plt.xticks(rotation=45)
  plt.xlabel('Date')
  plt.ylabel('Count')

  # Display plot in Streamlit
  st.title('Total Order')
  st.pyplot(plt.gcf())

def plot_per_weekday(df_orders):
  df = df_orders.copy()
  df['weekday'] = df['order_purchase_timestamp'].dt.day_name()

  df_week_counts = df['weekday'].value_counts().reindex([
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
  ])

  # Create bar chart
  plt.figure(figsize=(10, 5))
  plt.bar(df_week_counts.index, df_week_counts.values)
  plt.xticks(rotation=45)
  plt.xlabel('Week')
  plt.ylabel('Count')
  for i, v in enumerate(df_week_counts.values):
    plt.text(i, v + 50, str(v), ha='center', va='bottom')

  # Display plot in Streamlit
  st.title('Total Order per Weekday')
  st.pyplot(plt.gcf())

def plot_order_per_time_of_day(df_orders):
  def assign_time_of_day(hour):
    if 0 <= hour < 6:
      return 'Early Morning'
    elif 6 <= hour < 12:
      return 'Morning'
    elif 12 <= hour < 18:
      return 'Afternoon'
    else:
      return 'Evening'

  df = df_orders.copy()
  df['time_of_day'] = df['order_purchase_timestamp'].dt.hour.apply(assign_time_of_day)
  df_counts = df['time_of_day'].value_counts().reindex([
    "Early Morning", "Morning", "Afternoon", "Evening"
  ])

  # Create plot
  plt.figure(figsize=(10, 5))
  plt.bar(df_counts.index, df_counts.values, color=['blue', 'orange', 'green', 'red'])
  plt.xlabel('Time of Day')
  plt.ylabel('Count')
  plt.xticks(rotation=45)
  for i, v in enumerate(df_counts.values):
    plt.text(i, v + 50, str(v), ha='center', va='bottom')

  # Display plot in Streamlit
  st.title('Total Order per Time of Day')
  st.pyplot(plt.gcf())
  time_of_day_df = pd.DataFrame({
    "Time of Day": ["Early Morning", "Morning", "Afternoon", "Evening"],
    "Time Range": ["0:00 - 5:59", "6:00 - 11:59", "12:00 - 17:59", "18:00 - 23:59"]
  })
  st.table(time_of_day_df)


if __name__ == '__main__':
  main()
