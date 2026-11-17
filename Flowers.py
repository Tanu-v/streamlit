import streamlit as st
from streamlit_extras.image_crop import *
from streamlit_extras.image_compare_slider import *
from streamlit_extras.pagination import *

#Homework16: Practice

st.title("🌸 :blue[Flowers] ")
st.sidebar.title("🌸 :blue[Flowers] ")
st.markdown("---")
st.sidebar.markdown("---")
st.sidebar.image(r"C:\Users\TANU\Downloads\c81a7a2999d702b1943bba5ae43d2c60.webp")
st.sidebar.markdown("---")
st.write(""" This site compare , crop and give some information about certain flowers .
           Its only a personal one! """)
st.write(" :green[To know about who made the site touch the icon below]:")

from streamlit_extras.mention import *
mention(label="Tanu-v", url="https://github.com/Tanu-v", icon="github")
st.markdown("---")
from streamlit_extras.stateful_button import *
if button("Flowers",key="button1") and button("Look at it",key="button2"):
    if button("Orchid",key="button3"):
        st.write(" This is a flower image of orchid . ")
        st.info("You can crop this image and see the coords")
        ic1=image_crop("https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Plant_Orchid_Cymbidium_aloifolium_P1110661_05_-_cropped.jpg/960px-Plant_Orchid_Cymbidium_aloifolium_P1110661_05_-_cropped.jpg",key="img1")
        if ic1:
            st.write(
                f" **Selected region**: x = {ic1['x']:.2f}, y = {ic1['y']:.2f}, width = {ic1['width']:.2f}, height = {ic1['height']:.2f} ")

        else:
            st.write("No region selected yet!!")
        image_compare_slider(r"C:\Users\TANU\Downloads\ChatGPT Image Jul 4, 2026, 12_35_56 PM.png",
                             r"C:\Users\TANU\Downloads\ChatGPT Image Jul 4, 2026, 12_37_54 PM.png",
                             label1 = "color", label2 = "Grayscale", key = "image1"
                             )
        if button("Tulip",key="button4"):
            st.write(" This is a flower image Tulip . ")
            st.info("You can crop this image and see the coords")
            ic2 = image_crop(r"C:\Users\TANU\Downloads\images.jpg",key="img2")
            if ic2:
                st.write(
                    f" **Selected region**: x = {ic2['x']:.2f}, y = {ic2['y']:.2f}, width = {ic2['width']:.2f}, height = {ic2['height']:.2f} ")

            else:
                st.write("No region selected yet!!")
            image_compare_slider(r"C:\Users\TANU\Downloads\images (1).jpg",
                                 r"C:\Users\TANU\Downloads\ChatGPT Image Jul 4, 2026, 12_26_39 PM.png",
                                 label1="color", label2="Grayscale", key="image2"
                                 )
            if button("Lotus",key="button5"):
                st.write(" This is a flower image Tulip . ")
                st.info("You can crop this image and see the coords")
                ic3 = image_crop(r"C:\Users\TANU\Downloads\Lotus-1.jpg", key="img3")
                if ic3:
                    st.write(
                        f" **Selected region**: x = {ic3['x']:.2f}, y = {ic3['y']:.2f}, width = {ic3['width']:.2f}, height = {ic3['height']:.2f} ")

                else:
                    st.write("No region selected yet!!")
                image_compare_slider(r"C:\Users\TANU\Downloads\ChatGPT Image Jul 4, 2026, 01_01_06 PM.png",
                                     r"C:\Users\TANU\Downloads\ChatGPT Image Jul 4, 2026, 01_04_37 PM.png",
                                     label1="color", label2="Grayscale", key="image3"
                                     )

                st.success(" This is the end !")
                st.write("If you want to know more about flowers click the button below:")
                mention("Flowers",url="https://en.wikipedia.org/wiki/Flower",icon="🌺")
st.markdown("---")

from streamlit_extras.bottom_container import *
with bottom():
    st.caption("This is made by - Tanu Verma" )
    st.caption("@2026 | All Rights Reserved")


from streamlit_extras.mandatory_date_range import *
st.write("Select a date range:")
ran = date_range_picker("Choose a date range")
st.write("Your selected date range is : ",ran)

st.markdown("---")


c,d,e = st.columns(3)

with c:
    st.write("Flower 'Sunflower'")
    st.write("Some Images of 'Sunflower' ")
    st.image(r"C:\Users\TANU\Downloads\cf017e25-80ab-47f5-8d12-b8006b2fb977.webp")
    st.image(r"C:\Users\TANU\Downloads\shutterstock_2502729023-min-1080x721.jpg")
    st.image(r"C:\Users\TANU\Downloads\images (6).jpg")
    st.info("You can read more about Sunflower by touching the word below:")
    mention("Sunflower", url="https://en.wikipedia.org/wiki/Sunflower")
    n_pages = st.number_input("Number of pages", value=4, min_value=1, step=1, max_value=34, key="n_pages")

with d:
    st.write("Flower 'Rose'")
    st.write("Some Images of 'Rose' ")
    st.image(r"C:\Users\TANU\Downloads\images (4).jpg")
    st.image(r"C:\Users\TANU\Downloads\images (5).jpg")
    st.image(r"C:\Users\TANU\Downloads\rose-color-meanings-697a8582eee40.avif")
    st.info("You can read more about Rose by touching the word below:")
    mention("Rose", url="https://en.wikipedia.org/wiki/Rose")
    np = st.number_input("Number of np pages",value=11,min_value=1,step=1,max_value=100,key="np_pages")

with e:
    st.write("Flower 'Marigold'")
    st.write("Some Images of 'Marigold'")
    st.image(r"C:\Users\TANU\Downloads\71QUjEd9x7L._AC_UF1000,1000_QL80_.jpg")
    st.image(r"C:\Users\TANU\Downloads\images (3).jpg")
    st.image(r"C:\Users\TANU\Downloads\MAR-A_AMX00076_Blog.jpg")
    st.info("You can read more about marigold by touching the word below:")
    mention("Marigold",url="https://en.wikipedia.org/wiki/Marigold")

pagi = pagination(num_pages=n_pages, max_visible_pages = np ,key="pagi")
st.write(f" **Current Page**: {pagi}")
