import streamlit as st

#Todo list

from streamlit_extras.stodo import *

#to_do("I am doing Homework","I am doing Housework")
to_do([(st.write, "I have to sleep to")],"I have to go to sleeping",)
to_do([(st.write, "I have to dance to")],"I have to go to sweeping",)
to_do([(st.write, "I have to run to")],"I have to go to running ",)
to_do([(st.write, "I have to clean to")],"I have to go to cleaning ",)

#divider
st.markdown("---")

#toggle button

from streamlit_extras.stoggle import *

stoggle("Click me","I am clickable")

st.markdown("---")
st.caption("@2026 Tata Groups | Titan | All Rights Reserved")
st.markdown("---")



