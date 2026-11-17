import streamlit as st
import pandas as pd
import numpy as np

# Fuel Consumption Estimation
st.title("Fuel Consumption Estimator")
st.subheader("Problem: Calculate fuel efficiency.")

dis = st.number_input("Enter the distance your vehicle travelled: ")

fuel = st.number_input("Enter the fuel consumed in liters: ",min_value=0.1)

mil = dis / fuel
st.write("Your Vehicles Mileage in km/l is : ", mil)
# tips for how to improve mileage , add if mileage is low high or average

#Cricket Strike Rate  Calculator
st.title("Cricket strike rate Calculator")
st.subheader("Strick rate efficiency")

r = st.number_input("Enter the run you scored : ")
st.write(f"you made {r} runs")

b = st.number_input("Enter the number of balls in you scored above runs : ", min_value=1)
st.write(f"you made {r} runs in {b} balls")

Sr = r * 100 / b

st.write(f"your strick rate is {Sr} ")

#batting type agressive bating or you need  to do good batting , make correction , slow player , how to improve strick rate

