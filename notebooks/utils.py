import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

def get_df_description(df, description_json_df):
    # Get dtype series, and convert it to DataFrame
    dtype_series = df.dtypes
    dtype_df = dtype_series.reset_index()
    dtype_df.columns = ['column', 'dtype']
    dtype_df['dtype'] = dtype_df['dtype'].astype(str)

    # Calculate missing values for numerical columns
    missing_values = df.select_dtypes(include=[np.number]).isnull().sum().reset_index()
    missing_values.columns = ['column', 'missing_values']
    # Merge dtype and missing values information
    dtype_df = pd.merge(dtype_df, missing_values, on='column', how='left')

    # Merge
    merged_df = pd.merge(dtype_df, description_json_df, on='column', how='left')
    final_df = merged_df[['column', 'dtype', 'missing_values', 'source', 'description']]
    final_df['missing_values'] = final_df['missing_values'].fillna(0).astype(int)

    return final_df


def standardize(df):
    if df.select_dtypes(include=[np.number]).shape[1] != df.shape[1]:
        raise ValueError('Dataframe contains non-numeric columns')

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    df_standardized = pd.DataFrame(df_scaled, columns=df.columns)
    return df_standardized


def normalize(df):
    if df.select_dtypes(include=[np.number]).shape[1] != df.shape[1]:
        raise ValueError('Dataframe contains non-numeric columns')
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)
    df_normalized = pd.DataFrame(df_scaled, columns=df.columns)
    return df_normalized
