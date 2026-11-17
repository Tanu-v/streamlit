#Checkbox creation
import streamlit as st

'''
#st.checkbox("")
r =st.checkbox("Select your stream:",["BCA","Bcom","BA","Bsc"])

#radio creation
ra = st.radio("Select your stream:",["BCA","Bcom","BA","Bsc"])

if ra == "BCA":
    st.success("You're Eligible")


elif ra == "Bcom":
    st.success("You're Eligible")
else :
    st.error("you are not Eligible")
'''

# selection box
sel = st.selectbox("Select your Cast:",["OBC","General","ST/SC"])
st.write("Your cast is:",sel)


#Multiple selection box

msel = st.multiselect("Select your localities :",["Indian","Chhattisgarhiya","Maharastrian","Gujrati"])
st.write("Your localities is:",msel)



#button
st.button("Help me")
if st.button("Contact"):
    st.text("9347436731")

#Text Input
name = st.text_input("Enter your name:")

n1 = st.text_input("Enter your name:","Type here")

if st.button("submit"):
    st.text("Thankyou for submitting")

