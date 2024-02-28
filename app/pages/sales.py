import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd

def main():
  df = get_df()
  plot_sales(df)

def get_df():
  df_order_payments = pd.read_csv('datasets/olist_order_payments_dataset.csv')
  df_orders = pd.read_csv('datasets/olist_orders_dataset.csv')
  df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'])
  df = pd.merge(
    df_orders[["order_id", "order_purchase_timestamp"]],
    df_order_payments[["order_id" ,"payment_value"]],
    how="left",
    on='order_id'
  )
  return df

def plot_sales(df):
  df_tmp = df.copy()
  df_tmp['order_purchase_timestamp'] = df_tmp['order_purchase_timestamp'].dt.strftime('%Y/%m')
  df_counts = df_tmp['order_purchase_timestamp'].value_counts().sort_index()
  df_total_sales = df_tmp.groupby('order_purchase_timestamp')['payment_value'].sum().sort_index()

  _, ax1 = plt.subplots(figsize=(10, 5))

  # line chart for "payment_value"
  ax1.plot(df_total_sales.index, df_total_sales.values, label='Total Sales', color="#03A9F4")
  ax1.set_xlabel('Date')
  ax1.set_ylabel('Total Sales')
  ax1.tick_params(axis='y', labelcolor="#03A9F4")

  # Customize y-axis to display in thousands
  def thousands_formatter(x, pos):
    return '%1.0fk' % (x * 1e-3)

  formatter = FuncFormatter(thousands_formatter)
  ax1.yaxis.set_major_formatter(formatter)
  ax1.set_xticklabels(df_total_sales.index, rotation=45)
  for i, v in enumerate(df_total_sales.values):
    label = '{:.1f}k'.format(v / 1000)
    plt.text(i, v + 50, label, ha='center', va='bottom', fontsize=7)

  # bar chart for "order_purchase_timestamp"
  ax2 = ax1.twinx()
  ax2.bar(df_counts.index, df_counts.values, alpha=0.5, label='Counts', color='purple')
  ax2.set_ylabel('Counts')
  ax2.tick_params(axis='y', labelcolor='purple')
  total_count = df_counts.values.sum()
  max_count = df_counts.values.max()
  for i, v in enumerate(df_counts.values):
    plt.text(i, v + 500, str(v), ha='center', va='bottom', fontsize=7)
    plt.text(
      i, v + 50, str(round(v / total_count * 100, 2)) + '%',
      ha='center', va='bottom', fontsize=6
    )
  ax2.set_ylim(0, max_count * 2)

  # Display legend
  lines, labels = ax1.get_legend_handles_labels()
  lines2, labels2 = ax2.get_legend_handles_labels()
  ax2.legend(lines + lines2, labels + labels2, loc='upper left')

  # Display plot in Streamlit
  st.title('Total Sales')
  st.pyplot(plt.gcf())


if __name__ == '__main__':
  main()
