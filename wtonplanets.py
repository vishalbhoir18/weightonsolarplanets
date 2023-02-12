import streamlit as st

def calculate_weight(weight, planet):
    if planet == "Mercury":
        return weight * 0.38
    elif planet == "Venus":
        return weight * 0.91
    elif planet == "Mars":
        return weight * 0.38
    elif planet == "Jupiter":
        return weight * 2.34
    elif planet == "Saturn":
        return weight * 1.06
    elif planet == "Uranus":
        return weight * 0.92
    elif planet == "Neptune":
        return weight * 1.19
    elif planet == "Moon":
        return weight * 0.17
    elif planet == "Pluto [dwarf planet]":
        return weight * 0.06
    else:
        return weight

st.title("Weight on Different Planets")

weight_on_earth = st.number_input("Enter your weight on Earth (in kg):", min_value=0.0)
planet = st.selectbox("Select a planet or moon:", ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Moon", "Pluto [dwarf planet]"])

result = calculate_weight(weight_on_earth, planet)

st.write("Your weight on", planet, "would be:", result, "kg")

if planet == "Mercury":
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercury_in_true_color.jpg", use_column_width=True)
elif planet == "Venus":
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/54/Venus_-_December_23_2016.png", use_column_width=True)
elif planet == "Mars":
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg", use_column_width=True)
elif planet == "Jupiter":
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2b/Jupiter_and_its_shrunken_Great_Red_Spot.jpg", use_column_width=True)
elif planet == "Saturn":
    st.image("https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg", use_column_width=True)
elif planet == "Uranus":
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg", use_column_width=True)
elif planet == "Neptune":
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/56/Neptune_Full.jpg", use_column_width=True)
elif planet == "Moon":
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg", use_column_width=True)
elif planet == "Pluto [dwarf planet]":
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/ef/Pluto_in_True_Color_-_High-Res.jpg", use_column_width=True)


st.write("Note: The weight has been calculated based on the gravitational pull on each planet/moon relative to Earth.")
st.write("_Reference: https://www.exploratorium.edu_")
