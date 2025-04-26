import streamlit as st

st.title("Interactive Streamlit App")

name = st.text_input("Enter your name:", "123")
age = st.slider("Select your age:", 1, 100, 25)

if st.button("Submit"):
    st.title(f"Hello, {name}!")
    st.title(f"You are {age} years old.")