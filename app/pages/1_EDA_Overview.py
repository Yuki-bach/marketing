from components.sales import display_sales
from components.total_order import display_total_order
from components.payment_type import display_payment_type
from components.ordered_product_category import display_ordered_product_category
from components.payment_amount import display_payment_amount
from components.review_score import display_review_score
from utils.set_favicon import set_favicon


def main():
    set_favicon()
    display_sales()
    display_total_order()
    display_ordered_product_category()
    display_payment_amount()
    display_payment_type()
    display_review_score()


if __name__ == "__main__":
    main()
