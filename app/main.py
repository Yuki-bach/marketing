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

    st.header("Dataset")
    st.markdown(
        """
    [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
      > The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. We also released a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.
    """
    )


if __name__ == "__main__":
    main()
