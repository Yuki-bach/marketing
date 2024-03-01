import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from utils.dataloader import load_csv_files


def display_order_count_by_state():
    # Load data
    df_dict = load_csv_files()
    df_customers = df_dict["df_customers"]
    df_customers_by_state = df_customers["customer_state"].value_counts()

    # matplotlib
    __plot(df_customers_by_state)

    # streamlit
    st.title("Data by Customer State")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.pyplot(plt.gcf())
    with col2:
        display_state_names()


def __plot(df_customers_by_state):
    plt.figure(figsize=(8, 6))
    df_customers_by_state.plot(kind="bar", color="skyblue")
    plt.xticks(rotation=45)
    plt.xlabel("Customer State")
    plt.ylabel("Count")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
    # memo: I tried to use st.bar_chart, but the state is alphabetically sorted.


def display_state_names():
    data = {
        "State": [
            "SP",
            "SC",
            "MG",
            "PR",
            "RJ",
            "RS",
            "PA",
            "GO",
            "ES",
            "BA",
            "MA",
            "MS",
            "CE",
            "DF",
            "RN",
            "PE",
            "MT",
            "AM",
            "AP",
            "AL",
            "RO",
            "PB",
            "TO",
            "PI",
            "AC",
            "SE",
            "RR",
        ],
        "State Name": [
            "São Paulo",
            "Santa Catarina",
            "Minas Gerais",
            "Paraná",
            "Rio de Janeiro",
            "Rio Grande do Sul",
            "Pará",
            "Goiás",
            "Espírito Santo",
            "Bahia",
            "Maranhão",
            "Mato Grosso do Sul",
            "Ceará",
            "Federal District",
            "Rio Grande do Norte",
            "Pernambuco",
            "Mato Grosso",
            "Amazonas",
            "Amapá",
            "Alagoas",
            "Rondônia",
            "Paraíba",
            "Tocantins",
            "Piauí",
            "Acre",
            "Sergipe",
            "Roraima",
        ],
    }

    df_states = pd.DataFrame(data)
    st.dataframe(df_states, hide_index=True)
