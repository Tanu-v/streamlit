
import streamlit as st

st.header("COLORS")
st.info(" *Colors for kids to learn* .")
st.sidebar.markdown(" :rainbow[Colors] 🫟 ")
st.image("https://i.pinimg.com/736x/80/3b/10/803b109036902f82cbf76227a69ff24f.jpg")

from streamlit_extras.radial_menu import *


cl = radial_menu(
    options={
        "Red":"❤️",
        "Pink":"🩷",
        "Blue":"💙",
        "Purple":"💜",
        "Yellow":"💛",
        "Brown":"🤎",
        "Green":"💚",
        "Black":"🖤",
        "Orange":"🧡",
        "Gray":"🩶",
        "White":"🤍",

    },

    key="nav_menu",
   )
if cl['selection'] == "Red":
        st.subheader(" :red[Red] ")
        st.success(" This is a color named Red .")
        st.toast("Red is a color named :red[Red] .")
        st.image("https://i.pinimg.com/736x/0c/65/13/0c65137df577df68763ecf541928056f.jpg")

elif cl['selection'] == "Pink":
    st.subheader(" :pink[Pink] ")
    st.success(" This is a color named Pink .")
    st.toast("Pink is a color named :pink[Pink] .")
    st.image("https://i.pinimg.com/736x/f9/a8/0d/f9a80d7a13d628e9188cdd7923d671e0.jpg")

elif cl['selection'] == "Blue":
    st.subheader(" :blue[Blue] ")
    st.success(" This is a color named Blue .")
    st.toast("Blue is a color named :blue[Blue] .")
    st.image("https://i.pinimg.com/736x/9d/3c/6e/9d3c6e66ff7a42573b2af3c696aeaaa7.jpg")

elif cl['selection'] == "Purple":
    st.subheader(" :purple[Purple] ")
    st.success(" This is a color named Purple .")
    st.toast("Purple is a color named Purple .")
    st.image("https://i.pinimg.com/474x/31/a4/bc/31a4bc5aa82e2923cff4efa8dfa910cc.jpg")

elif cl['selection'] == "Yellow":
    st.subheader(" :yellow[Yellow] ")
    st.success(" This is a color named Yellow .")
    st.toast("Yellow is a color named Yellow .")
    st.image("https://i.pinimg.com/1200x/9e/8c/7c/9e8c7ca9eecf4517e7e21e70ff6f11b8.jpg")

elif cl['selection'] == "Brown":
    st.subheader(" :brown[Brown] ")
    st.success(" This is a color named Brown .")
    st.toast("Brown is a color named Brown .")
    st.image("https://i.pinimg.com/474x/48/bb/0c/48bb0c0c72954150091078b379d595db.jpg")

elif cl['selection'] == "Green":
    st.subheader(" :green[Green] ")
    st.success(" This is a color named Green .")
    st.toast("Green is a color named Green .")
    st.image("https://i.pinimg.com/564x/5f/8f/b2/5f8fb25c31bff7fc2e8f67f7af10e2e6.jpg")

elif cl['selection'] == "Black":
    st.subheader(" :black[Black] ")
    st.success(" This is a color named Black .")
    st.toast("Black is a color named Black .")
    st.image("https://i.pinimg.com/736x/bd/84/60/bd84603f9b6720e0ae084bf06d06d358.jpg")

elif cl['selection'] == "Orange":
    st.subheader(" :orange[Orange] ")
    st.success(" This is a color named Orange .")
    st.toast("Orange is a color named Orange .")
    st.image("https://i.pinimg.com/564x/17/0f/11/170f11154cd3520a07ddc0e861f1c9fc.jpg")

elif cl['selection'] == "Gray":
    st.subheader(" :gray[Gray] ")
    st.success(" This is a color named Gray .")
    st.toast("Gray is a color named Gray .")
    st.image("https://i.pinimg.com/474x/d5/44/50/d54450a1773f9b1ca68ef3c73b63c162.jpg")

else:
    st.subheader(" White")
    st.success(" This is a color named White .")
    st.toast("White is a color named White .")
    st.image("https://i.pinimg.com/564x/9e/07/a8/9e07a8b10cf622b0d87afca5167c9766.jpg")


st.success(" Here's a video from where you can learn :- ")
st.video("https://youtu.be/FiC3ClDnsG0")
st.video("https://youtu.be/qhOTU8_1Af4")
