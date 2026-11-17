import streamlit as st

#Graph segment

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#g = np.random.normal(1,2,size=20)

#fig,ax = plt.subplots()

#ax.hist(g, bins=6)

#st.pyplot(fig)

#st.line_chart(g)

#st.bar_chart(g)

# Area chart
#st.area_chart(g)

df = pd.DataFrame(np.random.randn(10,2), columns=['x', 'y'])
st.line_chart(df)

st.bar_chart(df)

st.area_chart(df)

st.scatter_chart(df)

#st.bokeh_chart(df)

#st.streamlit-bokeh(df)   not working

#Graphviz
import streamlit as st
import graphviz


import graphviz
print(graphviz.__file__)
import streamlit as st
import graphviz

# Initialize the diagram
gf = graphviz.Digraph()

# Define the family/relationships tree
#gf.edge("Mr. Dhanuk Lal Lodhi", "Mr. HeeraRam Verma")
#gf.edge("Mr. HeeraRam Verma", "Ms. Tanu Verma")
#gf.edge("Ms. Tanu Verma", "Ms. Tanu Verma S/O")
#gf.edge("Mr. HeeraRam Verma", "Ms. Taniya Verma")
#gf.edge("Mr. HeeraRam Verma", "Ms. Neha Verma ")
#gf.edge("Mr. HeeraRam Verma", "Mr. Ketan Verma")
#gf.edge("Mr. Dhanuk Lal Lodhi", "Mr. shiv Verma")
#gf.edge("Mr. Dhanuk Lal Lodhi", "Mr. Ketan Verma")
#gf.edge("Mr. Dhanuk Lal Lodhi", "Ms. Tanu Verma S/O")
#gf.edge("Ms. Tanu Verma S/O", "Mr. Dhanuk Lal Lodhi")

# Display the chart in your Streamlit browser app
#st.graphviz_chart(gf)


st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

