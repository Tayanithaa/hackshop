import streamlit as st


st.set_page_config(page_title="My Portfolio", page_icon=":wave:", layout="centered")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Contact"])


if page == "Home":
    st.title("Welcome to My Portfolio!")
    st.write("Hello! I'm Tayanithaa.N.S, a passionate Student .")

    st.write("Explore my projects and learn more about me!")


elif page == "About Me":
    st.header("About Me")
    st.write("""
    I'm a Cyber security engineering student .
    I would like to work on projects that involve Hacking and Networking.
    """)

    st.write("### Skills")
    st.write(" Fast learner ")
    st.write(" Easily adaptable")
    st.write(" Good Communicator")

# Contact Section
elif page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out through the following channels.")
    
    st.write("Email: [tayanithaans2196@gmail.com](tayanithaans2196@gmail.com)")
    st.write(" LinkedIn: [linkedin.com/in/tayanithaa](https://linkedin.com/in/tayanithaa)")