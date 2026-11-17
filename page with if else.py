import streamlit as st
import graphviz as vg

#sidebar
st.title("Chatgpt on supreme")

st.sidebar.title("How to cheat")
st.sidebar.header("This is my portfolio")
gen = st.sidebar.radio("Choose your gender:",["Male","Female","Others"])
if gen == "Male" :
    st.write("Welcome to our company sir!")
    st.image(r"C:\Users\TANU\Downloads\gettyimages-2235551984-612x612.jpg")

elif gen == "Female" :
    st.write("welcome to our company Madam!")
    st.image(r"C:\Users\TANU\Downloads\gettyimages-1266802968-612x612.jpg")

else:
    st.write("Welcome to our company Honourable sir/madam!")
    st.image(r"C:\Users\TANU\Downloads\gettyimages-1066143570-612x612.jpg")

#st.write("elif ") , elif inside doubole inverted coma work as a raw data

#
st.sidebar.slider("Pick a number:",0,50,20)
st.sidebar.select_slider("Pick a grade :",["Good","Bad","Excellent"])

con = st.container()
con.write("I am a container with Something special things in it")

st.write("I am a container with Something special things in it")



st.graphviz_chart(''' digraph {Mr.Dhanuk_Lal_Lodhi->Mr.HeeraRam_Verma
                               Mr.HeeraRam_Verma->Tanu_Verma
                               Tanu_Verma->S/N_Tanu_Verma}''')