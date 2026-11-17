import streamlit as st

#3D viewer
from streamlit_extras.three_viewer import *

st.write(" Basic 3D demo viewer with sample data")
model = (r"C:\Users\TANU\Downloads\jarethcruz38819hs_essex.glb")
three_viewer(model,height=400, key="three_viewer")
st.caption("drag it to see in 3D mode")

#word importance
from streamlit_extras.word_importances import *
text = "Tanu Verma is a very lazy girl "
text1 = format_word_importances(
          words=text.split(),
          importances=[0.1, 0.2,-1, 0, 0.8, 0.9, 0.1,],
         )

st.html(text1)