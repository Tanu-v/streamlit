import streamlit as st

st.info("""

# ***Pro Women Zone***
## *Empowering Professional Women Through Style, Confidence, and Well-Being.*

""")

p1 = st.Page("User Info.py", title="Personal Info",icon="👩‍💻")
p2 = st.Page("about.py", title="About",icon="👩🏼‍🏫")
p3 = st.Page("Top.py", title="Top Wear",icon="👚")
p4 = st.Page("Bottom.py", title="Bottom Wear",icon="👖")
p5 = st.Page("Dress.py", title="Dresses",icon="👗")
p6 = st.Page("Blazer.py", title="Blazer Wear",icon="🧥")
p7 = st.Page("Accessories.py", title="Accessories",icon="💍")
p8 = st.Page("Footwear.py",title="Footwear",icon="🥿")
p9 = st.Page("Anxiety Handling.py", title="Anxiety Handling",icon="💆‍♀️")

#mapping all in one place through navigation

page = st.navigation([p1,p2,p3,p4,p5,p6,p7,p8,p9])

page.run()



