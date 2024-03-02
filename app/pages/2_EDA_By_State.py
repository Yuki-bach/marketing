import streamlit as st

from utils.dataloader import load_csv_files
from components.EDA.monthly_sales import display_sales
from components.EDA.total_order import display_total_order
from components.EDA.order_date_by_states import display_total_order_by_states
from components.EDA.payment_type import display_payment_type
from components.EDA.ordered_product_category import display_ordered_product_category
from components.EDA.order_count_by_state import display_order_count_by_state
from components.EDA.payment_amount import display_payment_amount
from components.EDA.total_sales_by_state import display_total_sales_by_state
from components.EDA.state_names import display_state_names
from utils.set_favicon import set_favicon
from utils.eda_headers import get_eda_headers


def main():
    set_favicon()
    # Load data
    df_dict = load_csv_files()
    df_customers = df_dict["df_customers"]

    col1, col2 = st.columns([4, 1])
    with col1:
        display_order_count_by_state()
        display_total_sales_by_state()
    with col2:
        display_state_names()

    st.subheader("Explore Each State")
    tab1, tab2 = st.tabs(["State", "Several States"])
    with tab1:
        # Set selectbox
        states = df_customers["customer_state"].unique()
        state = st.selectbox("Choose the state for plotting:", states, key="state_box")

        # Set button
        submit_button = st.button("Show Charts", key="state_btn")
        if submit_button:
            st.toast(f"State name: {state}", icon="🇧🇷")
            toc(state)
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


def toc(state):
    headers = get_eda_headers()

    toc_md = (
        "<ul>"
        + "".join(
            f'<li><a href="#{header["id"]}-in-{state.lower()}">{header["title"]}</a></li>'
            for header in headers
        )
        + "</ul>"
    )
    with st.expander("Table of Contents", expanded=True):
        st.markdown(toc_md, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
