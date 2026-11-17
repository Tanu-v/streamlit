import streamlit as st

from streamlit_extras.stodo import *


st.title(" 📝 :blue[My ToDo List] ")
st.sidebar.title("📝 :blue[My ToDo List]")
st.sidebar.image("https://imgs.search.brave.com/X9_rNeK5xQ_Igxub6nUH7lrd0HikewQp9fWqYPepRWo/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS12ZWN0b3Iv/dGlueS1wZW9wbGUt/d2l0aC1jbG9jay1j/aGVja2xpc3QtdGFy/Z2V0Xzc0ODU1LTE3/OTI0LmpwZz9zZW10/PWFpc19oeWJyaWQm/dz03NDA")

#Long term goals
st.sidebar.header("🌟 Future Life Goals (Long-Term Vision)")
sb = st.sidebar.selectbox("Select one to see:-",["Career/Skill Goal","Financial Goal","Health Goal"])

if sb== "Career/Skill Goal":
    st.header("🌟 :red[Future Life Goals (Long-Term Vision)]")
    st.subheader("Career/Skill Goal🎯")
    to_do([(st.write," :green[Become a well established Data Scientist.]")],"Data Scientist",)
    to_do([(st.write," :green[Become a Good AI Researcher .]")],"AI Researcher",)
    to_do([(st.write," :green[Got a good placement in a Big company .]")],"Placement",)
    to_do([(st.write," :green[Learn the remaining coding languages required .]")],"Coding languages",)
    to_do([(st.write," :green[If you become successful try to help others.]")],"Helping",)
    st.info("I want to become a well established Data Scientist and AI researcher , so that i can be independent and help my parents and loved ones in their need .")

    st.write()
    "How to complete my carrier goals [youtube Help](https://youtu.be/fXyRprdoEoE) "
    st.write()

    st.success("It is One of my priority.")
    st.toast(" :orange[These are my Career/Skill Goals🎯!]")

elif sb == "Financial Goal":
    st.header("🌟 :red[Future Life Goals (Long-Term Vision)]")
    st.subheader("Financial Goal💸")
    to_do([(st.write," :violet[Have a permanent source of Income .]")],"Income source",)
    to_do([(st.write," :violet[Have many sources of Income as much as possible .]")]," Multiple Income source",)
    to_do([(st.write," :violet[Collect an emergency fund of enough amount .]")],"Emergency fund",)
    to_do([(st.write," :violet[Save money for travelling.]")],"Travelling",)
    to_do([(st.write," :violet[Save money for food .]")],"Food",)
    st.info("I want earn and save enough money so that i can be independent and help my parents and my loved ones in their need . And also can travel and eat as much as i want .")
    st.success("It is also One of my priority.")

    st.write()
    "How to complete my financial goals [youtube Help](https://youtu.be/IbcYNtZ8HZY) "
    st.write()

    st.toast(" :blue[These are my Financial Goals💸!.]")


else :
    st.header("🌟 :red[Future Life Goals (Long-Term Vision)]")
    st.subheader("Health Goals 🚵‍♀️")
    to_do([(st.write," :orange[Stay in health as much as possible.]")],"Health Goals",)
    to_do([(st.write," :orange[Try to do exercise three-four times a week .]")],"Exercise three-four times a week .",)
    to_do([(st.write," :orange[Have a full body checkup Once a year .]")],"Full body checkup",)
    to_do([(st.write," :orange[maintain your body in shape and be fit .]")],"Maintain your body in shape and be fit .",)
    to_do([(st.write," :orange[Have good sleep .]")],"Sleep",)
    st.info("I want to be fit and have a good sleep so that I can be healthy and work with all my might and take care of my parents and loved ones .")
    st.success("It is also One of my priority.")

    st.write()
    "How to complete my health goals [youtube Help](https://youtu.be/F8IQQad0lTA) "
    st.write()

    st.toast(" :green[These are my Health Goals🚵‍♀️!] ")


#Short term goals
st.sidebar.header(" 🧘🏻‍♀️Personal Things & Daily Routine (Short-Term Action)")
ms = st.sidebar.multiselect("Select to see:",["Daily Tech","Self Care","Home/Hobbies"])

if ms == "Daily Tech":
    st.header("🧘🏻‍♀️ :green[Personal Things & Daily Routine (Short-Term Action)] ")
    st.subheader("Daily Tech👩🏼‍💻")
    to_do([(st.write," :yellow[Complete the daily work given .]")],"Daily work",)
    to_do([(st.write," :yellow[Complete the daily tech task.]")],"Daily tech task",)
    to_do([(st.write, " :yellow[Revise the all tech related notes.]")],"Revision",)
    st.error("Do it daily otherwise you won't be able to reach your long term goals.")
    st.toast(" :green[These are my Daily Tech short term goals.]")

elif ms == "Self Care":
    st.header("🧘🏻‍♀️ :green[Personal Things & Daily Routine (Short-Term Action)] ")
    st.subheader("Self Care 💆🏻‍♀️")
    to_do([(st.write, " :blue[Do skin care twice a week .]")], "skin care", )
    to_do([(st.write, " :blue[Take a bath daily.]")], "Daily bath", )
    to_do([(st.write, " :blue[Drink sufficient amount of water daily and be hydrated.]")], "drink water", )
    to_do([(st.write," :blue[Eat your food on time .]")],"Food on time ",)
    to_do([(st.write," :blue[Take 2km walk daily]")],"daily walk",)
    st.error("Do it daily otherwise you won't be able to reach your long term goals.")

    st.write()
    "Daily self care is essential watch this [daily self care](https://youtu.be/UaMFf6Y4hHU) "
    st.write()

    st.toast(" :green[These are my self care short term goals.]")

else:
    st.header("🧘🏻‍♀️ :green[Personal Things & Daily Routine (Short-Term Action)] ")
    st.subheader("Home/Hobbies🍀 ")
    to_do([(st.write, " :orange[Organize things don't make a mess .]")], "Organize things", )
    to_do([(st.write, " :orange[Help mom and dad daily and as much as you can.]")], "help parents", )
    to_do([(st.write, " :orange[Do house work daily like cleaning, cooking, chores and laundry.]")], "house work", )
    to_do([(st.write, " :orange[warship god daily .]")], "warship ", )
    to_do([(st.write, " :orange[Water the plants and spend time in nature.]")], "nature", )
    st.error("Do it daily otherwise you won't be able to reach your long term goals.")

    st.toast(" :blue[These are my Home/Hobbies short term goals.]")








