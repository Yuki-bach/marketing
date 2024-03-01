import streamlit as st

from utils.dataloader import load_csv_files
from components.sales import display_sales
from components.total_order import display_total_order
from components.order_date_by_states import display_total_order_by_states
from components.payment_type import display_payment_type
from components.ordered_product_category import display_ordered_product_category
from components.order_count_by_state import display_order_count_by_state
from components.payment_amount import display_payment_amount
from utils.set_favicon import set_favicon


def main():
    set_favicon()
    # Load data
    df_dict = load_csv_files()
    df_customers = df_dict["df_customers"]

    display_order_count_by_state()

    tab1, tab2 = st.tabs(["State", "Several States"])
    with tab1:
        # Set selectbox
        states = df_customers["customer_state"].unique()
        state = st.selectbox("Choose the state for plotting:", states, key="state_box")

        # Set button
        submit_button = st.button("Show Charts", key="state_btn")
        if submit_button:
            st.toast(f"State name: {state}", icon="🇧🇷")
            display_sales(state)
            display_total_order(state)
            display_ordered_product_category(state)
            display_payment_amount(state)
            display_payment_type(state)
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
            display_total_order_by_states(selected_states)


if __name__ == "__main__":
    main()
