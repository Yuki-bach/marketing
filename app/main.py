import matplotlib.pyplot as plt
import streamlit as st
from cycler import cycler
from utils.set_favicon import set_favicon

# Set color cycle for all plot in this app
plt.rcParams["axes.prop_cycle"] = cycler(
    color=[plt.get_cmap("Set2")(i) for i in range(9)]
)


def main():
    set_favicon()
    st.title("ASU DAT490 Capstone Project")

    st.warning(
        """
        Rendering charts may take some time.
        While 'running' is displayed on the top-right corner, your patience would be appreciated.
        Unexpected behavior or errors may occur.""",
        icon="⚠️",
    )

    st.header("Introduction")
    st.write(
        """
        This exploratory data analysis provides an overview of visualizations that present the key metrics and trends of this dataset.
        This includes the total sales revenue, order volumes, distribution of payment types,
        and the prevalence of different product categories.
        Leveraging the RFM (Recency, Frequency, Monetary) analysis framework,
        it delves deeper into customer behavior, offering insights into transaction recency, frequency, and monetary value.
        The analysis extends beyond national summaries to offer insights at a more detailed level into the distinct dynamics observed within each individual state across Brazil.
        Furthermore, it scrutinizes the sales performance and consumer preferences associated with each specific product category,
        showing insights on variations in demand, pricing strategies, and market trends.

        This dataset is structured as a relational database, consisting of multiple dataset files, each with linking ID codes that connect the information of the products, customers, and sellers among different tables. We merged the ordered items, order payments, order reviews, products, customer information, and seller information into one table. The table contains key information important for analysis, such as product types and descriptions, price, customer location, seller location, and more.
        Although there are many null and repeat values, those will be easy to handle and clean up. For the null values, if it is a quantity, we would place them as 0 as it is possible that there could not be enough information on sales to get the true picture for it. This should not be a problem as most missing values are not in the vital quantity columns. For textual entries, such as review information and dates, we will leave them blank or have a sign indicating nothing as those entries may not be as important to the analysis. As for duplicates, we will remove them from the dataset as it could lead to inaccurate results.

            """)

    st.header("Dataset")
    st.markdown(
        """
    [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
      > The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. We also released a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.
    """
    )


if __name__ == "__main__":
    main()
