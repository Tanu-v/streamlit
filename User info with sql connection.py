import streamlit as st

import mysql.connector

sq = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Af01234#",
    database="Streamlit"
)

ls = sq.cursor()

print("Stabilised Connection with MySQL")

def main():
    st.title("User Information form ")
    st.write("This is only for research purpose")
    sb = st.sidebar.selectbox("Select an option", ["Create","Update","Delete","Read"])
    if sb == "Create":
        st.subheader("Create a Record")
        #Id = st.number_input("Enter an Id")
        Name = st.text_input("Enter your Name")
        Email = st.text_input("Enter your Email")
        if st.button("Save Record"):
            D = "Insert into user(Name,Email) values(%s,%s)"
            a = (Name,Email)
            ls.execute(D,a)
            sq.commit()
            st.success("Record Created successfully!")


    elif sb == "Update":
        st.subheader("Update Record")
        Id = st.number_input("Enter your ID")
        Name = st.text_input("Enter your Name")
        Email = st.text_input("Enter your Email")
        if st.button("Update Record"):
            D = "update user set Name = %s , Email = %s where Id = %s"
            a = (Name,Email,Id)
            ls.execute(D,a)
            sq.commit()
            st.success("Record Updated successfully!")



    elif sb == "Delete":
        st.subheader("Delete Record")
        Id = st.number_input("Enter your ID",min_value=1)
        if st.button("Delete Record"):
            D = "delete from user where Id = %s"
            a = (Id,) #or [Id]
            ls.execute(D,a)
            sq.commit()
            st.success("Record Deleted successfully!")


    else:
        st.subheader("Read Record")
        ls.execute("select * from user")
        result = ls.fetchall()
        for row in result:
            st.write(row)







if __name__ == "__main__":
    main()
