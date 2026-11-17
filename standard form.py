import pandas as pd
import streamlit as st

import os
#Standard form

from streamlit_extras.specialized_inputs import *

n = st.text_input("Enter your name",)

st.text_input("Enter your text",placeholder="text input")

st.text_input("Enter your text",placeholder="text input",help="Help")

st.text_input("Enter your text",placeholder="password input",type="password",help="I'm going to sleep")

st.chat_input("Chat input t")#placeholder="Chat input")

p = password_input("Enter your password",help="minimum 8 characters",key="basic key")

if p:
    st.caption(f"Lenght: {len(p)} characters.")

e = email_input("Email Address",placeholder="xy@email.com",key="ke",label_visibility="hidden")
if e:
    valid=bool(re.match(r"^[^@]+@[^@]+\.[^@]+$" ,e))
    #Advance validation alternatives [ Ragex pattern] check the presence of @ and .
    #re = regular expression
    if not valid :
        email_input(" Email Address validated",value=e,error="Please enter a valid email address",key="kes")

pn = phone_input("Phone Number",help="Include your country code",placeholder="phone number",key="phone")

u = url_input("URL",placeholder="xyz.com",key="url")

s = search_input("Search",placeholder="search",key="search",label_visibility="collapsed")
if s:
    st.caption(f"Query:{s!r}")

ls = search_input("Live search",placeholder="live search",key="live",keyup=True ,debounce=300)
if ls:
    st.caption(f"Live value :{ls!r}")


sr = money_input("Money",placeholder="Money",key="money",currency="₹")
if sr:
    st.caption(f"Money value :{sr!r}₹")

#specialized text input

specialized_text_input("Gmail",suffix="@gmail.com",placeholder="Gmail",key="gmail",help="Enter your gmail id without '@gmail.com'")

specialized_text_input("Money",prefix="₹",placeholder="Money",key="amount",help="Enter your amount")

age = st.number_input("Age",min_value=5,max_value=100,step=1,key="age")

gen = st.selectbox("Gender",["Male","Female"])

if st.button("Submit"):
    response={"Name": n ,
              "Age": age ,
              "Gender": gen ,
              "Email": e ,
              "Phone no.": pn ,
              "Salary": sr ,
              "Link": u ,
              "Password": p ,
              }
    file_name = "Feedback.csv" # it's not the csv file of the above variable
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)

    else :
        df = pd.DataFrame()

    df = pd.concat([df,pd.DataFrame([response])],ignore_index=True)
    df.to_csv(file_name)
    st.success("Your file is submitted!!")
    st.download_button("Download your file",data=df.to_csv(index=False),file_name='Feedback.csv',mime="text/csv")







