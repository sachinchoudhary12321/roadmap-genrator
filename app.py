import streamlit as st
from roadmap_generator import generate_roadmap

st.set_page_config(
    page_title="AI Roadmap Generator",
    page_icon="🚀",
    layout="centered"
)

st.title("Roadmap Generator")
st.markdown("Generate a personalized learning roadmap using AI")

# Sidebar
st.sidebar.header("About")
st.sidebar.info(
    "This AI tool generates structured learning roadmaps "
    "based on your skill, level and career goal."
)

# User Inputs
skill = st.text_input("Enter Skill (e.g., Data Science, Python, Full Stack)")
level = st.selectbox("Select Level", ["Beginner", "Intermediate", "Advanced"])
goal = st.text_input("Your Goal (Job / Freelance / Startup / Interview)")

generate_button = st.button("Generate Roadmap")

if generate_button:
    if skill and goal:
        with st.spinner("Generating roadmap... Please wait..."):
            roadmap = generate_roadmap(skill, level, goal)

        st.success("Roadmap Generated Successfully!")

        st.markdown("## 📚 Your Personalized Roadmap")
        st.write(roadmap)

        # Download option
        st.download_button(
            label="📥 Download Roadmap",
            data=roadmap,
            file_name="AI_Roadmap.txt",
            mime="text/plain"
        )
    else:
        st.error("Please fill all fields!")
