import streamlit as st

#Homerwork03 : Customer Feedback form for Tanlit Company

st.title("Tanlit Pvt. Ltd.")
st.header("Customer Feedback")

q1 = st.radio("1.  Did our staff greet you in a friendly manner?",["Yes","No"])

q2 = st.radio("2.  Did our staff answer your all your questions?",["Yes","No"])

q3 = st.radio("3. Did our staff able to resolve your issue or concern?", ["Yes","No"])

q4 = st.radio("4.  Please rate your overall customer experience",["Excellent","Above Average","Average","Below Average","Poor"])

q5 = st.text_input("5. Please tell us how can we make your experience better")

q6 = st.radio("6. How likely would you recommend our products to your friends or family members?",["Not at all", "Maybe", "Extremely Likely"])

q7 = st.radio("7.  Please rate the quality of the product", ["Very high quality","Somewhat high quality","Neither high or low","Low quality","Very low quality"])

q8 = st.radio("8.  Please rate the quality of the product",["Very high quality","Somewhat high quality","Neither high Neither low","Low quality","Very low quality"])

q9 = st.text_input("9. Please tell us how can we improve our products")

q10 = st.text_input("10. Do you have any other comments, questions or concerns?")

st.header("Customer Information")

st.text_input("1. Customer Name",["Please Enter Your Name"])

st.text_input("2. Customer Address",["Please Enter Your Address"])

st.text_input("3. Customer City",["Please Enter Your City"])

st.text_input("4. Customer Zip Code",["Please Enter Your Zip Code"])

st.text_input("5. Customer Phone Number",["Please Enter Your Phone Number"])

st.text_input("6. Customer Email",["Please Enter Your Email"])

st.text_input("7. Customer Gender",["Please Enter Your Gender"])

st.text_input("8. Customer Age",["Please Enter Your Age"])

#st.button("Submit")
if st.button("Submit"):
    st.text("Thankyou for submitting your Valueable Feedback!")