from streamlit_extras.scroll_to_element import *

"""Example: Compare smooth and instant scrolling."""
st.write("Compare different scroll behaviors.")

with st.container(key="scroll_target"):
    st.header("Target Element")
    st.info("This is the target element for scrolling.")

for i in range(15):
    st.write(f"Spacer content line {i + 1}")

st.subheader("Scroll Options")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Smooth scroll", key="smooth_btn"):
        scroll_to_element("scroll_target", scroll_mode="smooth")

with col2:
    if st.button("Instant scroll", key="instant_btn"):
        scroll_to_element("scroll_target", scroll_mode="instant")

with col3:
    if st.button("Align to top", key="center_btn"):
        scroll_to_element("scroll_target", alignment="start")