import streamlit as st
from plotly.graph_objs.layout.ternary import aaxis

#st.markdown("Personal Information")
st.header("Top Wear ")
st.info("This page tells what kind of top to wear in which kind of situations.")
st.sidebar.markdown("Top Wear")

st.success("""
         # Professional Tops Guide for Women

Discover the best professional tops tailored to your industry, helping you look confident, stylish, and workplace-ready.

## Corporate & Finance (Formal Business)

### Structured Button-Down Blouses

Choose high-quality cotton or silk blouses in timeless neutral shades such as white, light blue, and navy for a polished corporate appearance.

### Tailored Peplum Tops

A structured peplum silhouette creates a refined and modern look that pairs beautifully with formal trousers and blazers.

### Mock Neck Shell Tops

Perfect for layering under suits and blazers, offering sophistication without adding bulk.

---

## Creative Fields (Marketing, Design & Media)

### Asymmetrical Tunics

Make a subtle creative statement while maintaining professionalism and elegance.

### Bold Prints & Textured Tops

Experiment with geometric patterns, satin finishes, and premium knit fabrics to express your personal style.

### Oversized Blazers as Tops

Wear a structured oversized blazer over a simple camisole for a fashionable and confident look.

---

## Tech & Startups (Smart Casual)

### Premium Knit Polos

A sophisticated alternative to basic t-shirts, providing a clean and smart-casual appearance.

### Silk or Chiffon Blouson Tops

Versatile and stylish, these tops can easily transition from casual meetings to professional presentations.

### Fine-Gauge Cardigans

Buttoned-up cardigans worn as standalone tops create a comfortable yet polished outfit.

---

## Healthcare & Education (Practical & Approachable)

### Soft Wrap Tops

Comfortable for long working hours while maintaining a professional and flattering silhouette.

### Breathable Linen-Blend Shirts

Lightweight and practical, ideal for active work environments while remaining stylish.

### Patterned Shell Tops

Subtle florals, dots, or soft patterns create a warm and approachable appearance for interacting with students, patients, or clients.
  
           
          """ )


st.info("""

# Top wear suggession video
### check out the video given below:-

""")

st.video("https://youtu.be/YHoTjuH_vuA")

