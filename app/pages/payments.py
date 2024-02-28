import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

def main():
  df_order_payments = pd.read_csv('datasets/olist_order_payments_dataset.csv')
  df_orders = pd.read_csv('datasets/olist_orders_dataset.csv')

  sns.set_theme(style='darkgrid')
  plot_pie_chart(df_order_payments)
  plot_payments_by_month(df_order_payments, df_orders)

def plot_pie_chart(df_order_payments):
  df_payment_type = df_order_payments['payment_type'].value_counts()
  plt.figure(figsize=(6, 3))
  plt.pie(df_payment_type, labels=df_payment_type.index, autopct='%1.1f%%')
  st.title('Payment Type')
  st.pyplot(plt.gcf())
  """
    ※**boleto**: an official form of payment regulated by the Central Bank of Brazil that uses vouchers to pay
  """

def plot_payments_by_month(df_order_payments, df_orders):
  df = df_order_payments.copy()
  df = pd.merge(df, df_orders[['order_id', 'order_purchase_timestamp']], on='order_id', how='left')
  df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
  df['order_purchase_timestamp'] = df['order_purchase_timestamp'].dt.strftime('%Y/%m')
  df_counts = df.groupby(['order_purchase_timestamp', 'payment_type']). \
    size().unstack(fill_value=0)

  plt.figure(figsize=(10, 5))

  # Plot a line for each payment type
  for payment_type in df_counts.columns:
    plt.plot(df_counts.index, df_counts[payment_type], lw=2, label=payment_type)

  plt.xticks(rotation=45)
  plt.xlabel('Date')
  plt.ylabel('Count')
  plt.legend(title='Payment Type')

  # Display plot in Streamlit
  st.title('Evolution of Payment Type')
  st.pyplot(plt.gcf())


if __name__ == '__main__':
  main()
