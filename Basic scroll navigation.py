from streamlit_extras.scroll_to_element import *

import streamlit as st

"""Example: Basic scroll navigation."""
st.write("Click the buttons to scroll to different sections of the page.")

# Navigation buttons at the top
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Go to Introduction", key="nav_intro"):
        scroll_to_element("intro_section")
with col2:
    if st.button("Go to Name Input", key="nav_name"):
        scroll_to_element("name_input")
with col3:
    if st.button("Go to Middle Section", key="nav_middle"):
        scroll_to_element("middle_section")
with col4:
    if st.button("Go to Conclusion", key="nav_conclusion"):
        scroll_to_element("conclusion_section")

# Create sections with keys using containers
with st.container(key="intro_section"):
    st.header("Introduction")
    st.write(
        "This example demonstrates how to scroll to elements by their key. "
        "Click the buttons above to navigate between sections."
    )

# Add some spacer content
for i in range(10):
    st.write(f"Content block {i + 1}")

with st.container(key="middle_section"):
    st.header("Middle Section")
    st.text_input("Enter your name", key="name_input")
    st.write("This is the middle of the page with a text input.")

for i in range(10):
    st.write(f"More content {i + 1}")

with st.container(key="conclusion_section"):
    st.header("Conclusion")
    st.write("You've reached the end of the page!")