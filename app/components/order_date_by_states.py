import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from dataloader import load_csv_files


# main function
def display_order_date_by_states(states):
    # Load data
    df_dict = load_csv_files()
    df_orders = df_dict["df_orders"].copy()
    df_orders = __filter_by_state(df_dict, df_orders, states)

    # Display charts
    st.title(f'Total Order in {(", ").join(states)}')
    __plot_order_date(df_orders)

    st.title(f'Total Order per Weekday in {(", ").join(states)}')
    __plot_per_weekday(df_orders)

    st.title(f'Total Order per Time of Day in {(", ").join(states)}')
    __plot_order_per_time_of_day(df_orders)


def __filter_by_state(df_dict, df_orders, states):
    df_customers = df_dict["df_customers"]
    df_orders = pd.merge(
        df_orders,
        df_customers[["customer_id", "customer_state"]],
        how="left",
        on="customer_id",
    )
    df_orders = df_orders[df_orders["customer_state"].isin(states)]
    return df_orders


def __plot_order_date(df_orders):
    df = df_orders.copy()
    df["order_purchase_timestamp"] = df["order_purchase_timestamp"].dt.strftime("%Y/%m")
    df_counts = (
        df.groupby(["order_purchase_timestamp", "customer_state"])
        .size()
        .unstack(fill_value=0)
    )

    plt.figure(figsize=(10, 5))

    for state in df_counts.columns:
        plt.plot(df_counts.index, df_counts[state], lw=2, label=state)

    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend(title="Customer State", bbox_to_anchor=(1.05, 1), loc="upper left")

    st.pyplot(plt.gcf())


def __plot_per_weekday(df_orders):
    df = df_orders.copy()
    df["weekday"] = df["order_purchase_timestamp"].dt.day_name()

    df_week_counts = (
        df.groupby(["weekday", "customer_state"]).size().unstack(fill_value=0)
    )
    df_week_counts = df_week_counts.reindex(
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    )

    # Create bar chart
    plt.figure(figsize=(10, 5))

    df_week_counts.plot(kind="bar", stacked=False, width=0.8)

    plt.xticks(rotation=45)
    plt.xlabel("Weekday")
    plt.ylabel("Count")
    plt.title("Orders per Weekday by Customer State")

    st.pyplot(plt.gcf())


def __plot_order_per_time_of_day(df_orders):
    def assign_time_of_day(hour):
        if 0 <= hour < 6:
            return "Early Morning"
        elif 6 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 18:
            return "Afternoon"
        else:
            return "Evening"

    df = df_orders.copy()
    df["time_of_day"] = df["order_purchase_timestamp"].dt.hour.apply(assign_time_of_day)

    df_counts = (
        df.groupby(["time_of_day", "customer_state"]).size().unstack(fill_value=0)
    )
    df_counts = df_counts.reindex(["Early Morning", "Morning", "Afternoon", "Evening"])

    # Create bar chart
    plt.figure(figsize=(10, 5))

    # Plot a bar for each customer state
    df_counts.plot(kind="bar", stacked=False)

    plt.xlabel("Time of Day")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())

    time_of_day_df = pd.DataFrame(
        {
            "Time of Day": ["Early Morning", "Morning", "Afternoon", "Evening"],
            "Time Range": [
                "0:00 - 5:59",
                "6:00 - 11:59",
                "12:00 - 17:59",
                "18:00 - 23:59",
            ],
        }
    )
    st.table(time_of_day_df)
