import streamlit as st

#steps

from streamlit_extras.steps import *

s1,s2 = st.columns((1,3))

with s1:
    s = steps(["Account setup","Preferences","Confirmation"],
    icons = range(1,4),
    key='s1',
              )

with s2:
    with s[0]:
        st.text_input("Enter your name" , key='name')
        if st.button("Next", key='next0'):
            s.next()

    with s[1]:
        st.selectbox("Select your favorite option",["Light","Dark"])
        if st.button("Previous",key='previous'):
            s.previous()
        if st.button("Next", key='next1'):
            s.next()

    with s[2]:
        st.success("All Done!! , You are all set!")
        if st.button("Reset", key='abcd'):
            s.reset()

# sigma graph

from streamlit_extras.sigma_graph import *

st.write(" ### Basic networking graph ")
sg = {"nodes":[
    {"id":"Tanu","label":"Tanu","size":15,"color":"green"},
    {"id":"Pankaj","label":"Pankaj","size":9,"color":"red"},
    {"id":"Ketan","label":"Ketan","size":19,"color":"blue"},
    {"id":"Taniya","label":"Taniya","size":12,"color":"yellow"},
          ],
     "edges":[
         {"source":"Tanu","target":"Taniya","id":"e1"},
         {"source":"Taniya","target":"Ketan","id":"e2"},
         {"source":"Pankaj","target":"Taniya","id":"e3"},
         {"source":"Pankaj","target":"Ketan","id":"e4"},
         {"source":"Pankaj","target":"Tanu","id":"e5"},
     ],
}

sigma_graph(sg,height=400)

