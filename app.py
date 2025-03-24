import streamlit as st
import os

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# And the root-level secrets are also accessible as environment variables:

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)

st.title('This is my Hellow World app!')

st.write('Hello World!')

st. header('This is a header with a divider below it')

st.markdown("This is created using st.markdown")

x = st.slider("Choose an x value", 1, 10)
x
