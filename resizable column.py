import streamlit as st

#resizable column

from streamlit_extras.resizable_columns import *
st.write("Resizable Border")

rc = resizable_columns(3, border=True , key="3col")
with rc[0]:
    st.metric("profit",12234892000,"8%")

with rc[1]:
    st.metric("profit",11000,"7%")

with rc[2]:
    st.metric("profit",10000,"6%")

rc1 = resizable_columns(3, border=True, key="col3")
with rc1[0]:
    st.image(r"C:\Users\TANU\Downloads\images (7).jpg")

with rc1[1]:
    st.image(r"C:\Users\TANU\Downloads\ChatGPT Image Jul 5, 2026, 01_50_35 PM.png")

with rc1[2]:
    st.image(r"C:\Users\TANU\Downloads\ChatGPT Image Jul 4, 2026, 12_26_39 PM.png")

l,r = resizable_columns([1,2],key="2col")
with l:  #not resizable
    lt = st.radio("Choose the option:",["Chart","Table","Summery"])
    st.write(f"selected:{lt}")

with r: #resizable
    st.write("Main content area")
    st.bar_chart({"values":[2,5,9,5,6,9,8,24,56,78,9]})


