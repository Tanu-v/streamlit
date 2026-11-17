import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Homework09 : All charts practice with different types of data

st.title("Charts with Data")
st.subheader("You can see different types of chats with different types of data here")

st.sidebar.title("Charts with Data")
st.sidebar.header("Select and see the charts")
st.sidebar.subheader("choose one from here to see")

ds = st.sidebar.radio("Choose a data set type:", ["ds1", "ds2", "ds3"])

if ds == "ds1":

 # Data 1 :
   st.header("Data set 1")

   d1 = np.random.normal(2,3,size=100)

   fig, ax = plt.subplots()
   st.subheader("Histogram of data")
   ax.hist(d1, bins=6)

   st.pyplot(fig)
   st.subheader("Line chart of data")
   st.line_chart(d1)
   st.subheader("Bar chart of data")
   st.bar_chart(d1)
   st.subheader("Area chart of data")
   st.area_chart(d1)
   st.subheader("Scatter chart of data")
   st.scatter_chart(d1)

# Other charts are not working

#st.plotly_chart(d1)

#st.pydeck_chart(d1)

#st.vega_lite_chart(d1)
#st.scatter_chart(d1)

elif ds == "ds2":
     # Data 2 :
     st.header("Data set 2")
     d2 = pd.DataFrame(np.random.randn(25,3), columns=['x', 'y','z'])
     st.subheader("Line chart of data")
     st.line_chart(d2)
     st.subheader("Bar chart of data")
     st.bar_chart(d2)
     st.subheader("Area chart of data")
     st.area_chart(d2)
     st.subheader("Scatter chart of data")
     st.scatter_chart(d2)

else :

    # Data 3 :
     st.header("Data set 3")
     st.subheader("Data set used ")
     d3 = pd.read_csv(r"C:\Users\TANU\Desktop\DATA_SCIENCE\Power bi\Power bi datasets\School data performance.csv")
     d3
     st.subheader("Area chart of data")
     st.area_chart(d3)
     st.subheader("Line chart of data")
     st.line_chart(d3)
     st.subheader("Bar chart of data")
     st.bar_chart(d3)
     st.subheader("Scatter chart of data")
     st.scatter_chart(d3)