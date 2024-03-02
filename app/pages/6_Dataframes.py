import os
import pandas as pd
import streamlit as st
from PIL import Image
from utils.dataloader import load_csv_files
from utils.image_utils import get_image
from utils.set_favicon import set_favicon


def main():
    set_favicon()
    df_dict = load_csv_files()

    st.balloons()
    st.title("DataFrames")
    __display_data_schema()
    __display_df_shapes(df_dict)
    __display_dfs(df_dict)


def __display_data_schema():
    image = get_image("../images/data_schema.png")
    st.image(image)


def __display_df_shapes(df_dict):
    st.write("There are 8 dataframes in this dataset.")
    df_shapes = {df_name: df.shape for df_name, df in df_dict.items()}
    df_shapes = pd.DataFrame(list(df_shapes.items()), columns=["DataFrame", "Shape"])
    st.table(df_shapes)


def __display_dfs(df_dict):
    for df_name, df in df_dict.items():
        st.header(df_name)
        st.subheader("Summary")
        df_summary = __resumetable(df)
        st.dataframe(df_summary, height=200)
        if df_name == "df_customers":
            __display_customer_text()
        st.subheader("Data")
        st.dataframe(df, height=200)
        st.write(f"Shape: {df.shape}")


def __resumetable(df):
    summary = pd.DataFrame(df.dtypes, columns=["dtypes"])
    summary = summary.reset_index()
    summary["Name"] = summary["index"]
    summary = summary[["Name", "dtypes"]]
    summary["Missing"] = df.isnull().sum().values
    summary["Uniques"] = df.nunique().values
    summary["First Value"] = df.loc[0].values

    return summary


def __display_customer_text():
    st.markdown(
        """
        Caution
        - `customer_id` is key to the orders dataset. Each order has a unique customer_id.
        - `customer_unique_id` is unique identifier of a customer.
    """
    )


if __name__ == "__main__":
    main()
