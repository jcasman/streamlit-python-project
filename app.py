import streamlit as st

st.title('This is my Hellow World app!')

st.write('Hello World!')

st. header('This is a header with a divider below it')

st.markdown("This is created using st.markdown")

x = st.slider("Choose an x value", 1, 10)
x
