import pandas as pd
import streamlit as st
from dataloader import load_csv_files


def main():
    df_dict = load_csv_files()

    st.title("DataFrames")
    display_df_shapes(df_dict)
    display_dfs(df_dict)


def display_df_shapes(df_dict):
    st.write("There are 8 dataframes in this dataset.")
    df_shapes = {df_name: df.shape for df_name, df in df_dict.items()}
    df_shapes = pd.DataFrame(list(df_shapes.items()), columns=["DataFrame", "Shape"])
    st.table(df_shapes)


def display_dfs(df_dict):
    for df_name, df in df_dict.items():
        st.header(df_name)
        st.dataframe(df)


if __name__ == "__main__":
    main()
