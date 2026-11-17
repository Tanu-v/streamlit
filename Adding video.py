import streamlit as st
# Adding video without encryption in mp4
st.header(" motivational Video")
st.video("D:\IMPORT FROM TAB\VID-20221114-WA0047.mp4")
st.title(" motivational Video")
st.header("dance video")
st.video("D:\IMPORT FROM TAB\VID-20221213-WA0007.mp4", start_time="1m03s")
#st.audio("C:\Users\TANU\Downloads\WhatsApp Ptt 2026-06-06 at 9.03.41 PM.ogg") need mp3
st.header("glimps of me")
st.image("D:\IMPORT FROM TAB\what's app images\IMG_20230522_100143.JPG")

st.image("D:\IMPORT FROM TAB\what's app images\IMG_20230507_224045_191.jpg")

# Peak python pattern we upload the video using rb , rb provide incription to video
v = open("D:\IMPORT FROM TAB\VID-20221213-WA0003.mp4","rb")

v1 = v.read()
st.video(v1)

#st.video("https://youtu.be/k-cFjRRLgA8")
st.image("http://youtube.com/post/UgkxPteboYLHf_DD_iwbLxS2g6iZrerL1dBK?si=qfclkYHkCP6m0C3a")
st.video("https://youtube.com/shorts/e6QBXlP-e28?si=l3rOUaGp1P2BJN1N")

insta ="https://www.instagram.com/reel/DZJjVIvNbwE/"
st.video(insta)

st.image("https://www.instagram.com/p/DZOm65PmdBA/")

left_col,center_col,right_col = st.columns([1,3,1080])
with right_col:
    st.video("https://youtu.be/k-cFjRRLgA8")