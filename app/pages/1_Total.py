from components.sales import display_sales
from components.order_date import display_total_order
from components.payment_type import display_payment_type
from components.ordered_product_category import display_ordered_product_category
from components.payment_amount import display_payment_amount


def main():
    display_sales()
    display_total_order()
    display_ordered_product_category()
    display_payment_amount()
    display_payment_type()


if __name__ == "__main__":
    main()
