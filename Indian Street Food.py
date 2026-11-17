import streamlit as st

from streamlit_extras.resizable_columns import *

st.title("🍲 ***:blue[Indian Street Food]*** ")
st.markdown("---")
st.space("small")
st.warning("Indian street food relies on an intricate balance of five core taste pillars: spicy, sweet, sour, salty, and umami (often derived from dynamic textures and chaat masala). Roadside stalls (rehris or thelas) masterfully combine fresh textures—such as hot, deep-fried elements paired with chilled yogurt or crispy garnishes—to create instantly satisfying meals.")
st.markdown("---")
st.image("https://www.indianpanorama.co.uk/public/images/blog/1753552929.jpg")
st.markdown("---")
st.space("small")

#Steps or region in steps formate
from streamlit_extras.steps import *

st.header("📈 :blue[Roadmap]")
st.markdown("---")
r1,r2 = st.columns((1,4))

with r1:
    r = steps(["North India","West India","East & Northeast India","South India"],
    icons = range(1,5),
    key='region',
              )

with r2:
    with r[0]:
        st.warning("North India")
        st.write("""
            1. Golgappa ,
            2. Chole Bhature ,
            3. Tikki Amritsari ,
            4. Kulcha 
        
        """)
        if st.button("Next", key='next0'):
            r.next()

    with r[1]:
        st.warning("West India")
        st.write("""
             1. Vada Pav ,
             2. Pav Bhaji ,
             3. Bhel Puri ,
             4. Dhokla 
        
        """)
        if st.button("Previous",key='previous'):
            r.previous()
        if st.button("Next", key='next1'):
            r.next()

    with r[2]:
        st.warning("East & Northeast India")
        st.write("""
            1. Phuchka ,
            2. Jhal Muri ,
            3. Kathi Roll
        
        """)
        if st.button("Previous",key='previous2'):
            r.previous()
        if st.button("Next", key='next2'):
            r.next()

    with r[3]:
        st.warning("South India")
        st.write("""
            1. Masala Dosa ,
            2. Idli & Sambar ,
            3. Medu Vada ,
            4. Mirchi Bajji
        
        """)
        if st.button("Previous",key='previous3'):
            r.previous()
        if st.button("Reset", key='reset'):
            r.reset()

st.markdown("---")
st.space("small")

#Region in json editor

from streamlit_extras.json_editor import *
st.header("🌏 :blue[Region] ")
st.markdown("---")
st.write("This is an editable region json file.")
region_data = {"region1":"North India",
               "Number in index":1,
               "region2":"West India",
               "Number":2,
               "region3":"East & Northeast India",
               "number":3,
               "region4":"South India",
               "number index":4,
               "Dveloper":{"name":"Tanu Verma",
                          "email":"tanuv511@gmail.com",
                          "country":"India"},
               }
result = json_editor(region_data,
                     name="Region",
                     collapsed=False,
                     editable=True,
                     key="region_json",

                     )
st.write(" **Current Region** ")
st.json(result["data"])

st.markdown("---")
st.space("small")

#region sigma graph
from streamlit_extras.sigma_graph import *

st.header("🕸 :blue[Region networking graph] ")
st.markdown("---")
sg = {"nodes":[
    {"id":"north","label":"North India","size":20,"color":"green"},
    {"id":"west","label":"West India","size":11,"color":"red"},
    {"id":"east","label":"East&Northeast India","size":24,"color":"blue"},
    {"id":"south","label":"South India","size":21,"color":"yellow"},
          ],
     "edges":[
         {"source": "north", "target": "east", "id": "e1", "label": "Chickpea & Chaat base"},
         {"source": "north", "target": "west", "id": "e2", "label": "Potato & Butter use"},
         {"source": "west", "target": "south", "id": "e3", "label": "Coastal & Griddle style"},
         {"source": "east", "target": "south", "id": "e4", "label": "Rice foundation"},
         {"source": "north", "target": "south", "id": "e5", "label": "Pan-India popularity"},
         {"source": "west", "target": "east", "id": "e6", "label": "Street Roll evolution"},
         {"source": "west", "target": "east", "id": "e7", "label": "Puffed Rice & Sev variants"},
     ],
}

sigma_graph(sg,height=400)
st.markdown("---")
st.space("small")

st.sidebar.title("🍲 ***:blue[Indian Street Food]*** ")
st.sidebar.markdown("---")
st.sidebar.space("small")
st.sidebar.image("https://content.jdmagicbox.com/quickquotes/listicle/listicle_1734609788164_qvslp_2000x945.jpg?impolicy=queryparam&im=Resize=(847,400),aspect=fit&q=75")
st.sidebar.markdown("---")
st.sidebar.space("small")

sb = st.sidebar.selectbox("Choose the region :",["North India","West India","East & Northeast India","South India"])
if sb == "North India":
    st.header("🏛️ ***:blue[North India: The Land of Potatoes, Dairy, and Tandoor]*** ")
    st.markdown("---")
    st.warning("North Indian street food is characterized by its heavy use of wheat-based flatbreads, root vegetables (primarily potatoes), whole chickpeas, and cooling dairy elements like sweetened yogurt. Cooking methods rely heavily on deep-frying in massive woks (kadhais) or roasting at high temperatures in clay ovens (tandoors).")
    st.markdown("---")
    st.space("small")
    st.subheader(" ***:blue[1. Golgappa (The Northern Pani Puri)]*** ")
    st.markdown("---")
    st.write(""" 
          ***The Component Breakdown:***
          
          **The Crispy Shell:** Made using fine semolina (sooji) mixed with a small amount of refined flour. It is rolled exceptionally thin and deep-fried to create an incredibly rigid, brittle sphere that can hold liquid without collapsing.
          
          **The Internal Stuffing:** A cool filling consisting of boiled, cubed potatoes, boiled black chickpeas, and occasionally sprouted moong lentils, seasoned lightly with roasted cumin powder and black salt.
          
          **The Flavoured Water:** The shell is filled with Teekha Pani—a cold, refreshing elixir made by blending fresh mint leaves, coriander, fiery green chilies, ginger, dry mango powder (amchur), and lemon juice.
          
          ***The Flavor Experience:*** It is consumed in a single bite. The brittle shell shatters instantly, releasing a sudden, cold rush of sharp, herbaceous heat, balanced immediately by the starchy, neutral potato filling.
    
    """)
    st.markdown("---")
    st.image("https://imgs.search.brave.com/L-65knhZ5J3KiYSQnD6-pYpZ1R3Cm3JPVjuYGEPYnms/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9ob2dy/LmFwcC9ibG9nL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIzLzA2/L2ltYWdlLTIzLnBu/Zw")
    st.markdown("---")
    st.space("small")
    st.subheader(" ***:blue[2. Chole Bhature]*** ")
    st.markdown("---")
    st.write("""
          ***The Component Breakdown:***
          
          **The Curry (Chole):** Raw chickpeas (kabuli chana) are slow-stewed for hours with dry gooseberries (amla) or black tea bags to give them their characteristic deep charcoal-black color. They are simmered in a dense gravy of onions, tomatoes, ginger, and a pungent spice blend containing dried pomegranate seeds (anardana), nutmeg, and mace.
          
          **The Fried Bread (Bhatura):** Made from a highly elastic dough of refined flour (maida), curd, baking powder, and a touch of semolina. The dough is left to ferment for several hours, hand-stretched into a large oval shape, and dropped into smoking-hot oil.
          
          ***The Cooking Technique:***
          
           The bhatura must instantly balloon in the hot oil. This creates a dual texture: a micro-thin, golden, crispy exterior skin, and a soft, chewy, slightly sour internal crumb. It is served steaming hot with raw onions, green chili pickles, and a pat of butter on the curry.
    """)
    st.markdown("---")
    st.image("https://imgs.search.brave.com/39XQZfjKvJ2TiLZ7_ZpjHbvrE88ka4oVsGEGv_r7JpY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA1LzUzLzk4LzM3/LzM2MF9GXzU1Mzk4/MzcxM19mUFFBclBB/Tm9Lb3BqMlRtNDYy/MWVZQUExU1h5NDhx/dC5qcGc")
    st.markdown("---")
    st.subheader(" ***:blue[3. Aloo Tikki Chaat]*** ")
    st.markdown("---")
    st.write("""
           ***The Component Breakdown:***
           
           **The Potato Patty:** Large potatoes are boiled, grated, and mixed with green chilies, chopped ginger, and cornstarch or arrowroot powder to ensure maximum crispness. Some variations feature a hidden stuffing of spiced split yellow peas (chana dal).
           
           **The Cooking Technique:** The patties are slowly shallow-fried on a massive, concave iron skillet called a tawa. Vendors move the cooking patties to the elevated outer rim of the pan, allowing the oil to drain away while the dry heat turns the potato skin into a deeply caramelized, glass-like crunchy crust.
           
           **The Assembly:** The hot patty is crushed open on a plate to release steam. It is layered with hot chickpea curry, a generous dousing of chilled, sweet whisked yogurt, a vibrant green mint-coriander chutney, and a sweet, viscous dark maroon tamarind-date chutney.
           
    """)
    st.markdown("---")
    st.image("https://imgs.search.brave.com/9_2JxKLvWbc3V1VUu7_jluOfkKDca8IXuupT2l5JhRY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zaW5m/dWxseXNwaWN5LmNv/bS93cC1jb250ZW50/L3VwbG9hZHMvMjAy/My8wMy8zLTEuanBn")
    st.markdown("---")
    st.subheader(" ***:blue[4. Amritsari Kulcha]*** ")
    st.markdown("---")
    st.write("""
          ***The Component Breakdown:***
          
          **The Laminated Dough:** A highly technical dough made from refined flour that is rolled out, smeared generously with clarified butter (ghee), folded, and rolled out again multiple times. This creates dozens of microscopic, flaky layers.
          
          **The Stuffing:** A dry, fragrant mixture of raw mashed potatoes, grated paneer, finely chopped onions, green chilies, heavy amounts of coarsely crushed coriander seeds, and dry pomegranate seeds.
          
          **The Baking Technique:** The stuffed bread is slapped directly onto the internal, clay-lined walls of an intensely hot tandoor oven. Once it develops deep brown, blistered chars, the vendor pulls it out and aggressively crushes the hot kulcha between their palms to shatter the flaky sheets, before drowning it in melted butter.
    
    """)
    st.markdown("---")
    st.image("https://imgs.search.brave.com/StZhU5LMr3Efon6c3LjLSveD-19d4kdENFaTCl2drQ0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMjIx/MzUzNTU1MS9waG90/by9hbXJpdHNhcmkt/a3VsY2hhLWlzLWEt/Y3Jpc3B5LWZsYWt5/LXN0dWZmZWQtZmxh/dGJyZWFkLWZyb20t/cHVuamFiLWZpbGxl/ZC13aXRoLXNwaWNl/ZC1tYXNoZWQuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPUIw/cjBtQmdXb2NQaEVh/Q0NzenFlRmVTdFBS/Ymw4UzdPYThVZzc4/TzBfOTA9")
    st.markdown("---")

elif sb == "West India":
    st.header("🌊 ***:blue[West India: High-Speed, Portable, Griddle-Cooked Snacks]*** ")
    st.markdown("---")
    st.warning("Western Indian street food, centering around Maharashtra and Gujarat, is designed for a fast-moving coastal lifestyle. It relies heavily on soft leavened yeast buns (pav), dry chickpea noodles (sev), puffed rice, and sharp garlic-chili condiments.")
    st.markdown("---")
    st.space("small")
    sb1 = st.selectbox("Choose a dish:",["Vada Pav","Pav Bhaji","Bhel Puri","Dhokla"])
    if sb1 == "Vada Pav":
        rc0,rc1 = resizable_columns([1,2],border=True,key="rc1")
        with rc0:
            st.markdown("---")
            st.subheader(" ***:blue[1. Vada Pav (The Mumbai Street Icon)]*** ")
            st.markdown("---")
            st.write("""
                 ***The Component Breakdown:***
                 
                 **The Batata Vada:** A smooth potato mash tempered with crackled mustard seeds, curry leaves, minced garlic, green chilies, and vibrant yellow turmeric. This mash is hand-formed into a sphere, coated in a thick chickpea flour (besan) batter, and deep-fried.
                 
                 **The Pav:** A soft, unsweetened, pillowy white bread bun.
                 
                 **The Condiments:** The pav is slit open and painted with three distinct chutneys: a wet, spicy green chili paste; a sweet tamarind sauce; and a dry, fiery red garlic-and-coconut spice blend (ghati masala).
                 
                 ***The Flavor Experience:***
                  
                  A single deep-fried, salted green chili is tucked into the bun. The texture transitions smoothly from the soft, pillowy bread into the crunchy fried batter casing, concluding with a hot, garlicky punch.
                  
            """)

        with rc1:
            st.markdown("---")
            st.image("https://imgs.search.brave.com/jXCTlibq_0GqIFehW0CHmNOesVyTsCAjjW-UNy4SBEk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9ibG9n/LnN3aWdneS5jb20v/d3AtY29udGVudC91/cGxvYWRzLzIwMjQv/MTEvSW1hZ2UtMV9t/dW1iYWktdmFkYS1w/YXYtMTAyNHg1Mzgu/cG5n")
            st.markdown("---")

    elif sb1 == "Pav Bhaji":
        rc0, rc1 = resizable_columns([1, 2], border=True, key="rc2")
        with rc0:
            st.markdown("---")
            st.subheader(" ***:blue[2. Pav Bhaji]*** ")
            st.markdown("---")
            st.write("""
                    ***The Component Breakdown:***
                    
                    **The Bhaji (Mashed Curry):** A smooth, velvety curry made from boiled potatoes, cauliflower, green peas, onions, and tomatoes.
                    
                    **The Cooking Technique:** Cooked live on an enormous, flat iron griddle. The vendor continuously ladles water and uses a heavy metal hand-masher to pulverize the vegetables while adding a heavily aromatic spice mix dominated by coriander, cumin, fennel, cinnamon, and dry mango powder.
                    
                    **The Butter Saturation:** Massive blocks of salted butter are melted directly into the bubbling mash. The pav buns are split open and pressed onto the same buttery griddle until they turn completely golden brown and crispy on the edges. It is garnished with raw chopped red onions and a squeeze of lime juice.
           
            """)

        with rc1:
            st.markdown("---")
            st.image("https://imgs.search.brave.com/OxWjBtQi8Cy-TUVA-3aijs7r1gqD9VuR0ToC4uusLBQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9teWZv/b2RzdG9yeS5jb20v/d3AtY29udGVudC91/cGxvYWRzLzIwMjEv/MDkvUGF2LUJoYWpp/LTMuanBn")
            st.markdown("---")

    elif sb1 == "Bhel Puri":
        rc0, rc1 = resizable_columns([1, 2], border=True, key="rc3")
        with rc0:
            st.markdown("---")
            st.subheader(" ***:blue[3. Bhel Puri]*** ")
            st.markdown("---")
            st.write("""
                    ***The Component Breakdown:***
                    
                    **The Dry Base:** Crisp, unflavored puffed rice mixed with sev (crunchy, fine chickpea flour noodles) and papdi (flat, fried flour crackers broken into small bits).
                    
                    **The Wet Mix-ins:** Finely diced raw red onions, boiled potatoes, chopped tomatoes, and raw green mangoes (when in season).
                    
                    ***The Assembly Technique:***
                     This is an unheated dish assembled dynamically in seconds. The vendor tosses the dry base and wet ingredients into a metal vessel, splashing in three chutneys (sharp green mint, sweet tamarind, and spicy red garlic). It is mixed rapidly with a large spoon and served immediately in a paper cone. It must be eaten instantly before the puffed rice turns soggy.
            
            """)

        with rc1:
            st.markdown("---")
            st.image("https://imgs.search.brave.com/MpZFwGyk55ucczVIPi4Zl_40HJEQ1rFwpEekSnxcch8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzE2LzA0LzU1Lzcx/LzM2MF9GXzE2MDQ1/NTcxOTdfNDJTdkNz/cjNZSVNkWE54cVA0/TE5EaWY1VTFNbkFa/WHQuanBn")
            st.markdown("---")

    elif sb1 == "Dhokla":
        rc0, rc1 = resizable_columns([1, 2], border=True, key="rc4")
        with rc0:
            st.markdown("---")
            st.subheader(" ***:blue[Dhokla (Khaman Dhokla)]*** ")
            st.markdown("---")
            st.write("""
                 ***The Component Breakdown:***
                 
                 **The Batter:** Made from ground chickpea flour mixed with water, lemon juice, turmeric, and a small amount of semolina. A leavening agent (like fruit salt) is folded in at the very last second to introduce thousands of tiny air bubbles.
                 
                 **The Tempering (Tadka):** Once the batter is steamed into a large, spongy cake and sliced into cubes, a hot liquid tempering is poured over it. This liquid is made by boiling water with sugar, green chilies, mustard seeds, and fresh curry leaves.
                 
                 ***The Texture:***
                  
                  The spongy cake acts like a sponge, absorbing the sweet, sour, and spicy water. It is light, airy, moist, and served cold with fine sev and fresh coriander leaves.
            
            """)

        with rc1:
            st.markdown("---")
            st.image("https://imgs.search.brave.com/hnaSM4sbjOWKBYYTQo1tCBDOwqwQD3A1oHhEhAm-KE8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90aHVt/YnMuZHJlYW1zdGlt/ZS5jb20vYi9ndWph/cmF0aS1raGFtYW4t/ZGhva2xhLXN0ZWFt/ZWQtZ3JhbS1mbG91/ci1zbmFjay1pbmRp/YW4tY3Vpc2luZS1m/b29kLWNvbW1vbi1n/dWphcmF0LXN0YXRl/LWluZGlhLW1hZGUt/c29ha2VkLTExODc1/NzI0Ny5qcGc")
            st.markdown("---")


elif sb == "East & Northeast India":
    st.header("🌾 ***:blue[East & Northeast India: Pungent Oils and Himalayan Influences]*** ")
    st.markdown("---")
    st.warning("The eastern street food profile (anchored by Kolkata) leans heavily into the sharp, tongue-tingling heat of raw mustard oil, sour tamarind extractions, and paratha rolls. Further north, towards the Himalayan foothills, the cuisine shifts completely toward steamed dough structures and intensely hot chili chutneys.")
    st.markdown("---")
    st.space("small")
    st.subheader(" ***:blue[1. Phuchka (The Eastern Variant)]*** ")
    st.markdown("---")
    st.write("""
           ***How it differs from Golgappa:***
           
           **The Shell:** Considerably larger, thinner, darker, and crispier, made from a blend of whole wheat flour and semolina.
           
           **The Heavy Stuffing:** Unlike the mild northern potato filling, Phuchka features a hot, heavily mashed potato mix combined with boiled black chickpeas, green chili paste, roasted cumin-coriander powder, and a generous pour of raw, unheated mustard oil.
           
           **The Liquid:** The liquid is not mint-based. It is made strictly from thick, dark tamarind pulp water infused with fresh lime juice, black salt, and a crushed local chili spice mix. It is distinctly more sour, pungent, and fiery than its northern counterpart.
    """)
    st.markdown("---")
    st.image("https://imgs.search.brave.com/Nl-oG1LDtVZR49cQmwJL-bYxTlU8SpXGlDRWRsHgC6o/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/Y3JlYXRlLnZpc3Rh/LmNvbS9hcGkvbWVk/aWEvc21hbGwvNTI4/OTkwMDc4L3N0b2Nr/LXBob3RvLXBhbmlw/dXJpLWZ1Y2hrYS1m/aHVjaGthLWd1cGNo/dXAtZ29sZ2FwcGEt/cGFuaS1wYXRha2Ut/dHlwZS1zbmFjay1v/cmlnaW5hdGVk")
    st.markdown("---")
    st.space("small")
    st.subheader(" ***:blue[2. Jhal Muri]*** ")
    st.markdown("---")
    st.write("""
           ***The Component Breakdown:***
           
           **The Base:** Fresh, crisp puffed rice mixed with fried chickpea lentils (chanachur), roasted peanuts, and boiled potato cubes.
           
           **The Secret Ingredient:** A heavy splash of seasoned mustard oil taken directly from the top of a jar of pickled green chilies or mangoes.
           
           ***The Technique:***
            
            The ingredients are placed inside a tall cylindrical tin container and shaken aggressively with a metal spoon. The raw mustard oil coats every grain of puffed rice, creating a sharp, nasal-clearing heat. It is garnished with fresh coconut slices and served in a rolled-up newspaper cone (thonga).
            
    """)
    st.markdown("---")
    st.image("https://imgs.search.brave.com/CW-08MxRrw9Vi4iXCjh4ViVu1OOOiPisvgSmgfKPhhk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMuc3F1YXJlc3Bh/Y2UtY2RuLmNvbS9j/b250ZW50L3YxLzVl/YTVmMzkxM2IwY2Nm/MDZkMGVjMjU2My8x/NTkzNDQ1ODUwOTM4/LUtINFA0NzY2T1Y4/VFcyRFBPTVhWL0po/YWwrTXVyaSsoOSku/anBn")
    st.markdown("---")
    st.space("small")
    st.subheader(" ***:blue[3. Kathi Roll]*** ")
    st.markdown("---")
    st.write("""
          ***The Component Breakdown:***
          
          **The Paratha:** A layered flatbread made from refined flour. The dough is stretched, coiled tightly like a rope, and rolled out flat again to create thin, flaky layers. It is fried on a flat tawa with plenty of oil. Often, an egg is cracked and cooked directly onto one side of the paratha.
          
          **The Filling:** Skewered cubes of mutton, chicken, or paneer are marinated in a thick yogurt-tandoori spice blend and cooked over charcoal.
          
          **The Roll:** The hot filling is laid down the center of the egg-lined paratha, topped with thinly sliced raw onions, green chilies, and a squeeze of fresh lime juice. It is wrapped tightly in greaseproof paper for easy hand-held consumption. 
    
    """)
    st.markdown("---")
    st.image("https://imgs.search.brave.com/OB8CTLJVchYeZPiJ_BDAkE9ceTXw7t6Ky-tIiBf-_uI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9taW5p/c3RyeW9mY3Vycnku/Y29tL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDIwLzA1L2NoaWNr/ZW4ta2F0aGktcm9s/bHNfLTItODUweDEy/NzUuanBn")
    st.markdown("---")


elif sb == "South India":
    st.header("🌴 ***:blue[South India: Fermented Griddle Crepes and Lentil Fritters]*** ")
    st.markdown("---")
    st.warning("Southern street food is anchored by ancient fermentation techniques involving rice and split black lentils (urad dal). The flavors are characterized by the earthy notes of curry leaves, mustard seeds, fresh coconut, and sour tamarind-based lentil stews (sambar).")
    st.markdown("---")
    st.space("small")
    st.subheader(" ***:blue[1. Masala Dosa]*** ")
    st.markdown("---")
    st.write("""
            ***The Component Breakdown:***
            
            **The Fermented Batter:** Parboiled rice and split black lentils are soaked separately, stone-ground into a velvety smooth paste, and left to ferment naturally for 12 to 24 hours. The fermentation creates a light lactic acidity and natural carbonation.
            
            **The Griddle Technique:** A ladle of batter is poured onto a massive, seasoned cast-iron hot plate. Using the flat bottom of a metal bowl, the vendor spreads the batter outward in rapid, concentric circles until it is paper-thin. Ghee or butter is ladled around the edges, frying the underside to a deep mahogany-brown crisp.
            
            **The Potato Stuffing (Palya):** The center is packed with a dry mash of boiled potatoes tempered with mustard seeds, chana dal, sliced onions, ginger, green chilies, and turmeric. It is folded into a large cylinder and served with cool coconut chutney and hot, tangy sambar.
    
    """)
    st.markdown("---")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvmTZhnS01yNc3GK6HYuCpJFiLU8au90D2B3MFn7gKlFt0AEBzKjjYFMOz&s=10")
    st.markdown("---")
    st.space("small")
    st.subheader(" ***:blue[2. Idli & Sambar]*** ")
    st.markdown("---")
    st.write("""
            ***The Component Breakdown:***
            
            **The Idli:** A batter similar to dosa, but ground slightly coarser with a higher ratio of rice to lentils. The batter is ladled into specialized perforated, concave molds and steamed. The result is a pillowy, soft, airy rice cake that is completely fat-free.
            
            **The Sambar:** A hot, comforting lentil-based vegetable stew cooked with pigeon peas (toor dal), tamarind pulp, pumpkin, okra, and a toasted spice paste of coriander seeds, fenugreek seeds, dry red chilies, and asafoetida (hing). The idlis are often served completely submerged in a bowl of hot sambar.
    
    """)
    st.markdown("---")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5R7aMsXuSwsP2jl7k9X8W6aQYbi87YWTgcMCv2VPgh_6DwaFTtNq12W8&s=10")
    st.markdown("---")
    st.space("small")
    st.subheader(" ***:blue[3. Medu Vada]*** ")
    st.markdown("---")
    st.write("""
            ***The Component Breakdown:***
            
            **The Batter:** Split black lentils are soaked and ground with a minimal amount of water to create an incredibly thick, aerated paste. The paste is beaten vigorously by hand to trap air, then mixed with whole black peppercorns, curry leaves, ginger, and finely chopped green chilies.
            
            **The Shaping Technique:** The vendor wets their palms, takes a ball of the sticky batter, uses their thumb to punch a clean hole right through the center, and slides it smoothly into a vat of hot oil.
            
            **The Final Texture:** It fries into a savory, donut-shaped fritter. The high air content in the batter causes the inside to remain light, fluffy, and cake-like, while the exterior forms a deep golden, crunchy crust.
    
    """)
    st.markdown("---")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMkQLt5zEOx4aWd6tZWAZnlEtyxzhy_rGmCRcuqZrXyUDGcXQoMMkZBJg&s=10")
    st.markdown("---")
    st.space("small")
    st.subheader(" ***:blue[4. Mirchi Bajji]*** ")
    st.markdown("---")
    st.write("""
           ***The Component Breakdown:***
           
           **The Chili:** Large, thick, mild green banana chilies (bhavnagari mirchi) are selected for their low heat profile and high flesh content.
           
           **The Stuffing:** The chilies are slit down the center and deseeded. They are stuffed with a tangy paste made of tamarind pulp, carom seeds (ajwain), salt, and roasted cumin powder.
           
           **The Fry:** The stuffed chili is dipped into a thick, seasoned chickpea flour batter and deep-fried. Once fried, vendors often slit the hot bajji open once more, stuffing it with a raw mix of finely chopped red onions, fresh coriander, and a heavy squeeze of lemon juice.
    
    """)
    st.markdown("---")
    st.image("https://yummyindiankitchen.com/wp-content/uploads/2016/07/Mirchi-bajji-mirapakaya-bajji.jpg")
    st.markdown("---")


st.sidebar.markdown("---")
st.sidebar.space("small")

st.sidebar.caption("developed by Tanu Verma")
st.sidebar.html(" <a href='https://github.com/Tanu-v'>More about Tanu Verma</a>")
st.sidebar.caption("@2026 | All Rights Reserved")

