import streamlit as st

#html integration

#1st method

st.html("<h1>This is a Heading</h1>")
st.html("""
      <div style='background-color:#f0f2f6; padding:10px;border-radius:5px;'>
      
            <h2 style='color:red; font-size:80px;'> Heading 2 from streamlit .</h2>
            <p>This is just for research purpose </p>
      
      </div>


      """)
st.html("C:/Users/TANU/Desktop/DATA_SCIENCE/html/portfolio.html")

st.iframe("https://www.icc-cricket.com/tournaments/womens-t20-worldcup-2026",width="stretch",height=900)


#2nd method
st.markdown("centered text using <span style='font-weight:bold;color:green;'>markdown html injection</span>.",unsafe_allow_html=True)

import streamlit as st

# Render HTML by enabling the unsafe flag
st.markdown(
    "Centered text using <span style='font-weight:bold; color:green;'>Markdown HTML Injection</span>.",
    unsafe_allow_html=True
)

st.markdown("<h1 style='color:yellow;'>Tanu this side</h1>",unsafe_allow_html=True)

#3rd method (*** Most Important one)
import streamlit.components.v1 as c
c.html("""
        <h1 style='color:purple;font-size:50px;'>This is a Heading</h1>
        <p>This is just for research purpose </p>
        
        """)
c.iframe("https://www.icc-cricket.com",width="stretch",height=900)
c.iframe("https://getemoji.com/",width="stretch",height=900)

