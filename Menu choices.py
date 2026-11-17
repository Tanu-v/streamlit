import streamlit as st
from streamlit_extras.radial_menu import radial_menu

# 1. Define your menu choices
menu_selection = radial_menu(
    options={
        "home": "🏠",
        "analytics": "📈",
        "external_site": "🔗",
    },
    key="nav_menu"
)

# 2. Handle routing based on selection
if menu_selection:
    selection = menu_selection.get("selection")

    if selection == "home":
        # Assumes a file named home.py exists in a pages/ directory
        st.switch_page("pages/home.py")

    elif selection == "analytics":
        st.switch_page("PythonProject\about.py")

    elif selection == "external_site":
        # External URLs need to be opened via link buttons
        st.link_button("Go to External Site", "https://example.com")