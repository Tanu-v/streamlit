import pandas as pd
import streamlit as st
from plotly.graph_objs.layout.ternary import aaxis
from streamlit.elements.widgets import file_uploader

st.title("Personal Information")
st.warning("Please Provide your personal information for better tips and  suggestions .")
st.sidebar.markdown("Personal Information")


name  = st.text_input("Name")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=10, max_value=100)
phone = st.text_input("Phone Number")
email = st.text_input("Email")
location = st.text_input("Location")
fup = st.file_uploader("Please upload your file here: ", type = ["csv"], accept_multiple_files=True, max_upload_size=1024*1024)

for i in fup :
       c = pd.read_csv(i)
       st.write(c)
       st.success("File uploaded!!")



if st.button("Submit"):
    st.success("Information submitted successfully!")
    st.write(f"Welcome, {name}!")
    st.balloons()
    username = st.text_input("Username: ", max_chars=15 )
    st.write(" your entered username is :",username)
    password = st.text_input("Password: ", max_chars=15, type="password")
    st.write("password length is :",len(password))