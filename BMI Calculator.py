import streamlit as st
import numpy as np

#Slider
#sld = st.slider("Select your age:",min_value=14,max_value=60,value=46)
#st.info(f"Your age is: {sld} ")

#BMI calculator
st.title("BMI Calculator")
height = st.number_input("Enter your height in cm:")
st.write("Your height is:",height)
weight = st.number_input("Enter your weight in kg:" , format="%.2f")
st.write("Your weight is:",weight)

h = height ** 2
#st.write("Your weight is:",h)

w = weight * 10000
#st.write("Your height is:",w)

bmi = w / h
st.write("Your BMI is:",bmi)

if bmi < 18.5:
    st.write("Your Underweight")

elif 18.5<bmi < 25:
    st.write("You are fit")

else:
    st.write("You are Overweight")


#File upload
st.file_uploader("Upload a photo")

# Colorpicker
st.color_picker("Select a color")


# Discription text area
st.text_area("Enter a message")

# For date and time
st.date_input("Enter a date")
st.time_input("Enter a time")

#baloon sender
if st.button("Click me"):
    st.balloons()

    st.subheader("Progress")
    st.progress(10)
import time
st.subheader("Wait the execution")
with st.spinner("Wait for it"):
    time.sleep(10)