import streamlit as st
import pandas as pd

df = pd.read_csv('purchases.csv', sep = ';')
st.title("Анализ данных по покупкам")
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.header("Статическая таблица")
    st.table(df)
with tab2:
    st.header("Интерактивная таблица")
    st.dataframe(df)
with tab3:
    st.title("Interactive Streamlit App")

    name = st.text_input("Enter your name:", "123")
    age = st.slider("Select your age:", 1, 100, 25)

    if st.button("Submit"):
        st.title(f"Hello, {name}!")
        st.title(f"You are {age} years old.")