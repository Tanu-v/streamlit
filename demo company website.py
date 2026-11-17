import streamlit as st

#Homework08 : TANLIT , Date - 10/06/26

st.title("TANLIT")
st.subheader("Indian national Clothing referral company.")

st.sidebar.title("TANLIT | Online Fashion, Homeware & Kids Clothes | TANLIT IN")
ra = st.sidebar.radio("Choose to explore ", ["Home","Fashion","Beauty","Home & Kitchen","Customer Services"])


# Home tab

if ra == "Home":
    st.success("TANLIT is your shopping destination for fashion, home, beauty, kids' clothes and more. Browse the latest collections and find quality pieces at affordable prices.")
    st.header("WELCOME TO TANLIT!!!")
    st.image(r"C:\Users\TANU\Downloads\premium_vector-1683121609098-3a7345febc0b.jpg")

#Information about company
    st.info("TANLIT is an Indian national clothing and home and beauty referral company it connects different websites together and pick the best piece according to your choices and selection you made in one platform making it easier to connect and shop for different categories according to your choices and in affordable prices.It was founded to solve peoples worry and going to watch and see in different websites , it saves time and money and efforts of people making it easier and effortless for everyone to use.It is an open source website so everyone can use it easily and freely online .")
    st.video(r"C:\Users\TANU\Downloads\CFUL263C01E_Summer_M_15_16x9_COM.webm")

    st.header("Factsheet")
    st.subheader("Trade name")
    st.write("TANLIT")
    st.subheader("Company type")
    st.write("Public")
    st.subheader("Industry")
    st.write("Referral & Retail")
    st.subheader("Founded")
    st.write("2023 , 3 years ago in Raipur (C.G.) India")
    st.subheader("Area served")
    st.write("PAN India")
    st.subheader("Contact")
    st.write("tanlitgmail.com")

#Personal Information
    if st.header("Personal Information"):
        name = st.text_input("Name")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        age = st.number_input("Age", min_value=10, max_value=100)
        phone = st.text_input("Phone Number")
        email = st.text_input("Email")
        location = st.text_input("Location")


        if st.button("Submit"):
             st.success("Information submitted successfully!")
             st.write(f"Welcome, {name}!")


#Fashion tab

if ra == "Fashion":
   gen = st.selectbox("Choose your gender: ",["Male","Female"])
   if gen == "Male":
      st.image(r"C:\Users\TANU\Downloads\SPB_1500x460._SX1500_QL85_FMpng_.png")
      st.info("Find all men's clothing at H&M. Find the trendiest clothes, shoes, bags....")
      st.image(r"C:\Users\TANU\Downloads\IN_Mf05263p2_4x5_wk23.avif")

   else:
      st.image(r"C:\Users\TANU\Downloads\Ethnic_must-haves_1500x460._SX1500_QL85_FMpng_.png")
      st.info("Refresh your daily rotation with our women’s clothing range. With the....")
      st.image(r"C:\Users\TANU\Downloads\Classic_styles_1500x460._SX1500_QL85_FMpng_.png")


#Beauty tab

elif ra == "Beauty":
   st.image(r"C:\Users\TANU\Downloads\Beauty_1500x460._SX1500_QL85_FMpng_.png")
   st.info("You can find all men and women beauty product in our website and different ranges like perfumes, bags , sunglasses , makeups....")
   st.image(r"C:\Users\TANU\Downloads\Beauty_1500x460._SX1500_QL85_FMpng_ (1).png")


#Home & Kitchen tab

elif ra ==  "Home & Kitchen":
   st.image(r"C:\Users\TANU\Downloads\banner_v2_01._CB550379432_.jpg")
   st.info("You can get different home and kitchen appliences here in higher discount and affordable prices.")
   st.image(r"C:\Users\TANU\Downloads\Header_PC_Main_Auto._SX1500_QL85_.jpg")
   st.image(r"C:\Users\TANU\Downloads\banner_1_01._CB550378927_.jpg")
   st.image(r"C:\Users\TANU\Downloads\Header_PC_Main_Garden__Outdoors._SX1500_QL85_.jpg")



# Customer services

elif ra == "Customer Services":
    st.subheader("Customer Support")

    if st.button("Contact Us"):
        st.success("Our support team will be happy to help you!")

        st.write("You can contact our dedicated customer service team at tanlit@gmail.com")

    st.success("Thank you for using TANLIT!")
    st.info("Have a pleasant shopping experience.")
    st.balloons()

