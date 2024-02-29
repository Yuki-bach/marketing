import streamlit as st

from dataloader import load_csv_files
from components.sales import display_sales
from components.order_date import display_order_date
from components.order_date_by_states import display_order_date_by_states
from components.payments import display_payments


def main():
    # Load data
    df_dict = load_csv_files()
    df_customers = df_dict["df_customers"]
    df_customers_by_state = df_customers["customer_state"].value_counts().reset_index()

    st.title("Data by Customer State")
    st.dataframe(df_customers_by_state, height=200)

    tab1, tab2 = st.tabs(["State", "Several States"])
    with tab1:
        # Set selectbox
        states = df_customers["customer_state"].unique()
        state = st.selectbox("Choose the state for plotting:", states, key="state_box")

        # Set button
        submit_button = st.button("Show Charts", key="state_btn")
        if submit_button:
            st.toast(f"State name: {state}", icon="🇧🇷")
            display_order_date(state)
            display_sales(state)
            display_payments(state)
    with tab2:
        # Set multiselect
        states = df_customers["customer_state"].unique()
        selected_states = st.multiselect(
            "Choose the states for plotting:", states, key="states_box"
        )

        # Set button
        submit_button = st.button("Show Charts", key="states_btn")
        if submit_button:
            st.toast(f"State names: {', '.join(selected_states)}", icon="🇧🇷")
            display_order_date_by_states(selected_states)


if __name__ == "__main__":
    main()
