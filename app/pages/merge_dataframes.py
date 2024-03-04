import pandas as pd
import streamlit as st
from utils.dataloader import load_csv_files
from utils.set_favicon import set_favicon


def main():
    set_favicon()
    st.title("Merge DataFrames")
    __display_merging_code()

    # merge 8 dataframes
    df_train = __merge_df()
    df_summary = __resumetable(df_train)
    st.write(f"Dataset Shape: {df_train.shape}")
    st.subheader("df_train Summary:")
    st.write(df_summary)


def __display_merging_code():
    st.code(
        """
        # Merge 8 dataframes

        df_train = df_orders.merge(df_customers, on='customer_id', how='inner')
            # df_orders and df_customers have the same row count
        df_train = df_train.merge(df_order_items, on='order_id', how='outer')
            # Order can have multiple items
        df_train = df_train.merge(df_order_payments, on='order_id', how='outer')
            # Order can have multiple payments
        df_train = df_train.merge(df_order_reviews, on='order_id', how='outer')
            # Order can have multiple reviews, while some orders may not have reviews
        df_train = df_train.merge(df_products, on='product_id', how='left')
        df_train = df_train.merge(df_product_category_name, on="product_category_name", how="inner")
        df_train = df_train.merge(df_sellers, on='seller_id', how='left')
        df_train.drop(columns=["product_category_name"], inplace=True)
            # We don't need Portuguese product category name
    """,
        language="python",
    )


def __merge_df():
    df_dict = load_csv_files()
    df_train = df_dict["df_orders"].merge(
        df_dict["df_customers"], on="customer_id", how="inner"
    )  # They have the same row count
    df_train = df_train.merge(
        df_dict["df_order_items"], on="order_id", how="outer"
    )  # Order can have multiple items
    df_train = df_train.merge(
        df_dict["df_order_payments"], on="order_id", how="outer"
    )  # Order can have multiple payments
    df_train = df_train.merge(
        df_dict["df_order_reviews"], on="order_id", how="outer"
    )  # Order can have multiple reviews, while some orders may not have reviews
    df_train = df_train.merge(df_dict["df_products"], on="product_id", how="left")
    df_train = df_train.merge(
        df_dict["df_product_category_name"], on="product_category_name", how="inner"
    )
    df_train = df_train.merge(df_dict["df_sellers"], on="seller_id", how="left")
    df_train.drop(columns=["product_category_name"], inplace=True)
    # We don't need Portuguese product category name
    return df_train


def __resumetable(df):
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
