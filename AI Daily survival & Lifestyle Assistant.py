import streamlit as st

# Making A lifestyle & Daily need hacks AI Assistant
st.title("AI Daily survival & Lifestyle Assistant")

#Personal information for making it realistic
st.header("User Information")
st.info("Please provide your personal details for making it more realistic and for better experience")
name = st.text_input("Full Name")

age = st.number_input("Age", min_value=16, max_value=100)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

location = st.text_input("Location")

budget = st.selectbox(
    "Monthly Budget",
    ["Under ₹5,000", "₹5,000-₹15,000", "₹15,000-₹30,000", "Above ₹30,000"]
)

interest = st.selectbox(
    "Select Topic",
    [
        "Cloth Collection",
        "Dress Styling",
        "Occasion Wear",
        "Accessories Styling",
        "How To Bargain",
        "Daily Need Skills",
        "5 Minute Food",
        "Low Budget Survival",
        "Other"
    ]
)
# Add contact info


if st.button("Submit"):


  if interest == "Cloth Collection":

    st.subheader("Build Your Wardrobe")

    st.success("""
    Essential Clothing Collection:

    • White Shirt
    • Black T-Shirt
    • Blue Jeans
    • Formal Trousers
    • Casual Sneakers
    • Traditional Wear
    • Black Blazer
    • Comfortable Daily Wear

    These pieces can create multiple outfits.
    """)

    st.header("Fashion Learning Video")

    st.video("https://youtu.be/uzjYzPmi6Fo")

  elif interest == "Dress Styling":

    st.subheader("How To Style Your Clothes")

    st.success("""
    Styling Tips:

    • Balance loose and fitted clothing.
    • Match colors wisely.
    • Layer outfits for a premium look.
    • Keep footwear clean.
    • Use accessories moderately.
    """)

    st.info("""
    Formula:
    Basic Outfit + Layer + Accessories
    = Stylish Look
    """)

    st.video("https://youtu.be/Jh65uUdLCZM")

  elif interest == "Occasion Wear":

    st.subheader("What To Wear On Different Occasions")

    occasion = st.selectbox(

        "Select Occasion",
        [
            "Wedding",
            "Interview",
            "Party",
            "College",
            "Office",
            "Date"
        ]
    )

    if occasion == "Wedding":
        st.write("""
        • Ethnic Wear
        • Suit or Saree
        • Traditional Accessories
        """)
        st.video("https://youtu.be/UkbyyvysDbU")

    elif occasion == "Interview":
        st.write("""
        • Formal Shirt
        • Formal Trousers
        • Professional Shoes
        """)
        st.video("https://youtu.be/N9ABtfXD9co")

    elif occasion == "Party":
        st.write("""
        • Smart Casual Outfit
        • Stylish Footwear
        • Watch
        """)

    st.video("https://youtu.be/uPQx2zs-nN4")


  elif interest == "Accessories Styling":

    st.subheader("How To Style Accessories")

    st.success("""
    Accessories Guide:

    • Watches
    • Belts
    • Sunglasses
    • Handbags
    • Jewelry
    • Scarves

    Choose accessories according to outfit color and occasion.
    """)

    st.video("https://youtu.be/VoaUOAklIVg")

  elif interest == "How To Bargain":

    st.subheader("Smart Bargaining Skills")

    st.success("""
    Bargaining Techniques:

    • Never accept first price.
    • Compare prices from multiple shops.
    • Stay polite and confident.
    • Ask for combo discounts.
    • Carry cash when possible.
    """)

    st.info("""
    Example:

    Seller: ₹1000
    You: Can you do ₹700?
    Negotiate gradually.
    """)

    st.video("https://youtu.be/AGKfseCbV60")

  elif interest == "Daily Need Skills":

    st.subheader("Essential Life Skills")

    st.success("""
    Learn:

    • Time Management
    • Communication Skills
    • Basic Cooking
    • Personal Finance
    • Public Speaking
    • First Aid Basics
    • Digital Skills
    """)

    st.video("https://youtu.be/fieU6Cvwz4c")

  elif interest == "5 Minute Food":

    st.subheader("Quick Food Ideas")

    st.success("""
    Ready In 5 Minutes:

    • Sandwich
    • Poha
    • Instant Oats
    • Fruit Bowl
    • Egg Toast
    • Peanut Butter Bread
    • Yogurt Bowl
    """)

    st.video("https://youtu.be/IFVC1Jp9G-Q")

  elif interest == "Low Budget Survival":

    st.subheader("Living Smart On A Budget")

    st.success("""
    Budget Tips:

    • Track every expense.
    • Cook at home.
    • Use public transport.
    • Buy essentials in bulk.
    • Avoid impulse purchases.
    • Follow 50-30-20 rule.
    """)

    if budget == "Under ₹5,000":
        st.warning("""
        Focus on:
        • Home-cooked food
        • Free learning resources
        • Essential purchases only
        """)

    st.video("https://youtu.be/cKwwG_o2z2k")

if st.button("Get More Suggestions"):
    st.success(
        f"Thank you {name}! Explore the recommendations and videos above."
    )
