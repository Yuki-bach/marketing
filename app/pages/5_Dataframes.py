import pandas as pd
import streamlit as st
from dataloader import load_csv_files


def main():
    df_dict = load_csv_files()

    st.balloons()
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
        st.subheader("Summary")
        df_summary = resumetable(df)
        st.dataframe(df_summary, height=200)
        st.subheader("Data")
        st.dataframe(df, height=200)
        st.write(f"Shape: {df.shape}")


def resumetable(df):
    summary = pd.DataFrame(df.dtypes, columns=["dtypes"])
    summary = summary.reset_index()
    summary["Name"] = summary["index"]
    summary = summary[["Name", "dtypes"]]
    summary["Missing"] = df.isnull().sum().values
    summary["Uniques"] = df.nunique().values
    summary["First Value"] = df.loc[0].values

    return summary


if __name__ == "__main__":
    main()
