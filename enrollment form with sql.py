import streamlit as st
import pandas as pd
from streamlit_extras.specialized_inputs import *
import os
from streamlit_extras.let_it_rain import *
import mysql.connector
from streamlit_extras.mention import *

cn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Af01234#",
    database="Streamlit"
)

sc = cn.cursor()
print("Connected with MySQL Server Successfully!!")

def home():
    st.title(" 📋 :blue[Candidate Enrollment Form]")
    st.markdown("---")
    st.sidebar.title("📋 :blue[Candidate Enrollment Form]")
 #   st.sidebar.space("small")
    st.sidebar.markdown("---")
    st.sidebar.image("https://imgs.search.brave.com/dpMqpkJ1z2FMKZBiqleltN3RRcTKSlZAXn3m0qgpNvk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTM5/ODQ3MzE3Ny9waG90/by9xdWVzdGlvbm5h/aXJlLXdpdGgtY2hl/Y2tib3hlcy1maWxs/aW5nLXN1cnZleS1m/b3JtLW9ubGluZS1h/bnN3ZXItcXVlc3Rp/b25zLmpwZz9iPTEm/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9SnlT/MG5EZXVKYUlRSTZK/anBnd3V5QzlsRWlW/NDNuMG82am9wTHF1/MGtLdz0")
    st.sidebar.markdown("---")
    st.sidebar.space("small")
    st.warning("This is only for research purpose .")
    st.markdown("---")
    op = st.sidebar.selectbox("Choose an option",["Enroll","Update info","Read Info","Top Enrollment","Order by","Delete"])
    if op == "Enroll":
        st.subheader("📝 :blue[Enrollment Form]")
        st.markdown("---")
        st.info("Please enter your Enrollment details")
        st.markdown("---")
        name = st.text_input("Full Name", placeholder="Enter your Full name", key="name", help="Like - John Doe")
        gender = st.selectbox("Gender",["Male","Female","Others"],placeholder="Choose your gender",key="gender",help="Are you female or male?")
        age = st.number_input("Age", min_value=18, max_value=50, step=1, key="age",help="What is your age?")
        category = st.selectbox("Category",["ST/SC","OBC","GEN"],placeholder="Choose your category",key="category",help="Enter your category")
        phone_no = specialized_text_input("Phone Number",prefix=+91, placeholder="Enter your phone number", key="phone_no",help="enter your phone number without +91")
        tenth = specialized_text_input("10th percentages",suffix="%",placeholder="Please enter your 10th percentages",help="Enter percentage without % sign",key="10th")
        twelth = specialized_text_input("12th percentages",suffix="%",placeholder="Please enter your 12th percentages",help="Enter percentage without % sign",key="12th")

        email = specialized_text_input("Gmail/Email", suffix="@gmail.com", placeholder="Gmail", key="email", help="Enter your gmail id without '@gmail.com'")
        city = st.text_input("City", placeholder="Enter your city", key="city", help="Enter the city where you live ")
        state = st.text_input("State", placeholder="Enter your state", key="state", help="Enter your state ")
        pincode = st.number_input("Pincode",placeholder="Enter your pincode", key="pincode", help="Enter  pincode of your location",min_value=1)
        linkedin_url = url_input("LinkedIn Link",placeholder="Enter your LinkedIn url", key="linkedIn_url", help="Enter your LinkedIn url")
        st.markdown("---")
        if st.button("Submit"):
            Q = "Insert into candidate(name, gender, age, category, phone_no, tenth, twelth,email, city, state, pincode, linkedin_url) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            va = (name, gender, age, category, phone_no, tenth, twelth,email, city, state, pincode, linkedin_url)
            sc.execute(Q,va)
            cn.commit()
            st.success("Enrolled successfully!")
            st.balloons()
            st.snow()

    elif op == "Update info":
        st.subheader("📥 :blue[Update information]")
        st.space("small")
        id = st.number_input("Enter your ID",min_value=1)
        name = st.text_input("Full Name", placeholder="Enter your Full name", key="name", help="Like - John Doe")
        gender = st.selectbox("Gender", ["Male", "Female", "Others"], placeholder="Choose your gender", key="gender",
                              help="Are you female or male?")
        age = st.number_input("Age", min_value=18, max_value=50, step=1, key="age", help="What is your age?")
        category = st.selectbox("Category", ["ST/SC", "OBC", "GEN"], placeholder="Choose your category", key="category",
                                help="Enter your category")
        phone_no = specialized_text_input("Phone Number", prefix=+91, placeholder="Enter your phone number",
                                          key="phone_no", help="enter your phone number without +91")
        tenth = specialized_text_input("10th percentages", suffix="%", placeholder="Please enter your 10th percentages",
                                       help="Enter percentage without % sign", key="10th")
        twelth = specialized_text_input("12th percentages", suffix="%",placeholder="Please enter your 12th percentages",help="Enter percentage without % sign", key="12th")

        email = specialized_text_input("Gmail/Email", suffix="@gmail.com", placeholder="Gmail", key="email",
                                       help="Enter your gmail id without '@gmail.com'")
        city = st.text_input("City", placeholder="Enter your city", key="city", help="Enter the city where you live ")
        state = st.text_input("State", placeholder="Enter your state", key="state", help="Enter your state ")
        pincode = st.number_input("Pincode", placeholder="Enter your pincode", key="pincode",
                                  help="Enter  pincode of your location",min_value=1)
        linkedin_url = url_input("LinkedIn Link", placeholder="Enter your LinkedIn url", key="linkedIn_url",
                                 help="Enter your LinkedIn url")
        st.markdown("---")
        if st.button("Update Information"):
            Q = "update candidate set name=%s, gender=%s, age=%s, category=%s, phone_no=%s, tenth=%s, twelth=%s, email=%s, city=%s, state=%s, pincode=%s, linkedin_url=%s WHERE id=%s"
            va = (id,name, gender, age, category, phone_no, tenth, twelth, email, city, state, pincode, linkedin_url)
            sc.execute(Q, va)
            cn.commit()
            st.success("Enrolled successfully!")


    elif op == "Read Info":
        st.subheader("🪪 :blue[Read Information]")
        st.space("small")
        sc.execute("select * from candidate")
        result = sc.fetchall()
        for row in result:
            st.write(row)

    elif op == "Top Enrollment":
        st.subheader("📈 :blue[Top 5 Enrollment]")
        st.space("small")
        sc.execute("select name, twelth from candidate order by twelth desc limit 5;")
        result = sc.fetchall()
        for row in result:
            st.write(row)

    elif op == "Order by":
        st.subheader("📊 :blue[Order by]")
        st.space("small")
        sb = st.selectbox("Order by", ["Name","tenth","category","gender", "twelth"], key="order")
        if sb == "Name":
            st.subheader(" :blue[Order by Name]")
            st.space("small")
            ob = st.selectbox("Order in",["Ascending", "Descending"], key="ord")
            if ob == "Ascending":
                st.write("Order by Name in Ascending order")
                sc.execute("select * from candidate order by name ")
                result = sc.fetchall()
                for row in result:
                    st.write(row)
            else:
                st.write("Order by Name in Descending order")
                sc.execute("select * from candidate order by name desc")
                result = sc.fetchall()
                for row in result:
                    st.write(row)

        elif sb == "tenth":
            st.subheader(" :blue[Order by tenth]")
            st.space("small")
            ob = st.selectbox("Order in", ["Ascending", "Descending"], key="ord")
            if ob == "Ascending":
                st.write("Order by 10th in Ascending order")
                sc.execute("select * from candidate order by tenth ")
                result = sc.fetchall()
                for row in result:
                    st.write(row)
            else:
                st.write("Order by Name in Descending order")
                sc.execute("select * from candidate order by tenth desc")
                result = sc.fetchall()
                for row in result:
                    st.write(row)


        elif sb == "category":
            st.subheader(" :blue[Order by category]")
            st.space("small")
            ob = st.selectbox("Order in", ["Ascending", "Descending"], key="ord")
            if ob == "Ascending":
                st.write("Order by Category in Ascending order")
                sc.execute("select * from candidate order by category ")
                result = sc.fetchall()
                for row in result:
                    st.write(row)
            else:
                st.write("Order by Name in Descending order")
                sc.execute("select * from candidate order by category desc")
                result = sc.fetchall()
                for row in result:
                    st.write(row)


        elif sb == "gender":
            st.subheader(" :blue[Order by gender]")
            st.space("small")
            ob = st.selectbox("Order in", ["Ascending", "Descending"], key="ord")
            if ob == "Ascending":
                st.write("Order by Gender in Ascending order")
                sc.execute("select * from candidate order by gender ")
                result = sc.fetchall()
                for row in result:
                    st.write(row)
            else:
                st.write("Order by Name in Descending order")
                sc.execute("select * from candidate order by gender desc")
                result = sc.fetchall()
                for row in result:
                    st.write(row)


        else:
            st.subheader(" :blue[Order by twelth]")
            st.space("small")
            ob = st.selectbox("Order in", ["Ascending", "Descending"], key="ord")
            if ob == "Ascending":
                st.write("Order by 12th in Ascending order")
                sc.execute("select * from candidate order by twelth ")
                result = sc.fetchall()
                for row in result:
                    st.write(row)
            else:
                st.write("Order by Name in Descending order")
                sc.execute("select * from candidate order by twelth desc")
                result = sc.fetchall()
                for row in result:
                    st.write(row)

    else:
        st.subheader(" :blue[Delete Information]")
        st.space("small")
        id = st.number_input("Enter your Id ", key="id",min_value=1,step=1)
        if st.button("Delete Information"):
            Q = "delete from candidate where id = %s"
            va = (id,)
            sc.execute(Q,va)
            cn.commit()
            st.success("Candidate Deleted Successfully!")

if __name__ == "__main__":
    home()

from streamlit_extras.bottom_container import *
with bottom():
    st.markdown("---")
    st.caption("Developed by Tanu Verma")
    mention(label="Tanu-v", url="https://github.com/Tanu-v", icon="github")
    st.sidebar.markdown("---")

    st.caption("@2026| All Rights Reserved")
    st.sidebar.caption("Developed Tanu Verma")
    st.sidebar.caption("@2026| All Rights Reserved")

rain(
    emoji="🌞",
    falling_speed=5,
    font_size=39,
    animation_length="infinite"
)