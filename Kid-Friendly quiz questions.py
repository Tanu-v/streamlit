import streamlit as st

# Homework:02 "Question and Answer" Date:05/06/26

st.title("Kid-Friendly quiz questions")
st.info("These are easy questions made for kids when they are growing and making easy progress with their studies and healthy developing their brains.")

#Easy question section
st.header("Easy Questions")
q1 = st.radio("1.  What color do you get when you mix blue and yellow?",["Yellow","Green","Blue","Olive"])
if q1 == "Green":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q2 =st.radio("2. How many legs does a spider have? ",["Five","Four","Six","Eight"])
if q2 == "Eight":
    st.success("You're Right")
else:
    st.error("You're Wrong")


q3 = st.radio("3. What do bees make?",["Honey","Bunny","Water"])
if q3 == "Honey":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q4 = st.radio("4.  What is the tallest land animal? ",["Giraffe","Tiger","Elephant"])
if q4 == "Giraffe":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q5 = st.radio("5. Which planet do we live on? ",["Mars","Earth","Moon"])
if q5 == "Earth":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q6 = st.radio("6.  What do caterpillars turn into?",["Bees","Bugs","Mosquito","Butterfly"])
if q6 == "Butterfly":
    st.success("You're Right")
else:
    st.error("You're Wrong")


q7 = st.radio("7. What do we call baby dogs?",["Puppy","Stuffy","Calfy"])
if q7 == "Puppy":
    st.success("You're Right")

else:
    st.error("You're Wrong")

q8 = st.radio("8. What Shape has three sides?",["rectangle", "Square","Triangle"])
if q8 == "Triangle":
    st.success("You're Right")
else:
    st.error("You're Wrong")


#Medium Question Section
st.header("Medium Questions")

q9 = st.radio("9. What do plants need from sunlight to make food?",["Photosynthesis","Ozonification","Glycolysis"])
if q9 == "Photosynthesis":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q10 = st.radio("10. What gas do we breathe in that our bodies need?",["CO2","O2","N","He"])
if q10 == "O2":
    st.success("You're Right")
else:
    st.error("You're Wrong")


q11 = st.radio("11.  Which planet is known as the Red Planet?",["Mars","Earth","Moon"])
if q11 == "Mars":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q12 = st.radio("12.  What is the largest ocean on earth?",["Atlantic","Pacific Ocean","Arctic Ocean"])
if q12 == "Pacific Ocean":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q13 = st.radio("13. What do you call a baby cat?",["Doggy","Meow","Kitten"])
if q13 == "Kitten":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q14 = st.radio("14. Which animal is famous for black-and-white stripes?",["Zebra", "Lion", "Cat"])
if q14 == "Zebra":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q15 = st.radio("15.  What is the opposite of hot?",["Soft","Sour","Cold"])
if q15 == "Cold":
    st.success("You're Right")

else:
    st.error("You're Wrong")

q16 = st.radio("16. How many minutes are in an hour? ",["20","30","60","40"])
if q16 == "60":
    st.success("You're Right")
else:
    st.error("You're Wrong")


#Hard Questions Section
st.header("Hard Questions")

q17 =st.radio("17. How many bones are in the human ear? ",["Three", "Four", "Five"])
if q17 == "Three":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q18 = st.radio("18. Which layer protects us from Harmful UV lights?",["Troposphere","Ozone","Mesosphere"])
if q18 == "Ozone":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q19 = st.radio("19. Which continent has the most people?",["Asia","Europe","North America"])
if q19 == "Asia":
    st.success("You're Right")
else:
    st.error("You're Wrong")

q20 = st.radio("20. What force keeps us on the ground?  ",["Newton", "Friction","Gravity"])
if q20 == "Gravity":
    st.success("You're Right")
else:
    st.error("You're Wrong")
