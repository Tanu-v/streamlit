import altair

import streamlit as st

from streamlit_extras.bottom_container import *

st.write("This is my container")

with bottom():
    st.write("This is a bottom container")
    st.text_input("Enter some text")


st.write("""LinkedIn is a global professional social networking service designed to connect the world’s professionals, facilitate career development, and support business-to-business (B2B) marketing.  Launched in 2003 by Reid Hoffman and acquired by Microsoft in 2016 for $26.2 billion, it is currently the largest professional network with over 1.2 billion registered members. 

The platform serves three primary functions:

Professional Networking: Users create detailed profiles similar to resumes to showcase work history, education, and skills, allowing them to connect with colleagues, recruiters, and industry peers. 
Job Search and Recruitment: It provides a comprehensive job board for seekers and tools for employers and recruiters to post vacancies and identify potential candidates. 
Content and Learning: Members share industry insights, articles, and videos to build personal brands or company visibility, while LinkedIn Learning offers online courses for skill development. 
Unlike general social media, LinkedIn maintains a professional tone focused on career growth and business connections.  While basic access is free, the company generates revenue through premium subscriptions, advertising, and Talent Solutions for recruiters.  It is available in multiple languages and is accessible via desktop and mobile apps, though it remains banned or restricted in countries such as Russia, Kazakhstan, and China.""")
#chart container

from streamlit_extras.chart_container import *
cc = get_random_data()
with chart_container(cc):
    st.write("This is a chart container")
    st.write("This is a cool chart")
    st.area_chart(cc)

#Chart Annotation

from streamlit_extras.chart_annotations import *
data: pd.DataFrame = get_data()
chart: altair.TopLevelMixin=get_chart(data=data)
chart += get_annotations_chart(annotations=[
        ("Mar 01, 2008", "Pretty good day for GOOG"),
        ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"),
        ("Nov 01, 2008", "Market starts again thanks to..."),
        ("Dec 01, 2009", "Small crash for GOOG after..."),
    ],)
st.altair_chart(chart, width="stretch")

#customize running
from streamlit_extras.customize_running import *
click = st.button("Observe where the running widget is now")
if click:
    center_running()
    time.sleep(10)

#Dataframe explorer ui
from streamlit_extras.dataframe_explorer import *

dataframe = generate_fake_dataframe(size=500,cols="dfc",col_names=["Id","Name","Salary"],seed=1)
st.dataframe(dataframe)
st.markdown("---")
filtered_df = dataframe_explorer(dataframe,case=False)

st.dataframe(filtered_df, width="stretch")

#Jupiter embedding
import streamlit.components.v1 as components

from streamlit_extras.jupyterlite import *

jupyterlite(1500,1600)
st.button("Runcell")

#iframe is a different one
st.markdown("---")
components.iframe("https://jupyter.org/",width=1000,height=1000,scrolling=True)

#keyboard text
from streamlit_extras.keyboard_text import *
st.markdown("---")
load_key_css()
key("🪟+k")









