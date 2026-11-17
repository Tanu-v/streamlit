import streamlit as st

#All streamlit's basic properties

#live camera and audio

st.camera_input("Take a picture")
st.audio_input("Make a sound")

st.pills( "tag",["Sports","Modeling","Singing"])

st.feedback("thumbs")

st.space("small")

st.feedback("faces")
st.space("large")
st.feedback("stars")
st.space()
#["stretch", "xxsmall", "xsmall", "small", "medium", "large", "xlarge", "xxlarge"] options indside st.space()

fil=st.segmented_control("filter",["A","B","C","D","E","F"])
if fil=="A":
    st.write("This is segment A")

st.menu_button("Export",[".csv",".json",".pdf",".text"])

st.toggle("Unable")

st.pagination(10)

var = st.container(horizontal=True)
var.button("A")
var.button("B")
var.image(r"C:\Users\TANU\Downloads\ChatGPT Image Jul 4, 2026, 12_26_39 PM.png")

with st.echo():
    st.write("This is a segment")#write code segment

st.badge("Tanu",icon="😍")

tab1,tab2=st.tabs( ["Tab1","Tab2"])
with tab1:
    st.image(r"C:\Users\TANU\Downloads\cf017e25-80ab-47f5-8d12-b8006b2fb977.webp")
    st.write("This is a sunflower")

with tab2:
    st.image(r"C:\Users\TANU\Downloads\images.jpg")
    st.write("These are tulips")

st.metric("My Metric",42,2)
if st.button("Snow"):
    st.snow()

if st.button("Balloon"):
    st.balloons()

st.write(["st","Is < ", 3]) #property of list in under st.write  formation

"_This_ is **Markdown**" # _text_ makes it in italic

st.json({"foo":"bar","Fu":"Ba"}) # property of dictionary under json
