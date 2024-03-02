# Used to get the headers for the EDA page
def get_eda_headers():
    headers = [
        {"id": "total-sales", "title": "Total Sales"},
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

    return headers
