import streamlit as st
from streamlit_extras.three_viewer import *

st.title("🏯 :blue[***Some Ancient Decoration rooms***]")
st.sidebar.title("🏯 :blue[***Some Ancient Decoration rooms***]")
st.sidebar.markdown("---")
st.sidebar.image("https://imgs.search.brave.com/3b5TPL1O_Hzo-Pp6F7kOkT1iF1-mrONAxzht4ZJA1r8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzFhL2Ux/LzlhLzFhZTE5YWIx/NTMwODA1Mjc3NDBl/MDg2M2FiOTgzZmM0/LmpwZw")
st.sidebar.markdown("---")
st.markdown("---")
cb = st.sidebar.selectbox("Choose to see:",["Drawing room","King's Hall","The Armoury","Morning room","Smoking room","Japanese temple"])

if cb == "Drawing room":
    st.header(" :green[The great Drawing room]")
    st.markdown("---")
    st.space("small")
    st.info("""
        A Great Drawing Room is a large, elegant reception room traditionally found in grand houses, palaces, and mansions. It was designed to receive guests, host social gatherings, and showcase the wealth and taste of the homeowner.

        ***Typical features include:***

**Spacious layout:** High ceilings and a large floor area that create an open, luxurious feel.

**Elegant furniture:** Plush sofas, armchairs, coffee tables, side tables, and decorative cabinets arranged for conversation.

**Grand lighting:** Crystal chandeliers, wall sconces, and table lamps provide both illumination and visual appeal.

**Rich décor:** Ornate mirrors, paintings, sculptures, vases, carpets, curtains, and decorative moldings enhance the room's sophistication.

**Fireplace (in traditional designs):** Often serves as the focal point, with a mantel displaying artwork or decorative objects.

**Premium materials:** Marble, polished wood, velvet, silk, brass, and crystal are commonly used for floors, furniture, and accessories.

**Large windows:** Tall windows with luxurious drapes allow natural light while adding elegance.

**Symmetrical arrangement:** Furniture and decorations are often placed symmetrically to create a balanced, formal appearance.

**Entertainment purpose:** Historically used for receiving visitors, hosting tea parties, musical performances, or formal conversations.

Overall, a great drawing room conveys luxury, comfort, and sophistication, blending fine architecture with tasteful furnishings to create an impressive space for entertaining guests.
    
    """)
    st.markdown("---")
    st.space("small")

    m1 = (r"C:\Users\TANU\Downloads\the_great_drawing_room.glb")
    three_viewer(m1, height=400, key="3D_1")
    st.caption("drag it to see in 3D mode")


elif cb == "King's Hall":
    st.header(" :green[The great King's Hall]")
    st.markdown("---")
    st.space("small")
    st.info("""
             A King's Hall (also called the Great Hall or Royal Hall) is the principal ceremonial room in a castle, palace, or royal residence. It served as the heart of royal life, where the king held court, welcomed distinguished guests, celebrated important occasions, and conducted official affairs.

     Typical features of a King's Hall include:

**Grand entrance:** Large carved doors that create an impressive first impression.

**High vaulted ceiling:** Often supported by massive wooden beams or stone arches, emphasizing the hall's grandeur.

**Royal throne:** Positioned on a raised platform or dais at one end of the hall as the central focal point.

**Long banquet tables:** Used for royal feasts, state dinners, and celebrations.

**Massive chandeliers:** Crystal or wrought-iron chandeliers illuminate the expansive interior.

**Stone or marble flooring:** Durable and luxurious, often decorated with intricate patterns.

**Decorative walls:** Adorned with tapestries, murals, paintings, coats of arms, banners, and shields depicting the kingdom's history.

**Columns and arches:** Ornate stone columns and arches add architectural elegance and support.

**Large fireplace:** A monumental fireplace provides warmth and serves as another focal feature.

**Royal symbols:** Crowns, crests, flags, and heraldic emblems reinforce the authority and prestige of the monarchy.

**Tall stained-glass windows:** Fill the hall with colorful natural light while depicting historical or religious scenes.

**Gallery or balcony:** Sometimes included for musicians, guards, or spectators during ceremonies.


***Purpose of a King's Hall***

Holding royal court and public audiences.
Hosting coronations, banquets, and diplomatic receptions.
Receiving ambassadors and noble guests.
Celebrating festivals, victories, and important state events.
Conducting judicial proceedings and official announcements.

The overall atmosphere of a King's Hall is majestic, powerful, and ceremonial, designed to reflect the wealth, authority, and prestige of the king and the kingdom.
    
    """)
    st.markdown("---")
    st.space("small")
    m2 = (r"C:\Users\TANU\Downloads\the_king_s_hall.glb")
    three_viewer(m2, height=400, key="3D_2")
    st.caption("drag it to see in 3D mode")


elif cb == "The Armoury":
    st.header(" :green[The Armoury]")
    st.markdown("---")
    st.space("small")
    st.info("""
            The Armoury (also spelled Armory) is a secure room or building used for storing, maintaining, and displaying weapons, armor, and military equipment. In castles and royal palaces, the armoury played a vital role in preparing soldiers and protecting the kingdom.

            Key Features of an Armoury
            
Weapon Storage: Racks and stands holding swords, spears, axes, maces, bows, crossbows, shields, and other traditional weapons.

Armor Displays: Suits of plate armor, chainmail, helmets, gauntlets, greaves, and breastplates arranged on mannequins or storage racks.

Heavy Wooden Racks: Custom-built shelves and cabinets designed to organize weapons safely and allow quick access.

Forging and Repair Area: A workspace equipped with anvils, hammers, grinding wheels, and blacksmith tools for repairing and maintaining weapons and armor.

Secure Construction: Thick stone walls, reinforced wooden doors, and heavy iron locks to protect valuable military equipment.

Training Equipment: Practice swords, wooden dummies, archery targets, and other tools used for military training.

Lighting: Torches, lanterns, and wall-mounted sconces provide illumination while enhancing the medieval atmosphere.

Decorative Displays: Banners, coats of arms, shields, and ceremonial weapons displayed to reflect the kingdom's military heritage.

Storage Chests: Large wooden chests and barrels used to store arrows, bolts, spare equipment, and supplies.

Stone Flooring: Durable floors designed to withstand the weight of metal armor and weaponry.


***Purpose of an Armoury***

Safely storing weapons and armor.
Equipping soldiers before battles.
Repairing and maintaining military equipment.
Protecting valuable arms from theft or damage.
Training warriors in the use of various weapons.
Preserving ceremonial and historical weapons.


***Overall Atmosphere***

An armoury conveys a sense of strength, discipline, and preparedness. The combination of gleaming steel weapons, polished armor, sturdy stone architecture, and organized storage creates an environment that reflects the military power, craftsmanship, and defensive readiness of a castle or kingdom.
    """)
    st.markdown("---")
    st.space("small")
    m4 = (r"C:\Users\TANU\Downloads\the_armoury.glb")
    three_viewer(m4, height=400, key="3D_4")
    st.caption("drag it to see in 3D mode")


elif cb == "Morning room":
    st.header(" :green[The great Morning Room]")
    st.markdown("---")
    st.space("small")
    st.info("""
            The Morning Hall is a bright and welcoming gathering space in a palace, mansion, or grand residence, traditionally used during the early hours of the day for meetings, relaxation, and receiving visitors. It is designed to maximize natural light and create a calm, refreshing atmosphere.

            Key Features of a Morning Hall
            
            
Large Windows: Tall windows or glass panels allow abundant natural sunlight to illuminate the room.

Elegant Seating: Comfortable sofas, armchairs, benches, and small tables arranged for informal conversations and relaxation.

High Ceilings: Spacious interiors with decorative moldings, arches, or exposed wooden beams that enhance openness.

Natural Décor: Fresh flowers, indoor plants, and decorative vases add warmth and freshness to the space.

Fine Flooring: Polished marble, hardwood, or patterned stone floors, often complemented by elegant rugs or carpets.

Soft Color Palette: Light shades such as cream, ivory, beige, or pastel tones create a bright and peaceful ambiance.

Decorative Elements: Paintings, mirrors, sculptures, chandeliers, and ornamental columns enhance the hall's elegance.

Breakfast or Tea Area: A small dining arrangement where morning tea, coffee, or breakfast may be served.

Open Layout: Designed to encourage movement and provide a pleasant setting for informal gatherings.

Connection to Gardens: Often overlooks or opens directly onto gardens, courtyards, or terraces, blending indoor comfort with outdoor beauty.


***Purpose of a Morning Hall***

Welcoming family members and guests at the start of the day.
Hosting informal meetings and conversations.
Enjoying morning tea, coffee, or breakfast.
Reading, relaxing, or planning daily activities.
Providing a peaceful space filled with natural light.


***Overall Atmosphere***

A Morning Hall is characterized by brightness, elegance, and tranquility. With abundant sunlight, tasteful furnishings, and a connection to nature, it creates a refreshing environment that promotes relaxation, social interaction, and a pleasant beginning to the day.
    """)
    st.markdown("---")
    st.space("small")
    m5 = (r"C:\Users\TANU\Downloads\the_morning_room.glb")
    three_viewer(m5, height=400, key="3D_5")
    st.caption("drag it to see in 3D mode")


elif cb == "Smoking room":
    st.header(" :green[The great Smoking Room]")
    st.markdown("---")
    st.space("small")
    st.info("""
            The Smoking Hall is a private lounge traditionally found in royal palaces, grand mansions, and gentlemen's clubs, where guests gathered to enjoy cigars, pipes, or tobacco while engaging in conversation, relaxation, and social activities. It is typically designed with rich furnishings and a refined atmosphere that reflects sophistication and comfort.

            Key Features of a Smoking Hall
            
            
Comfortable Seating: Luxurious leather armchairs, sofas, and lounge chairs arranged to encourage conversation and relaxation.

Wood-Paneled Interiors: Rich wooden walls, carved panels, and elegant moldings create a warm and distinguished ambiance.

Fireplace: A grand fireplace often serves as the focal point, providing warmth and enhancing the room's cozy atmosphere.

Cigar and Pipe Storage: Cabinets, humidors, and display cases designed to preserve cigars, pipes, and smoking accessories.

Ventilation System: Large windows, high ceilings, or specially designed ventilation to disperse smoke and maintain air quality.

Decorative Lighting: Chandeliers, wall sconces, table lamps, and soft ambient lighting create an intimate setting.

Fine Flooring: Hardwood, marble, or patterned carpets add elegance and comfort.

Library and Reading Area: Bookshelves stocked with literature, newspapers, and journals provide opportunities for quiet reading.

Refreshment Corner: A sideboard or bar offering beverages such as coffee, tea, or fine spirits to complement social gatherings.

Classic Décor: Oil paintings, antique clocks, ornate mirrors, sculptures, and hunting trophies enhance the hall's luxurious character.


***Purpose of a Smoking Hall***

Providing a private space for relaxation and social interaction.
Hosting informal discussions, business meetings, and after-dinner conversations.
Enjoying cigars or pipes in a comfortable, well-ventilated environment.
Offering a quiet retreat for reading, reflection, or entertainment.


***Overall Atmosphere***

A Smoking Hall is characterized by luxury, warmth, and sophistication. Its elegant furnishings, rich wooden interiors, soft lighting, and comfortable seating create an inviting environment where guests can unwind, converse, and enjoy moments of leisure in a refined setting.
    """)
    st.markdown("---")
    st.space("small")
    m6 = (r"C:\Users\TANU\Downloads\the_smoking_room.glb")
    three_viewer(m6, height=400, key="3D_6")
    st.caption("drag it to see in 3D mode")


else:
    st.header(" :green[The Japanese Temple]")
    st.markdown("---")
    st.space("small")
    st.info("""
             A Japanese Temple is a place of Buddhist worship, meditation, and cultural heritage. It is designed to create a sense of tranquility and harmony with nature, reflecting the principles of simplicity, balance, and spirituality.

Key Features of a Japanese Temple


Main Hall (Hondō): The central building where the principal Buddha statue or sacred object is enshrined and worshippers gather for prayer.

Temple Gate (Sanmon): A large, beautifully crafted wooden gate marking the entrance to the sacred grounds.

Pagoda: A multi-tiered tower, usually with three or five stories, symbolizing Buddhist teachings and often housing sacred relics.

Curved Roofs: Distinctive roofs with gently upturned eaves covered with ceramic tiles, providing both beauty and protection from weather.

Wooden Architecture: Constructed primarily from natural wood using traditional joinery techniques without nails.

Zen Garden: Landscaped gardens featuring rocks, gravel, moss, and carefully pruned trees to encourage meditation and contemplation.

Stone Lanterns (Tōrō): Decorative lanterns placed along pathways and in gardens, symbolizing enlightenment.

Incense Burner: Located near the entrance where visitors burn incense for purification and prayer.

Bell Tower (Shōrō): Houses a large bronze bell that is rung during ceremonies and special occasions.

Prayer Hall: A quiet space where visitors offer prayers, meditate, and make offerings.

Ponds and Bridges: Water features with koi fish and wooden bridges represent purity, peace, and the journey through life.

Torii Gate (sometimes nearby): Although primarily associated with Shinto shrines, a torii may be found near temple complexes where Buddhist and Shinto traditions coexist.


***Interior Features***

Buddha statues and bodhisattvas.
Tatami mat flooring in some buildings.
Wooden pillars and exposed beams.
Sliding paper doors (shōji).
Hanging scrolls with Buddhist calligraphy.
Candles, flowers, and incense offerings.


***Purpose of a Japanese Temple***

Worship and prayer.
Meditation and spiritual practice.
Religious ceremonies and festivals.
Preservation of Buddhist teachings.
Cultural and historical significance.
A peaceful retreat for reflection.


***Overall Atmosphere***

   A Japanese temple is characterized by serenity, simplicity, and harmony with nature. The combination of elegant wooden architecture, tranquil gardens, gentle water features, and carefully designed spaces creates an environment that promotes mindfulness, respect, and inner peace.
    """)
    st.markdown("---")
    st.space("small")
    m3 = (r"C:\Users\TANU\Downloads\japanese_temple.glb")
    three_viewer(m3, height=400, key="3D_3")
    st.caption("drag it to see in 3D mode")


st.sidebar.markdown("---")
st.sidebar.space("small")

st.sidebar.caption("developed by Tanu Verma")
st.sidebar.html(" <a href='https://github.com/Tanu-v'>More about Tanu Verma</a>")
st.sidebar.caption("@2026 | All Rights Reserved")