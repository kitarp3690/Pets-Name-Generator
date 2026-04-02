import langchain_helper as lch
import streamlit as st

st.title("🐾 Animal Name Suggester")
st.write("Enter an animal type and a color to get 5 unique name suggestions!")

animal = st.text_input("Animal (e.g. cat, dog, rabbit)", max_chars=40)
color = st.text_input("Color (e.g. golden, black, spotted)", max_chars=40)

if st.button("Get Name Suggestions"):
    if not animal or not color:
        st.error("Please provide both an animal name and a color.")
    else:
        with st.spinner("Generating name suggestions..."):
            suggestions = lch.get_name_suggestions(animal, color)
            st.success("Here are 5 name suggestions for your {} {}:".format(color, animal))
            st.text(suggestions)