import streamlit as st

#Child Learning Platform

st.title(" ***🧮CHILD SHEETS*** ")
st.warning(""" ## *This is a child learning site*""")
st.image("https://imgs.search.brave.com/TEQhCoyLMNv6PQWQApVuL1Rqv16nPMnUXbRd7clLwRA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/bWFnbmlmaWMuY29t/L2ZyZWUtcGhvdG8v/ZGl2ZXJzZS1raWRz/LXJlYWRpbmctYm9v/a3NfNTM4NzYtMTQ2/NDA2LmpwZz9zZW10/PWFpc19oeWJyaWQm/dz03NDAmcT04MA")

st.sidebar.title(" ***🧮CHILD SHEETS*** ")
p1 = st.Page("alpha.py", title="Alphabets", icon="🔠")
p2 = st.Page("num.py",title="Numbers", icon="🔢")
p3 = st.Page("shape.py", title="Shapes", icon="🟨")
p4 = st.Page("color.py", title="Colors", icon="🫟")


page = st.navigation([p1,p2,p3,p4])

page.run()


