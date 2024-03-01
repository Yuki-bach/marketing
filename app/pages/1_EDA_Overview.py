from components.sales import display_sales
from components.total_order import display_total_order
from components.payment_type import display_payment_type
from components.ordered_product_category import display_ordered_product_category
from components.payment_amount import display_payment_amount
from components.review_score import display_review_score
from utils.set_favicon import set_favicon
import streamlit as st


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
    headers = [
        {"id": "total-order", "title": "Total Order"},
        {"id": "total-order-per-weekday", "title": "Total Order per Weekday"},
        {"id": "total-order-per-time-of-day", "title": "Total Order per Time of Day"},
        {
            "id": "top-10-ordered-product-categories",
            "title": "Top 10 Ordered Product Categories",
        },
        {"id": "payment-amount", "title": "Payment Amount"},
        {"id": "payment-type", "title": "Payment Type"},
        {"id": "evolution-of-payment-type", "title": "Evolution of Payment Type"},
        {"id": "order-price-by-payment-type", "title": "Order Price by Payment Type"},
        {
            "id": "distribution-of-review-scores",
            "title": "Distribution of Review Scores",
        },
    ]
    toc_md = "<ul>" + "".join(
        f'<li><a href="#{header["id"]}">{header["title"]}</a></li>'
        for header in headers
    ) + "</ul>"
    with st.container(border=True):
        st.subheader("Table of Contents")
        st.markdown(toc_md, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
