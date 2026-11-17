import select
import streamlit as st
from streamlit_extras.radial_menu import radial_menu

st.write("Click the button below to open the radial menu : ")

rm = radial_menu(
    options={
        "Home":"🏠",
        "Search":"🔍",
        "Settings":"⚙️",
        "Profile":"👤",
        "Help":"❓"
    },

    key="nav_menu",
)


if select :
    se = select.get("selection")

    if se == "Search":
      st.switch_page(r"C:\Users\TANU\PycharmProjects\PythonProject\Footwear.py")


st.write(f"**Selected** '{rm["selection"]}' ")

# emoji rain

from streamlit_extras.let_it_rain import *

rain(
    emoji="❄️",
    font_size=54,
    falling_speed=5,
    animation_length= "infinite",

)

#Badges

from streamlit_extras.badges import *
badge( type="pypi",name="plost")
badge( type="pypi",name="streamlit")
#badge( type="google",name="meet") not available
badge(type="github",name="Tanu-v/Streamlit_demo" )
badge(type="buymeacoffee",name="andfanilo")
badge(type="streamlit",url="https://yourmist.streamlit.app/")
badge(type="twitter",name="streamlit")

#Card selector

from streamlit_extras.card_selector import *


cs = card_selector(
    [
        dict(icon=":material/cloud:" ,
             title="cloud" ,
             description= "deploy to manage cloud service",
             link="https://github.com/Tanu-v",
             ),
        dict(icon=":material/computer:" ,
             title= "computer",
             description= "material run on your own machine",
             ),
        dict(icon= ":material/dns:",
             title= "dns",
             description= "host in your data centre",
             ),


    ],

    key="demo_basic",

)

if select is not None:
    st.write(f"**Your picked option:** '{select}' ")

