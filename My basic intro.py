
import streamlit as st
import pandas as pd
st.title("Tanu Verma")

st.header("Data Scientist & AI Enthusiast | Content Creator | Technology Learner")

st.subheader("Turning data into insights and ideas into impact.")

st.markdown("""
Passionate about Data Science, Artificial Intelligence, Python, SQL, Power BI,
Data Visualization, and Digital Content Creation. I enjoy transforming data into
meaningful insights while creating engaging content that connects, informs, and inspires.

As a technology learner and content creator, I combine analytical thinking with creativity
to explore innovative solutions, communicate ideas effectively, and continuously grow in
the fields of AI, analytics, and digital innovation.
""")

# About Me Section
st.header("About Me")

st.markdown("""
I am a **Data Analytics & AI Enthusiast** passionate about transforming data into actionable insights and innovative solutions. My interests span **Python, SQL, Power BI, Data Visualization, Generative AI, and Prompt Engineering**.

Beyond technology, I am a **content creator** who enjoys sharing ideas, building communities, and communicating complex concepts in a simple and engaging way.

I believe in continuous learning, creativity, and using technology to create meaningful impact in the real world.
""")

st.success("Open to learning, collaboration, and exciting opportunities in Data Science and AI.")

st.info("Currently exploring Machine Learning, Generative AI, Prompt Engineering, and Advanced Analytics.")

st.warning("This portfolio is regularly updated with new projects, skills, and achievements.")

st.write(
    "Thank you for visiting my portfolio. Feel free to explore my projects, technical skills, certifications, and professional journey."
)

#Skills section
st.header("Skills")
x = (
    "Python",
    "SQL",
    "Power BI",
    "Machine Learning",
    "Data Visualization",
    "Streamlit",
    "Generative AI",
    "Prompt Engineering"
    "Deep Leaning",
    "Large Language Models (LLMs)",
    "Data preprocessing & analysis for AI models",
    "green skills",
    "Climate Change Adaptation",
    "Problem Solving"
)

y = (
    "Skill 1",
    "Skill 2",
    "Skill 3",
    "Skill 4",
    "Skill 5",
    "Skill 6",
    "Skill 7",
    "Skill 8",
    "Skill 9",
    "Skill 10",
    "Skill 11",
    "Skill 12",
    "Skill 13"

)

z = pd.DataFrame(x, index=y, columns=["Skills"])

st.dataframe(z)

#Education section
st.header("Education")

z = pd.DataFrame(
    {
        "Degree": ["BCA", "B.Com"],
        "College/University": [
            "Indira Gandhi National Open University (IGNOU)",
            "Hemchand Yadav Vishwavidyalaya, Durg (C.G.)"
        ],
        "Year": ["2023-2026", "2023-2026"],
        "Percentage": [">60%", ">55%"]
    }
)
st.dataframe(z, use_container_width=True)




st.header(" Certifications")
certifications = pd.DataFrame(
    {
        "Certificate": [
            "Data Analytics Certification",
            "Power BI Certification",
            "Python Certification",
            "AI/ML Certification"
        ],
        "Link": [
            "https://www.linkedin.com/in/tanu-verma-96595b32a/details/certifications/",
            "https://www.linkedin.com/in/tanu-verma-96595b32a/details/certifications/",
            "https://www.linkedin.com/in/tanu-verma-96595b32a/details/certifications/","https://www.linkedin.com/in/tanu-verma-96595b32a/details/certifications/"


        ]
    }
)



st.dataframe(certifications, use_container_width=True)




st.header(" Social Media & Professional Profiles")
social_media = pd.DataFrame(
    {
        "Social Media Platform": [
            "LinkedIn",
            "GitHub",
            "YouTube",
            "Instagram",
            "Portfolio Website"
        ],

        "Link": [
            "https://www.linkedin.com/in/tanu-verma-96595b32a/",
            "https://github.com/Tanu-v",
            "https://www.youtube.com/@i_tanuv",
            "https://www.instagram.com/just_.tanuu/",
            "https://yourportfolio.streamlit.app"
        ]
    }
)
st.dataframe(social_media, use_container_width=True)


st.header(" Languages Known")
languages = pd.DataFrame(
    {
        "Language": [
            "English",
            "Hindi"
        ]
    }
)

st.dataframe(languages, use_container_width=True)



st.header(" Contact Information")
contact_info = pd.DataFrame(
    {
        "Contact Method": [
            "Email",
            "LinkedIn",
            "GitHub",
            "Location"
        ],

        "Details": [
            "tanuv511@gmail.com",
            "https://www.linkedin.com/in/tanu-verma-96595b32a/",
            "https://github.com/Tanu-v",
            "Chhattisgarh, India"
        ]
    }
)
st.dataframe(contact_info, use_container_width=True)