import streamlit as st



#Text formatting

#Bold
st.write("**Bold text**")
st.write("Bold text")
st.markdown("** Bold text**")

#Italic text
st.write("*Italic text*")
st.write("Italic text")
st.markdown("** Italic text**")

#Italic + Bold text
st.write("***Italic and bold text***")
st.write("Italic and bold text")
st.markdown("** Italic and bold text**")

#monospace/code
st.write(" ` Code font ` ")
st.write(" **` Code font `**")
st.write(" ***`Code font `***")
st.write("example use ")
st.write("This is my file `about.py` you can check it .")

# Color formatting
st.write(" :blue[Blue text]")
st.markdown(" :blue[Blue text]")

st.write(" :green[Green text]")

st.write(" :yellow[Yellow text]")

st.write("  :gray[Gray text]")
#st.markdown(" :gray[Gray text]")

st.write(" :violet[Violet text]")

st.write(" :red[Red text]")

st.write(" :orange[Orange text]")

st.write(" :rainbow[Rainbow text]")


st.sidebar.title("Theme testing")

st.button("Submit")

st.metric("Profit",value=50000, delta=1200, delta_color="inverse", border=True )


col1, col2, col3 = st.columns(3)

col1.metric(label="Revenue", value="$52,400", delta="+1,200", border=True)
col2.metric(label="Churn Rate", value="2.1%", delta="-0.4%") #delta_color="inverse", border=True)
col3.metric(label="Active Users", value="14,210", delta="+342", border=True)


c3,c4 = st.columns(2)
with c3:
  st.file_uploader("Choose a file")

with c4:
  st.file_uploader("Choose a file",accept_multiple_files=True)


# For link adding in text formatting
st.write("")
"I am Tanu Verma and this is my [Portfolio](https://github.com/Tanu-v) and i enjoy sleeping  and eating with [chila](https://youtu.be/7iHGzA-IL-E)  "

st.write(" ")

#
