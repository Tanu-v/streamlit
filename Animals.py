import streamlit as st

#Homework17 : date-04/07/26

st.title("🦚 :blue[Animals] ")
st.markdown("---")
st.sidebar.title("🦚 :blue[Animals] ")
st.sidebar.space("small")
st.sidebar.image(r"C:\Users\TANU\Downloads\zoo-animals-nature-background-group-together-text-area-range-elephant-zebra-bear-rhino-use-31663413.webp")
st.sidebar.space("small")
st.space("small")
st.image(r"C:\Users\TANU\Downloads\collage-wild-animals-birds-nature-33582272.webp")
st.space("small")
st.markdown("---")
st.success(" In this site you can learn about some land , water and both[ Land + Water ] types of animals . There are also some images of these animals . You can see and read about them and also give feedback according to your liking .")
st.markdown("---")

st.write(" Here we will read about these below animals:-")
st.badge("Animals",icon="🐧")
st.badge("Land animal",icon="🐒")
st.badge("Water animal",icon="🪼")
st.badge("Both animal",icon="🐢")
with st.echo():
    st.write(""" These are animals .
    You can read about animals here . """)

st.metric("My Animals",value=3, delta=3-4)

st.markdown("---")
st.space("small")

st.warning("Under Types choose or tab the buttons below to read information about the animals given .")
st.sidebar.success("""  ### Types """)
st.sidebar.subheader("🐶 :blue[ Land Animals] ")
st.sidebar.subheader("🐬 :blue[Water Animals] ")
st.sidebar.subheader("🏞 :blue[Both Animals] ")


ty = st.pills("Type",["Land","Water","Both"])
st.space("small")
st.markdown("---")
if ty == "Land":
    st.header("🐶 :blue[Land Animals]")
    st.markdown("---")
    t1,t2,t3 = st.tabs(["Reptiles","Mammals","Birds"])
    with t1:
        st.header(" :blue[Reptiles]")
        st.markdown("---")
        st.write("Reptiles are cold-blooded vertebrates covered in dry scales or scutes. They breathe air through lungs and typically lay soft-shelled eggs on land. This group includes snakes, lizards, turtles, crocodiles, and alligators. Being ectothermic, they rely on external environmental sources to regulate their body temperature.")
        st.image(r"C:\Users\TANU\Downloads\collection-reptiles-collection-different-reptiles-isolated-white-background-201721664.webp")
        st.feedback("thumbs")
    with t2:
        st.header(" :blue[Mammals]")
        st.markdown("---")
        st.write("Mammals are warm-blooded vertebrates characterized by the presence of hair or fur at some stage of their life. A defining feature is that females produce milk to nourish their young. Most mammals give birth to live offspring rather than laying eggs. This diverse class includes humans, whales, elephants, and bats, inhabiting environments ranging from arctic tundra to deep oceans.")
        st.image(r"C:\Users\TANU\Downloads\91d8b693be20d7467d319b87a87e963b.webp")
        st.feedback("stars")
    with t3:
        st.header(" :blue[Birds]")
        st.markdown("---")
        st.write("Birds (Class Aves) are warm-blooded vertebrates uniquely identified by their feathers, wings, and beaks.  While not all birds can fly, they all possess wings and lay hard-shelled eggs. Their skeletons are often hollow to facilitate flight, and they are bipedal, meaning they walk on two legs. Examples range from tiny hummingbirds to massive ostriches and penguins. ")
        st.image(r"C:\Users\TANU\Downloads\collection-birds-including-one-with-red-beak_1295705-13566.webp")
        st.feedback("faces")
    st.space("medium")

elif ty == "Water":
    st.header("🐬 :blue[Water Animals]")
    st.markdown("---")
    se = st.segmented_control("Options",["Aquatic Vertebrates","Aquatic Invertebrates"])
    if se == "Aquatic Vertebrates":
        st.header(":blue[Aquatic Vertebrates]")
        st.markdown("---")
        st.write(""" These animals possess a spinal column and include five major classes:

Fish: The most diverse group, breathing through gills and using fins for movement.  Examples include Sharks (cartilaginous), Tuna (bony), and Salmon.
Mammals: Warm-blooded air-breathers that nurse their young. Examples include Whales, Dolphins, and Seals. 
Reptiles: Cold-blooded, air-breathing animals with scales. Examples include Sea Turtles, Sea Snakes, and Crocodiles. 
Amphibians: Animals that often start life in water with gills and develop lungs for land, though some remain aquatic. Examples include Frogs (tadpole stage), Salamanders, and Newts. 
Birds: While many fly, several species are highly adapted for aquatic life, swimming and diving for food. Examples include Penguins, Ducks, and Albatrosses. """)

        st.image(r"C:\Users\TANU\Downloads\illustration-of-the-diversity-of-fish-and-the-marine-world.webp")
        st.feedback("thumbs")
    else :
        st.header(" :blue[Aquatic Invertebrates]")
        st.markdown("---")
        st.write(""" Lacking a backbone, this group makes up the vast majority of aquatic species:

Cnidarians: Soft-bodied animals with stinging cells, such as Jellyfish, Corals, and Sea Anemones.
Mollusks: Soft-bodied animals, often with shells, including Octopuses, Squid, Clams, and Snails. 
Crustaceans: Arthropods with hard exoskeletons, such as Crabs, Lobsters, and Shrimp. 
Echinoderms: Spiny-skinned marine animals like Starfish (Sea Stars) and Sea Urchins. """)

        st.image(r"C:\Users\TANU\Downloads\some-invertebrates-moluscs-arthropods-sea-600nw-2019365729.webp")


elif ty == "Both":
    st.header("🏞 :blue[Both Animals]")
    st.markdown("---")
    con = st.container(horizontal=True)
    if con.button("Amphibians (The 'Double Life' Group)"):
        st.header(" :blue[Amphibians]")
        st.markdown("---")
        st.write(""" The term amphibian comes from the Greek amphibios, meaning "double life." These cold-blooded vertebrates typically begin life in water breathing through gills and undergo metamorphosis to develop lungs for life on land.  However, they must return to water or moist environments to breed and keep their skin hydrated.

Frogs and Toads: The most common examples. They start as aquatic tadpoles and transform into terrestrial adults, though they remain near water. 
Salamanders and Newts: Lizard-like amphibians that often retain a reliance on water throughout their lives. Some, like the Axolotl, remain aquatic permanently, while others like the Red-spotted Newt have distinct terrestrial juvenile stages. 
Caecilians: Legless, worm-like amphibians that live in moist soil or freshwater. """)
        st.image(r"C:\Users\TANU\Downloads\List-Of-Amphibians.webp")
        st.feedback("thumbs")

    elif con.button("Semiaquatic Reptiles"):
        st.header(" :blue[Semiaquatic Reptiles]")
        st.markdown("---")
        st.write(""" Unlike amphibians, these animals do not undergo metamorphosis and have scaly skin to prevent water loss. They breathe air via lungs throughout their lives but are highly adapted for hunting and living in water. 

Crocodiles and Alligators: Massive predators that spend significant time submerged in rivers and lakes but bask and nest on land. 
Sea Turtles: While they spend most of their lives in the ocean, they are obligate land-users for reproduction, as females must come ashore to lay eggs on sandy beaches. 
Marine Iguanas: Unique to the Galápagos Islands, these are the only lizards that forage in the sea for algae but bask on land to regulate body temperature.
Water Snakes: Species like the Anaconda and Water Moccasin are excellent swimmers that hunt in water but rest on land or in trees.  """)
        st.image(r"C:\Users\TANU\Downloads\462a3e934217d4ebee9460144614c8cb.webp")
        st.feedback("stars")

    elif con.button("Semiaquatic Mammals"):
        st.header(" :blue[Semiaquatic Mammals]")
        st.markdown("---")
        st.write("""  These warm-blooded animals have evolved specific physical traits—such as webbed feet, waterproof fur, and streamlined bodies—to thrive in both elements. They generally breathe air and give birth to live young on land or in dens near water. 

Beavers: Known as ecosystem engineers, they build dams and lodges in water but venture onto land to fell trees for construction and food. 
Otters: Highly agile swimmers that hunt fish and crustaceans in water but come ashore to rest, groom, and raise pups in riverbank dens. 
Capybaras: The world's largest rodents, native to South America. They are excellent swimmers that graze on land but retreat to water to escape predators and cool down. 
Platypus: An egg-laying mammal from Australia that forages underwater using its sensitive bill but lives in burrows along riverbanks. 
Hippopotamus: Spends days submerged in rivers to stay cool and nights on land grazing on grass. """)
        st.image(r"C:\Users\TANU\Downloads\ChatGPT Image Jul 5, 2026, 01_45_51 PM.png")
        st.feedback("stars")

    elif con.button("Semiaquatic Birds"):
        st.header(" :blue[Semiaquatic Birds]")
        st.markdown("---")
        st.write("""  While birds are terrestrial, many species are adapted to spend a majority of their time in the water. 

Penguins: Flightless birds with flipper-like wings that are superb swimmers but nest and molt on land or ice.
Ducks and Geese: Waterfowl that feed in water but nest and rest on land.
Cormorants: Fish-eating birds that swim underwater to hunt but perch on rocks or trees to dry their feathers. """)
        st.image(r"C:\Users\TANU\Downloads\ChatGPT Image Jul 5, 2026, 01_50_35 PM.png")
        st.feedback("stars")


from streamlit_extras.bottom_container import *
with bottom():
    st.caption("This is made by - Tanu Verma" )
    st.caption("@2026 | All Rights Reserved")
    st.sidebar.caption("This is made by - Tanu Verma")
    st.sidebar.caption("@2026 | All Rights Reserved")

if st.button("Snow"):
    st.snow()

if st.button("Thankyou!"):
    st.balloons()
    st.success(""" ### Thankyou !
    #### You've reached the end .""")
