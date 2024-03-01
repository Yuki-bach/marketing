from components.sales import display_sales
from components.order_date import display_order_date
from components.payments import display_payments
from components.ordered_product_category import display_ordered_product_category


def main():
    display_ordered_product_category()
    display_sales()
    display_order_date()
    display_payments()


if __name__ == "__main__":
    main()
