import streamlit as st
import os

# Ask the user for username and password
username = st.text_input("Enter your username")
password = st.text_input("Enter your password", type="password")

# Validate credentials
if username == st.secrets["valid_username"] and password == st.secrets["valid_password"]:
    st.success("Nice work, login successful!")
else:
    st.error("Sorry, invalid username or password")

st.title('This is my Hello World app!')

st.write('Helloooooo World!')

st. header('This is a header with a divider below it')

st.markdown("This is created using st.markdown")

x = st.slider("Choose an x value", 1, 10)
x
