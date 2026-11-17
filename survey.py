import streamlit as st
import pandas as pd
from streamlit_extras.specialized_inputs import *
import os
from streamlit_extras.let_it_rain import *

st.title("📋 :blue[Employee Exit Survey Form]")
st.sidebar.title("📋 :blue[Employee Exit Survey Form]")
st.warning("Thank you for your time and contributions to our organization. We want to ensure we continuously improve our workplace, culture, and employee experience. Please take 5–10 minutes to complete this survey. Your honest feedback is invaluable and will remain strictly confidential.")

st.image("https://imgs.search.brave.com/AdUkvT4xL9PdhqkMFPbp2tDYFd7GH9ejQJS8_c4BwcY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjIz/NTMzOTk3Ni92ZWN0/b3IvZ3JlYXQtcmVz/aWduYXRpb24tdHJl/bmQtZW1wbG95ZWUt/cXVpdHRpbmctam9i/LWFuZC1sZWF2aW5n/LWNvbXBhbnktYnVz/aW5lc3MtcGVvcGxl/LXdhbGsuanBnP3M9/NjEyeDYxMiZ3PTAm/az0yMCZjPUN0ZVpj/VEZUT2o4ejh2Wmww/a3JOektweW1ua0R6/UTdWaXE4U3RKVERF/ZDQ9")

st.sidebar.image("https://imgs.search.brave.com/1NjKNCJLYkxjPLrKnWVPWI9kpKaExy3iB_VnIqxTbJc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wNDYv/ODYxLzY0Ny9zbWFs/bC9nb29nbGUtbG9n/by10cmFuc3BhcmVu/dC1iYWNrZ3JvdW5k/LWZyZWUtcG5nLnBu/Zw")

from streamlit_extras.bottom_container import *
with bottom():
    st.markdown("---")
    st.caption("Made by Tanu Verma")
    st.sidebar.write("More about [Tanu Verma](https://github.com/Tanu-v)")
    st.sidebar.write("Contact Tanu Verma by [email](tanuv511@gmail.com)")

    st.caption("@2026| All Rights Reserved")
    st.sidebar.markdown("---")
    st.sidebar.caption("Made by Tanu Verma")
    st.sidebar.markdown("---")
    st.sidebar.caption("@2026| All Rights Reserved")


#Basic information section
st.header("📂 :blue[Basic Information]")

name=st.text_input("Full Name",placeholder="Enter your Full name",key="name",help="Like - John Doe")

age = st.number_input("Age",min_value=18,max_value=50,step=1,key="age")

mail = specialized_text_input("Gmail",suffix="@gmail.com",placeholder="Gmail",key="gmail",help="Enter your gmail id without '@gmail.com'")

q1=st.selectbox("1. What department did you work in? ", ["Sales", "Business Development", "Marketing / Communications", "Engineering / Technology / IT", "Customer Support / Client Success", "Operations / Logistics", "Human Resources / Recruitment", "Finance / Accounting", "Product / Design", "Other"] )

q2=st.selectbox("2. Length of Service (Tenure):",["Less than 6 months", "6–12 months", "1–2 years", "3–5 years", "5+ years"])

q3=st.selectbox("3. Job Level:", ["Entry-level / Associate", "Mid-level / Professional", "Senior-level / Specialist", "Manager / Director / Executive"])

#Primary reason for leaving
st.header(" :blue[Primary Reason for Leaving]")

q4=st.selectbox("4. What is your primary reason for leaving the organization? (Select one) 🎯",["Better compensation/salary elsewhere", "Lack of career advancement or growth opportunities", "Dissatisfaction with management or leadership", "Poor company culture or work environment", "Desire for better work-life balance / less burnout", "Inadequate training or resources to do the job", "Career pivot (changing industries or fields)", "Personal reasons (relocation, health, family, retirement)"])

q5=st.text_area("5. Please feel free to elaborate on your reason for leaving: ✍️")

#Employee Experience
st.header("⭐ :blue[Employee Experience]")

st.warning("For questions 6–9, please rate your agreement on a scale of 1 to 5:(1 = Strongly Disagree, 2 = Disagree, 3 = Neutral, 4 = Agree, 5 = Strongly Agree)")

q6=st.slider("6. I had the necessary tools, resources, and clear role expectations. ",1,5)

q7=st.slider("7. My supervisor provided clear goals, consistent support, and feedback. ",1,5)

q8=st.slider("8. I felt valued, included, and able to maintain a healthy work-life balance. ",1,5)

q9=st.slider("9. The company provided transparent opportunities for career growth.  ",1,5)

# Compensation & Market Outlook
st.header("💰 :blue[Compensation & Market Outlook]")

q10=st.selectbox("10. How do you view your overall salary and benefits package compared to market competitors?", ["Well above market average", "Competitive / Meets market average", "Below market average", "Unsure"])

#🔮 Future Outlook & Open Feedback
st.header("🔮 :blue[Future Outlook & Open Feedback]")

q11=st.selectbox("11. Would you recommend this company to a friend or colleague as a good place to work?",["Yes, definitely", "Maybe / Neutral", "No, I would not"])

q12=st.text_area("12. What is the single most important change this organization needs to make to improve employee retention?")

q13=st.text_area("13. Is there anything else you would like to share about your experience with us?")

if st.button("Submit Survey"):
    response={
        "Full Name": name,
        "Age": age,
        "Gmail": mail,
        "Q1: Department": q1,
        "Q2: Tenure": q2,
        "Q3: Job Level": q3,
        "Q4: Primary Reason": q4,
        "Q5: Reason Elaboration": q5,
        "Q6: Tools & Expectations": q6,
        "Q7: Supervisor Support": q7,
        "Q8: Value & Balance": q8,
        "Q9: Career Growth": q9,
        "Q10: Market Comp": q10,
        "Q11: Recommend Company": q11,
        "Q12: Retention Change": q12,
        "Q13: Open Comments": q13,
    }
    file_name = "Feedback.csv" # it's not the csv file of the above variable
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)

    else :
        df = pd.DataFrame()

    df = pd.concat([df,pd.DataFrame([response])],ignore_index=True)
    df.to_csv(file_name)
    st.success("Your Survey is submitted!!")
    st.balloons()
    rain(
        emoji="🌞",
        font_size=40,
        falling_speed=5,
        animation_length="infinite",

    )
    st.download_button("Download your file",data=df.to_csv(index=False),file_name='Feedback.csv',mime="text/csv")

