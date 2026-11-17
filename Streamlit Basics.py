import streamlit as st
import pandas as pd


x = (1,2,3,4,5,6,7,8,9,10)
y = ("A","B","C","D","E","F","G","H","I","J")
z = pd.DataFrame(x,y)
print(z)
st.dataframe(z)


st.title("This is Tanuverma.official")
st.header("Data Scientist")
st.subheader("From Chhattisgarh")
st.text("I'm sharing my bio as a employee in behalf of xyz company .")
st.markdown("### link")


st.success("success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("try dividing by 0")
st.exception(exp)
#exp = st.text("Hello World")
#st.write(exp)

st.write("I'm writing")
st.write(range(10))


import pillow as p 
