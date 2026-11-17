import streamlit as st
import pandas as pd
import numpy as np

# Homework04 : HR questions with personal information form

# Question section

st.title("Arithmetic Bix")
st.header("Recruitment Event Registration Form")
st.info(" Please fill out this form for joining our Company")

st.header("Questions section")
st.warning(" Please answer all the questions for now")

q1 = st.text_area("1. Tell me About Yourself?","Enter your answer here")

q2 = st.text_area("2. Why should I hire you?","Enter your answer here")

q3 = st.text_area("3. What do you do?","Enter your answer here")

q4 = st.text_area("4. What are your strengths and weaknesses?","Enter your answer here")

q5 = st.text_area("5. Why do you want to work at our company?","Enter your answer here")

q6 = st.text_area("6. How do you feel about working nights and weekends?","Enter your answer here")

q7 = st.text_area("7. How do you feel about working nights and weekends?","Enter your answer here")

q8 = st.text_area("8. Are you willing to relocate or travel?", "Enter your answer here")

q9 = st.text_area("9. Where do you see yourself five years from now?","Enter your answer here")

q10 = st.text_area("10. How much salary do you expect?","Enter your answer here")

st.header("Personal Information")
st.info(" Please fill out this form for personal information")

st.text_input(" Full Name",["Please Enter Your Full Name here"])

st.text_input(" Email Address",["Please Enter Your Email address here"])

st.number_input("Phone Number")

# Position Information
st.header("Position Information")
st.info(" Please fill out this form for position information")

st.multiselect("Enter the job title you are interested in?",["Data Analyst","IT manager","DevOps Engineer","Software Engineer"])

st.date_input("Enter your desired start date")

st.selectbox("Enter your salary expectation",["15000","40000","35000","70000","90000"])

#Educational Information
st.header("Education Information")
st.info(" Please fill out this form for education information")

st.subheader("10th certification")

st.text_input("Enter the name of school you passed 10th from")

st.date_input("Enter the date you pass above degree")

st.file_uploader("Upload your 10th certificate")

st.subheader("12th certification")

st.text_input("Enter the name of school you passed 12th from")
st.text_input("Enter the date you pass above degree")
st.file_uploader("Upload your 12th certificate")



st.selectbox("College degree",["Yes","No"])
if st.selectbox("College degree",["Yes"]):
    st.text_input("Enter your college name")
    st.date_input("Enter your college passed date")
    st.file_uploader("Upload your college degree")
    st.file_uploader("Upload your resume")
    st.file_uploader("Upload your Passport size photo")
    st.file_uploader("Upload your signature")

    #st.button("Submit")




else:
    st.warning("Your not Eligible for this form")



if st.button("Submit"):
    st.write("Thank you for your interest")
    st.balloons()


