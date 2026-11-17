import streamlit as st

import page2

home = st.Page("home.py", title="Home", icon = "🏠" )
page1 = st.Page("page1.py", title="Page 1")
page2 = st.Page("page2.py", title="Page 2")
page3 = st.Page("page3.py", title="Page 3")

#mapping
page = st.navigation([home, page1, page2, page3])

page.run()


import pandas as pd

fi = st.file_uploader("Upload your file", type=["csv"] , accept_multiple_files=False)



if fi is not None:
    up = pd.read_csv(fi)
    st.write(up)

    st.success("Your file has been uploaded")

else :
    st.error("Please upload a file")


fs = st.file_uploader("Upload your file", type=["csv"] , accept_multiple_files=True , max_upload_size=109951162)
if fs:
        #.min_upload_size() >= 2*1024*1024):
   # st.write("Your file is too small")

    for i in fs :
        a = pd.read_csv(i)
        #b = a.read().decode("UTF-8")
        st.write(a)
        st.success("Your file has been uploaded")

