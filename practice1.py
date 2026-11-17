import streamlit as st
from streamlit_extras.card_selector import *
from streamlit_extras.avatar import *

# emoji rain

from streamlit_extras.let_it_rain import *

rain(
    emoji="🌸",
    font_size=44,
    falling_speed=14,
    animation_length=15,

)

st.title(" :green-background[Flower, Fruit & Vegetable] ")
st.sidebar.title(" :green[Flower, Fruit & Vegetable] ")
st.info(""" 
             ## ***Some beautiful flowers , tasty fruits and yummy veggies*** 
             """)
st.warning("""
            ### It's only my personal choices only """)
sel = st.sidebar.radio("Select a option here: ",["flower","fruit","vegetable"])

#radial menu
from streamlit_extras.radial_menu import *

if sel == "flower":
    fl = radial_menu(
    options={
        "Sunflower":"🌻",
        "Rose":"🌹",
        "Tulip":"🌷",
        "Hibiscus":"🌺",
        "Lotus":"🪷",
    },

    key="nav_menu",
   )
    if fl:
       selection = fl.get("selection")

    if selection == "Sunflower":
        st.link_button(" :yellow[About Sunflower] ", "https://en.wikipedia.org/wiki/Common_sunflower" )
       # st.image("")
        st.toast("You can read about Sunflower here!", icon="🌻")

    elif selection == "Rose":
        st.link_button(" :blue[About Rose] ", "https://en.wikipedia.org/wiki/Rose")
        st.toast("You can read about Rose here!", icon="🌹")

    elif selection == "Tulip":
        st.link_button(" :green[About Tulip] ", "https://en.wikipedia.org/wiki/Tulip")
        st.toast("You can read about Tulip here!", icon="🌷")

    elif selection == "Hibiscus":
        st.link_button(" :red[About Hibiscus] ", "https://en.wikipedia.org/wiki/Hibiscus")
        st.toast("You can read about Hibiscus here!", icon="🌺")

    elif selection == "Lotus":
        st.link_button(" :orange[About Lotus] ", "https://en.wikipedia.org/wiki/Lotus")
        st.toast("You can read about Lotus here!", icon="🪷")

    st.write(f"**Selected options:** {selection}")


# Card selector

elif sel == "fruit":
    st.header("Fruits")
    if card_selector(
    [
         dict(icon="🥭",
             title=" Mango ",
             description="It is a fruit named Mango!",

            ),
         dict(icon="🍎",
             title=" Apple",
             description="It is a fruit named Apple!",

             ),
         dict(icon="🍌",
             title="Banana",
             description="It is a fruit named Banana!",

             ),
         dict(icon="🍊",
             title="Orange",
             description="It is a fruit named Orange!",

             ),
         dict(icon="🫐",
             title=" Blue-berry",
             description="It is a fruit named Blue-berry!",

             ),
         ],

        key="demo_basic",

       ):
           st.toast("Yummy!!!" )

#Avatar

else:
      st.header("Vegetables")
      veggies= st.radio("Select a vegetable :",["eggplant(Brinjal)","Tomato","Capsicum","Pea"])

      if veggies == "eggplant(Brinjal)":
           avatar("https://imgs.search.brave.com/Uw91etFjPG18Ktc5bpNnzbh7f7sWb8DXRCxEd7iaDsQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS1waG90by9z/dGlsbC1saWZlLXdp/dGgtZGVsaWNpb3Vz/LWVnZ3BsYW50XzIz/LTIxNTAzOTIyODcu/anBnP3NlbXQ9YWlz/X2h5YnJpZA",
              label="eggplant(Brinjal)",
              caption="It is a vegetable and also edible",
              height=100,
             # width=100,

               )
           st.toast("It is an eggplant(Brinjal)!", icon="🍆" )

           st.link_button("Wikipedia of eggplant(Brinjal)","https://en.wikipedia.org/wiki/Eggplant")


      elif veggies == "Tomato":
           avatar("https://imgs.search.brave.com/QAXKGOyTRf1d2asS1iByq2AY9mGaYfI-nywNHIbBsME/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjIy/MDYwNTU4My9waG90/by9yaXBlLW9yZ2Fu/aWMtdG9tYXRvZXMt/b24tYS13b29kZW4t/Y3V0dGluZy1ib2Fy/ZC1oZWFsdGh5LWFu/ZC1qdWljeS1tZWRp/dGVycmFuZWFuLWZv/b2QtcmVhZHktdG8u/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PUtOUnBxSWxxVWtr/OFF0Sjcxd2lmdHhl/cUJoNGZXV3JDM3FJ/ZzctMms3RGs9",
               label="Tomato",
               caption="It is a tomato and it is edible",
               height=100,
             #  width=100,

             )
           st.toast("It is an Tomato!", icon="🍅" )
           st.link_button("Wikipedia of Tomato!","https://en.wikipedia.org/wiki/Tomato")

      elif veggies == "Capsicum":
           avatar("https://imgs.search.brave.com/G7e2exMx8qnbQAjFHx4eHS5YWG3r5WmV6BaYu_VHt6E/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMzLmRlcG9zaXRw/aG90b3MuY29tLzEw/MDY4ODAvMjEzL2kv/NDUwL2RlcG9zaXRw/aG90b3NfMjEzMjIx/My1zdG9jay1waG90/by1jYXBzaWN1bS5q/cGc",
               label="Capsicum",
               caption="It is a capsicum and it is edible",
               height=100,
              # width=100,
             )
           st.toast("It is a capsicum!", icon="🫑" )
           st.link_button("Wikipedia of Capsicum!","https://en.wikipedia.org/wiki/Capsicum")

      else :
          avatar("https://imgs.search.brave.com/fMm8kzcT_Ukl5pD8TuoWLJYFLob_UJPn9bitLYvbh80/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/bWFnbmlmaWMuY29t/L2ZyZWUtdmVjdG9y/L2lzb2xhdGVkLWdy/ZWVuLXBlYXMtY2Fy/dG9vbl8xMzA4LTEz/MTkyNC5qcGc_c2Vt/dD1haXNfdGVzdF9j/Jnc9NzQwJnE9ODA",
               label="Pea",
               caption="It is a pea and it is edible",
               height=100,
             #  width=100,

             )
          st.toast("It is a pea!", icon="🫛" )
          st.link_button("Wikipedia of Pea!","https://en.wikipedia.org/wiki/Pea")



