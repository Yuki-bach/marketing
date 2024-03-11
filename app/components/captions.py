import streamlit as st


# EDA Overview
def cap_total_sales():
    text = """
        This bar chart displays the total sales and total count of orders overall by each month of the year 09/2016 to 10/2018. Due to some missing values in the data, some months have a very low or no number for the value. The Brazilian real (BRL) is the official currency used in Brazil, and the representation of it is R$. There was a significant decline observed from August 2018 to September 2018, which could potentially be attributed to data noise. To facilitate a more accurate comparison between 2017 and 2018, it is advisable to focus on the data pertaining to orders placed from January through August for both years.
    """
    st.write(text)


def cap_total_order_per_week():
    text = """
        The bar chart illustrates the distribution of total orders across different weekdays, encompassing all orders recorded over the entire duration of the dataset. Each bar represents the cumulative count of orders placed on a specific weekday. Surprisingly, it was observed that there were variations in the number of orders based on the day of the week, suggesting the potential inclusion of the day of the week as a feature in the analysis.
    """
    st.write(text)


def cap_total_order_per_time():
    text = """
        This bar chart shows the number of orders placed during a specific time of the day. These account for all the order data in the dataset. The specific time range for the timing is set above.
    """
    st.write(text)


def cap_top10_ordered_product_categories():
    text = """
        The bar graph highlights the top 10 product categories out of a total of 71, presenting the count of sales on the y-axis against the respective product categories on the x-axis. This visualization offers a succinct overview of the most popular product categories based on sales volume.
    """
    st.write(text)


def cap_payment_amount():
    text = """
        The bar chart showcases the distribution of payment values by frequency, offering a visual representation of the frequency distribution across different payment value ranges. This is complemented by a box plot, providing a concise summary of the payment amount's central tendency, dispersion, and presence of outliers within the dataset.
    """
    st.write(text)


def cap_payment_type():
    text = """
        This pie chart shows the percentage of each payment type used. The different payment types are credit cards, boleto, debit card, vouchers, and others. Boleto is a payment method used in Brazil that is cash-based. Instead of directly paying with cards or bank accounts, a shopper can create a boleto to pay with, using cash, vouchers, or card.
    """
    st.write(text)


def cap_evolution_of_payment_type():
    text = """
        The multiple line graph tracks the progression of various payment types—including boleto, credit card, debit card, vouchers, and undefined—over time. Each line represents the temporal evolution of a specific payment method, allowing for a comparative analysis of their respective usage trends.
    """
    st.write(text)


def cap_evolution_of_payment_type_as_percent():
    text = """
        As indicated by the previous plot, the data for the first and last 2-3 months is extremely limited, so it will be disregarded. Excluding those, the proportions of payment types have remained relatively unchanged. This suggests that there hasn’t been a significant shift in customer payment type preferences over the course of a year and a half, which is not particularly surprising.
    """
    st.write(text)


def order_price_by_payment_type():
    text = """
        The whisker box plot visually presents the distribution of order prices across different payment types, providing insights into the variability and central tendency of order prices within each payment method category. By displaying key statistical metrics such as median, quartiles, and outliers, the box plot aids in identifying any significant disparities or trends in order pricing across various payment methods.
    """
    st.write(text)


def cap_distribution_of_review_score():
    text = """
        The bar chart illustrates the distribution of review scores, offering a comprehensive overview of the frequency of different rating scores assigned by customers. Each bar represents a specific rating score, ranging from the lowest to the highest possible rating. This visualization enables the assessment of the distribution of customer sentiments towards the products or services, highlighting any prevailing trends or patterns in the feedback received. Additionally, it provides valuable insights into the overall satisfaction levels of customers based on their review scores.
    """
    st.write(text)


# EDA By State
def cap_order_count_by_customer_state():
    text = """
        The bar chart displays the order count categorized by the customer state of Brazil. Each bar represents a specific state, showcasing the volume of orders originating from customers in that particular region. This visualization offers insights into the geographical distribution of orders across different states within Brazil, providing valuable information about the regional demand for products or services.
    """
    st.write(text)


def cap_total_sales_by_state():
    text = """
        The bar chart presents the total sales generated by customer state, offering a visual representation of revenue distribution across different regions of Brazil. Each bar corresponds to a specific state, depicting the aggregate sales value attributed to customers residing in that particular area.
    """
    st.write(text)


# EDA by Product Category
def cap_order_count_by_product_category():
    text = """
        The horizontal bar chart dynamically visualizes order counts by product category, offering flexibility through a slider control to adjust the number of categories displayed. Categories are arranged in descending order based on the number of orders, enabling easy identification of the most popular product categories.
    """
    st.write(text)


def cap_dist_of_review_scores_for_product_category():
    text = """
        The bar chart presents the distribution of review scores tailored to a specific product category, offering insights into customer sentiments and satisfaction levels within that category. Each bar corresponds to a distinct review score, providing a visual representation of the frequency or distribution of ratings received by products within the selected category.
    """
    st.write(text)


# Map
def cap_map_customers():
    text = """
        The interactive map of Brazil provides a visualization of population density based on customer distribution, offering flexibility to display data either by state or zip code prefix. Users can seamlessly switch between these options to explore customer concentration patterns at different geographical levels. The map supports zoom functionality, allowing users to zoom in for a closer examination of specific regions or zoom out for a broader perspective. Hovering over individual circles on the map reveals additional information, such as the corresponding state or zip code prefix, along with the count of customers associated with that geographic area.
    """
    st.write(text)


def cap_map_sellers():
    text = """
        The interactive map of Brazil provides a visualization of seller distribution, offering users the option to explore data either by state or zip code prefix. Users can effortlessly switch between these options to analyze seller concentration patterns at various geographical levels. The map supports zoom functionality, enabling users to zoom in to focus on specific regions or zoom out for a broader overview. When hovering over individual circles on the map, users can view additional information such as the corresponding state or zip code prefix, along with the count of sellers operating within that geographic area.
    """
    st.write(text)


def cap_population_density():
    text = """
        This visual likely illustrates the density of population in different regions of the country, providing a graphical representation of where people are more densely concentrated and where population is sparser. Darker shades of green indicate areas with higher population density, while lighter shades represent regions with lower population density.
    """
    st.write(text)


# RFM
def cap_recency():
    text = """
        The bar graph illustrates the recency distribution as part of an RFM (Recency, Frequency, Monetary) analysis. With a slider allowing for adjustment of the number of bins, the graph displays the frequency of customers based on their recency in days. The y-axis represents the frequency of customers falling within each recency bin, while the x-axis denotes the recency in days.
    """
    st.write(text)


def cap_frequency():
    text = """
        The bar graph visualizes the frequency distribution derived from an RFM (Recency, Frequency, Monetary) analysis. The frequency plot presented indicates a highly skewed distribution of customer transactions towards the lower frequency range. The most noticeable aspect of the distribution is that the majority of customers have only a single transaction.The data highlights the potential need for strategies to increase customer retention and encourage repeat purchases.
    """
    st.write(text)
