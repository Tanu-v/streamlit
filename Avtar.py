import streamlit as st

#Avtar

from streamlit_extras.avatar import *

st.title("Avatar")

a1,a2,a3 = st.columns(3)
with a1:
     avatar("https://avatars.githubusercontent.com/u/182893925?v=4",
            label="Tanu Verma",
            caption="Founder"

            )

with a2:
    avatar(image="https://avatars.githubusercontent.com/u/690814?v=4",
           label="Adam smith",
           caption="co-founder"


    )



with a3:
    avatar(image="https://avatars.githubusercontent.com/u/47222480?v=4",
           label="Jessica",
           caption="assistant"


    )

st.title("Avatar with different height")

b1,b2,b3 = st.columns(3)
with b1:
     avatar("https://avatars.githubusercontent.com/u/182893925?v=4",
            label="Tanu Verma",
            caption="Founder",
            height=35,

            )
with b2:
     avatar("https://avatars.githubusercontent.com/u/182893925?v=4",
            label="Tanu Verma",
            caption="Founder",
            height=52,


            )

with b3:
     avatar("https://avatars.githubusercontent.com/u/182893925?v=4",
           label="Tanu Verma",
           caption="Founder",
           height=84,

       )

st.title("Avatar  clickable ")

if avatar("https://avatars.githubusercontent.com/u/690814?v=4",
           label="Click me",
           caption="I am interactive",
           on_click="rerun",
           key="clickable_avatar",

           ):
                st.toast("avatar clicked")


#button

if st.button("Submit"):
    st.toast("worked submitted successfully!", icon="🌞")
    st.toast("You can use a color like :yellow[Orange] or :green[Green] ")


st.write("This is :orange-background[Tanu verma]")
