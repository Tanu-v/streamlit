import streamlit as st

#Homework19:date-06/07/26

st.markdown("""
            <style>
            [data-testid="stHeaderElement"]:has(div[data-keyslot="my_header"]){
              
              background-color: yellow;
              color: blue;
              font-family:'Times New Roman',Times, serif;
              border: 1px solid black;
              padding: 5px;
              font-size: 41px;
            
            }
            </style>
            """,
              unsafe_allow_html=True)

st.header("Indian Spices", key = "my_header")

st.html("""
        <h1 style='font-size:50px; color:purple;font-family:serif;border:solid black 2px;padding:20px;'>Key Spices in Indian Cooking</h1>
        <p style='font-size:20px;'>Indian cooking relies on a sophisticated layering of spices, utilizing both whole and ground forms to build complex flavor profiles.  The choice between whole and ground is critical: whole spices are typically tempered in hot oil (tadka) at the start to infuse the base, while ground spices are added later to form the body of the gravy.</p>
        
        <img src='https://m.media-amazon.com/images/G/31/Amazon-Global-Selling-IN/Spices_export.jpeg' alt='Indian Spices' style='width:900px;height=800px;'>
""")

st.sidebar.title(" :blue[Key Spices in Indian Cooking]")
st.sidebar.markdown("---")
st.sidebar.image("https://zofffoods.com/cdn/shop/articles/Indian_Spices_List_for_Everyday_Cooking_Zoff_png_76d282b6-ff58-4429-8709-5e696a49f642.png?v=1781702467")
st.sidebar.markdown("---")
st.markdown("---")
sb = st.sidebar.selectbox("Select one to see:",["Whole Spices","Ground Spices","The Art of Layering"])

if sb == "Whole Spices":
    st.html("""
       <h1 style='color:green;font-size:40px;'>1. Whole Spices (Sabut Masale)</h1>
       
       <p style='font-size:20px;'>Whole spices are the foundation of Indian aromatics. Because their essential oils are locked inside their cellular structure, they must be fried in hot oil or ghee—a technique called Tempering or Tadka—to release their full fragrance. They provide a subtle, background depth and are often removed before serving, except in rice dishes. </p>
       
       <h2 style='color:green;font-size:35px;'>Cumin Seeds (Jeera)</h2>
       
       <p style='font-size:20px;'>These small, elongated brown seeds are the most common starting point for North Indian cooking. When fried in hot oil until they sizzle and darken slightly, they release a nutty, earthy aroma that forms the base for dishes like Dal Tadka and Jeera Rice. They are crucial for digestion and add a warm, citrusy undertone. </p>
       
       <h2 style='color:green;font-size:35px;'>Mustard Seeds (Rai)</h2>
       
       <p style='font-size:20px;'>Tiny, round spheres that come in black (pungent) or yellow (mild) varieties. Essential in South Indian and Bengali cuisines, they must be heated until they violently "pop" or crackle in the oil. This popping action releases a sharp, nutty flavor critical for dishes like Sambar, Rasam, and various vegetable stir-fries. </p>
       
       <h2 style='color:green;font-size:35px;'>Cardamom (Elaichi)</h2>
       
       <p style='font-size:20px;'>Known as the "Queen of Spices," it comes in two distinct types. Green Cardamom pods are small and spindle-shaped, offering an intensely floral, sweet, and cooling flavor used in sweets (Kheer), chai, and light curries. Black Cardamom pods are large, dark, and wrinkled, providing a smoky, camphor-like depth essential for heavy meat dishes like Rogan Josh and biryanis. Both are lightly crushed before frying to release their seeds. </p>
       
       <h2 style='color:green;font-size:35px;'>Cinnamon (Dalchini) & Cloves (Laung)</h2>
       
       <p style='font-size:20px;'>Often used together, these spices add sweet, woody warmth. Indian cinnamon (Cassia) comes in thick, rough bark sticks, while cloves are small, nail-shaped dried buds. They are fried briefly in oil at the start of cooking to infuse the fat with intense aroma, key for Biryani, Pulao, and rich gravies. Cloves also provide a mild numbing sensation if bitten into. </p>
       
       <h2 style='color:green;font-size:35px;'>Bay Leaves (Tej Patta)</h2>
       
       <p>Unlike Western bay leaves, Indian bay leaves (from the Cassia tree) have a subtle aroma reminiscent of cinnamon and cloves. They are added whole to hot oil or boiling water at the beginning of cooking to impart a background fragrance to rice and stews. Due to their tough texture, they are typically removed before serving.</p>
       
       <h2 style='color:green;font-size:35px;'>Fenugreek Seeds (Methi Dana)</h2>
       
       <p style='font-size:20px;'>These small, hard, yellowish-brown angular seeds have a strong, bitter taste if raw but transform into a sweet, maple-like aroma when toasted. They are used sparingly in pickles and tempering. Their dried leaf form, Kasuri Methi, is crushed over finished dishes like Butter Chicken for a distinct savory scent.</p>
       
       <h2 style='color:green;font-size:35px;'>Fennel Seeds (Saunf)</h2>
       
       <p style='font-size:20px;'>Small, pale green seeds with a sweet, licorice-like flavor. They are a staple in Kashmiri cuisine (e.g., Rogan Josh) and Gujarati cooking, where they balance heat and provide a cooling effect. They are often fried in oil at the start or served as a mouth freshener after meals.</p>
       
       <h2 style='color:green;font-size:35px;'>Nigella Seeds (Kalonji)</h2>
       
       <p style='font-size:20px;'>Tiny, matte black, tear-drop shaped seeds that taste of onions and oregano. They are not related to black cumin. They are commonly sprinkled on Naan bread before baking or fried in oil for Bengali dishes (like the Panch Phoron blend) and pickles to add a savory, oniony note without using actual onions.</p>
       
       <h2 style='color:green;font-size:35px;'>Black Peppercorns (Kali Mirch) & Star Anise (Chakra Phool) </h2>
       
       <p style='font-size:20px;'>Black peppercorns are small, wrinkled spheres that add a sharp, piney heat distinct from chilies; they are often crushed and fried or ground fresh. Star Anise is a star-shaped woody pod with a strong licorice flavor, used in rich meat curries and biryanis for its intense aroma and visual appeal. Both are typically added at the beginning of cooking. </p>
       
    
    
    """)

elif sb == "Ground Spices":
    st.html("""
          <h1 style='color:green;font-size:40px;'>2. Ground Spices (Pisi Huye Masale)</h1>
          
          <p style='font-size:20px;'>Ground spices form the "body" and color of the dish. Because their surface area is exposed, they burn easily and lose potency quickly. They are typically added after the onions and tomatoes have softened, often with a splash of water to prevent scorching.

         </p>
         
         <h2 style='color:green;font-size:35px;'>Turmeric (Haldi)</h2>
         
         <p style='font-size:20px;'>A bright yellow-orange powder with an earthy, musky, and slightly bitter flavor. It is added early in the cooking process, usually with onions and tomatoes, to cook out its raw smell. Turmeric provides the signature golden hue to almost all Indian curries, rice, and lentils, and acts as a natural antiseptic. </p>
         
         <h2 style='color:green;font-size:35px;'>Coriander Powder (Dhania)</h2>
         
          <p style='font-size:20px;'>Made from dried coriander seeds, this pale yellowish-brown powder has a citrusy, sweet, and floral taste. It is the primary thickening agent for gravies and makes up the bulk of most curry powders. Added after turmeric, it balances the heat of chilies and adds a mild, nutty body to dishes like Chana Masala and Aloo Gobi. </p>
         
         <h2 style='color:green;font-size:35px;'>Red Chili Powder & Kashmiri Chili Powder</h2>
         
          <p style='font-size:20px;'>Standard Red Chili Powder provides intense heat and a deep red color. Kashmiri Chili Powder is a specific variety prized for its vibrant scarlet color but mild heat. It is essential for achieving the rich red look of Tandoori Chicken and Rogan Josh without making the dish unbearably spicy. These are added mid-cooking with turmeric and coriander. </p>
         
         <h2 style='color:green;font-size:35px;'>Cumin Powder (Jeera)</h2>
         
          <p style='font-size:20px;'>Ground cumin has a more concentrated, earthy flavor than its whole counterpart but lacks the same aromatic lift. It is often added to marinades, dry vegetable dishes (Sabzi), and cooling yogurt dips (Raita) where the texture of whole seeds might be undesirable. </p>
         
         <h2 style='color:green;font-size:35px;'>Garam Masala</h2>
         
          <p style='font-size:20px;'>This is a complex blend of warming spices (cinnamon, cloves, cardamom, black pepper, cumin) ground together. Unlike other powders, it is added at the very end of cooking or sprinkled on top before serving. Cooking it for too long causes its volatile essential oils to evaporate, losing its signature high-note aroma. It is the finishing touch for dishes like Butter Chicken and Dal Makhani. </p>
         
         <h2 style='color:green;font-size:35px;'>Amchur (Dry Mango Powder)</h2>
         
          <p style='font-size:20px;'>A pale beige powder made from dried unripe green mangoes. It adds a sharp, tangy, and fruity sourness to dishes without introducing liquid (unlike lemon juice or tamarind). It is commonly used in dry snacks like Aloo Tikki, Chana Masala, and street food chaats. </p>
         
         <h2 style='color:green;font-size:35px;'>Ginger Powder (Saunth)</h2>
         
          <p style='font-size:20px;'>Made from dried ginger, this light brown powder has a concentrated, spicy warmth. It is used in specific regional dishes (like Kashmiri curries) and lentil preparations like Dal Makhani where fresh ginger might alter the texture or spoil faster. </p>
         
         <h2 style='color:green;font-size:35px;'>Chaats Masala</h2>
         
         <p style='font-size:20px;'>A greyish-brown blend containing dried mango powder, black salt, cumin, and other spices. It has a distinctive salty, sour, and sulfurous (from black salt) flavor. It is never cooked; instead, it is sprinkled raw over finished snacks, fruits, and salads like Pani Puri to provide an instant tangy kick. </p>
          
            """)

else:
    st.html("""
       <h1 style='color:green;font-size:40px;'>The Art of Layering</h1>
       
       <p style='font-size:20px;'>Authentic Indian flavor comes from the specific order of operations: </p>
       
       <p style='font-size:20px;'>1.Infuse: Start by frying Whole Spices in hot oil to flavor the fat. </p>
       
       <p style='font-size:20px;'>2.Sauté: Add aromatics (onions, ginger, garlic) and cook until golden. </p>
       
       <p style='font-size:20px;'>3.Bloom: Lower the heat and add Ground Spices (Turmeric, Coriander, Chili). Fry briefly ("Bhuna") until the oil separates from the masala, ensuring the raw taste is cooked out. </p>
       
       <p style='font-size:20px;'>4.Simmer: Add main ingredients and liquid. </p>
       
       <p style='font-size:20px;'>5.Finish: Turn off the heat and sprinkle Garam Masala and fresh herbs to trap the final aromas. </p>
       
       <p style='font-size:20px;'>Note on Potency: Ground spices are significantly more potent by volume than whole spices. If a recipe calls for whole spices and you must substitute with ground, use half the amount. For the best flavor, buy whole spices and grind them fresh in small batches, as ground spices lose up to 70% of their aroma within six months. </p>
    
    """)
st.sidebar.space("small")
st.sidebar.markdown("---")
st.sidebar.caption("Developed by Tanu Verma")
st.sidebar.html(" <a href='https://github.com/Tanu-v'>More about Tanu Verma</a>")
st.sidebar.caption("@2026 | All Rights Reserved")