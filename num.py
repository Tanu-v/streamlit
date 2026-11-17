import streamlit as st


st.header("NUMBERS")
st.info(" *Numbers for kids to learn* .")
st.sidebar.markdown(" :rainbow[Numbers] 🔢")

c,d =st.columns(2)

with c:
    st.metric("One", value=1, border=True)
    st.metric("Three", value=3, border=True)
    st.metric("Five", value=5, border=True)
    st.metric("Seven", value=7, border=True)
    st.metric("Nine", value=9, border=True)
    st.metric("Eleven", value=11, border=True)
    st.metric("Thirteen", value=13, border=True)
    st.metric("Fifteen", value=15, border=True)
    st.metric("Seventeen", value=17, border=True)
    st.metric("Nineteen", value=19, border=True)

with d:
    st.metric("Two", value=2, border=True)
    st.metric("Four", value=4, border=True)
    st.metric("Six", value=6, border=True)
    st.metric("Eight", value=8, border=True)
    st.metric("Ten", value=10, border=True)
    st.metric("Twelve", value=12, border=True)
    st.metric("Fourteen", value=14, border=True)
    st.metric("Sixteen", value=16, border=True)
    st.metric("Eighteen", value=18, border=True)
    st.metric("Twenty", value=20, border=True)

st.image("https://www.dreamlandpublications.com/wp-content/uploads/2023/01/9788184510461_1-scaled-1.jpg")

st.success(" Here's a video from where you can learn :- ")
st.video("https://youtu.be/D0Ajq682yrA")
st.video("https://youtu.be/x6D51-pz2A4")




