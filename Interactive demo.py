import streamlit as st

from streamlit_extras.mention import *
mention("IBM","https://www.ibm.com/in-en",icon="IBM")#"https://imgs.search.brave.com/1DamicmryBv61bYz_nDeyCY2u21kd8c54w8qkb2cLgA/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9jcnlz/dGFscG5nLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvMjAyNS8w/NS9pYm0tbG9nby5w/bmc")
#telegram,streamlit,github,notion, bydefault logo available
mention(label="touch me",icon="streamlit",url="https://streamlit.io/")

#date-range picker
from streamlit_extras.mandatory_date_range import *
st.write("Choose your date:")
re = date_range_picker("Select a date range")
#st.write("This is the date:",re)

#Pagination
from streamlit_extras.pagination import *
st.write(" ### Interactive demo ")

a,b = st.columns(2)

with a:
    num_pages=st.number_input("Number of pages",value=5,min_value=1,step=1,max_value=50,key="num_pages")

with b:
    num_page = st.number_input("Visible pages", value=11, min_value=0, step=1, max_value=25, key="demo_max_visible",help="set to 0 to not get any error")

ab = pagination(num_pages=num_pages, max_visible_pages = num_page,key="ab")

st.write(f" **Current Page**: {ab}")

#statefull button
from streamlit_extras.stateful_button import *
if button("Button1",key="button1") and button("Button2",key="button2"):
    if button("Button3",key="button3"):
        st.write(" You have reached level 3 ")
        if button("Button4",key="button4"):
            st.write(" You have reached level 4 ")
            st.image(r"C:\Users\TANU\Downloads\gettyimages-1266802968-612x612.jpg")
            if button("Button5",key="button5"):
                st.write(" You have reached level 5 ")
                st.success(" This is the end of level")
        # OR and AND

# 2 + 2 = 4 and 3 + 4 = 7

#Image crop
from streamlit_extras.image_crop import *
st.write(" ### Basic croping")
ci = image_crop(r"C:\Users\TANU\Downloads\banner_1_01._CB550378927_.jpg",key="image_crop")
if ci:
    st.write(f" **Selected region**: x = {ci['x']:.2f}, y = {ci['y']:.2f}, width = {ci['width']:.2f}, height = {ci['height']:.2f} ")

else:
    st.write("No region selected yet!!")

#Compare slider
from streamlit_extras.image_compare_slider import *

st.write(" ### Comparison of image")
image_compare_slider("https://imgs.search.brave.com/LPbKDrpJFiNAfTBkDVId7ZdOoYGYf7o0HUhIfYM98Ko/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9maWxt/ZmFyZS53d21pbmRp/YS5jb20vcGhvdG9n/YWxsZXJ5LzIwMjUv/YXByL2hhbmlhYWFt/aXI5MTc0MzQ4ODg4/My5qcGc",
                      "https://imgs.search.brave.com/LPbKDrpJFiNAfTBkDVId7ZdOoYGYf7o0HUhIfYM98Ko/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9maWxt/ZmFyZS53d21pbmRp/YS5jb20vcGhvdG9n/YWxsZXJ5LzIwMjUv/YXByL2hhbmlhYWFt/aXI5MTc0MzQ4ODg4/My5qcGc?w=800&sat=-100",#"https://imgs.search.brave.com/-BfkUq9T5ha-1h5Yn5pV0azAE8Mq6p250lMftP5S-YI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzBhLzE0/LzBlLzBhMTQwZWM4/NTkxZDAzZjRkZGNh/ODViNDM3ZmI4YTNh/LmpwZw",
                     label1="color", label2="Grayscale", key="img")





