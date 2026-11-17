import streamlit as st
from streamlit_extras.chart_container import get_random_data
from streamlit_extras.chart_container import *
from streamlit_extras.chart_annotations import *
from streamlit_extras.dataframe_explorer import *
import altair
from streamlit_extras.jupyterlite import *
from streamlit_extras.stoggle import *

st.title("📊 :blue[Data Frame]")
st.markdown("---")
st.sidebar.title("📊 :blue[Data Frame]")
st.sidebar.markdown("---")
st.sidebar.image("https://imgs.search.brave.com/nYgy-kv8E8un41779SQud2lbj4AHU-8AVJVEtp_eSsg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMucHJkLmRhdGF3/YXJzLmlvL3N0YXRp/Yy9wcm9qZWN0LXN2/Zy1pY29ucy8xMTAu/c3Zn")
st.warning("""
         A DataFrame is a two-dimensional, labeled data structure commonly used in data science to organize data into rows and columns, similar to a spreadsheet or database table.  It allows for the storage of heterogeneous data types across different columns and provides powerful tools for data manipulation, analysis, and cleaning. 

  :green[Key characteristics include]:

Tabular Structure: Data is arranged in rows (observations) and columns (variables), with each column having a specific name and data type. 
Flexibility: Unlike matrices, DataFrames can hold mixed data types (e.g., integers, strings, dates) within the same structure.
Scalability: Implementations like Apache Spark DataFrames enable processing of large datasets across distributed computing clusters, while libraries like Pandas (Python) and R provide efficient in-memory handling for analysis. 
Schema Definition: Many DataFrame implementations use a schema to define column names and types, ensuring data consistency and enabling optimized query execution. 
""")

#Bottom container
from streamlit_extras.bottom_container import *
with bottom():
    st.sidebar.markdown("---")
    st.caption("@2026 | Made by Tanu Verma")


# iframe
import streamlit.components.v1 as components

st.markdown("---")
components.iframe("https://pandas.pydata.org/docs/reference/frame.html",width=1000,height=500,scrolling=True)
st.markdown("---")

#custom running
from streamlit_extras.customize_running import *
click = st.sidebar.button("Click to Run")
if click:
    center_running()
    time.sleep(20)


sb = st.sidebar.selectbox("Some things about dataframe:-",["Example","Chart_Container","Chart_annotation","Dataframe_explorer"])

if sb == "Example":
    st.header("Example")
    df = get_random_data()
    st.dataframe(df)

#Chart container

elif sb == "Chart_Container":
    st.header(" Dataframe inside a chart container ")
    gd = get_random_data()
    if chart_container(gd):
        st.info("This is a Dataframe inside chart container")
        st.area_chart(gd)

#Chart annotation
elif sb == "Chart_annotation":
    st.header("Chart_annotation of dataframe")
    data: pd.DataFrame = get_data()
    chart: altair.TopLevelMixin = get_chart(data=data)
    chart += get_annotations_chart(annotations=[
        ("Mar 01, 2006", "It something wrong here"),
        ("Dec 01, 2007", "What do you think of here"),
        ("Nov 01, 2008", "Are sales value going up."),
        ("Dec 01, 2009", "A crash detected here"),
    ], )
    st.altair_chart(chart, width="stretch")

#Dataframe explorer
else:
    st.header("Dataframe explorer inside a dataframe")
    dt = generate_fake_dataframe(size=600, cols="dfc", col_names=["Id", "Sales","Revenue"], seed=1)
    #st.dataframe(dt)
    st.markdown("---")
    filtered_dt = dataframe_explorer(dt, case=False)

    st.dataframe(filtered_dt, width="stretch")


#Jupyter lite
st.markdown("---")
st.header("Jupyter Notebook")
jupyterlite(200,1000)
stoggle("Run","I am Running...")






