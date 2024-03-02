import streamlit as st

from components.EDA.monthly_sales import display_sales
from components.EDA.total_order import display_total_order
from components.EDA.payment_type import display_payment_type
from components.EDA.ordered_product_category import display_ordered_product_category
from components.EDA.payment_amount import display_payment_amount
from components.EDA.review_score import display_review_score
from utils.set_favicon import set_favicon
from utils.eda_headers import get_eda_headers


def main():
    set_favicon()
    toc()

    display_sales()
    display_total_order()
    display_ordered_product_category()
    display_payment_amount()
    display_payment_type()
    display_review_score()


def toc():
    headers = get_eda_headers()
    toc_md = "<ul>" + "".join(
        f'<li><a href="#{header["id"]}">{header["title"]}</a></li>'
        for header in headers
    ) + "</ul>"
    with st.expander("Table of Contents", expanded=True):
        st.markdown(toc_md, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
