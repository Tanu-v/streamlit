import streamlit as st


#Jason editor

from streamlit_extras.json_editor import *
st.write("This is a editable json file.")
sample_data = {"Name":"John Doe",
               "Age":32,
               "Gender":"Male",
               "Email":"john@gmail.com",
               "tags":["Developer","Python","Streamlit"],
               "Address":{"street":"123 Main st",
                          "City":"Delhi",
                          "country":"India"},
               }
result = json_editor(sample_data,
                     name="User",
                     collapsed=False,
                     editable=True,
                     key="json_edit",

                     )
st.write(" **Current data** ")
st.json(result["data"])