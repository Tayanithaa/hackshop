import streamlit as st
import random

st.set_page_config(page_title="Home", page_icon=":wave:", layout="centered")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Guessing game", "Portfolio"])
if page=="Home":
    st.write('''WELCOME TO MY PAGE
         ''')

if page == "Guessing game":
    st.sidebar.title("Guessing Game")
    page=st.sidebar.radio("Go To",["User Mode","Computer Mode"])
    # Title and Description
    st.title("Guessing Game")
    st.write("Choose a mode and play a fun guessing game!")

    

    # User Mode 
    if page == "User Mode":
        st.subheader("User Mode: Try to guess the computer's number!")
    
        if 'target' not in st.session_state:
            # Set a random target number between 1 and 100
            st.session_state.target = random.randint(1, 100)
            st.session_state.attempts = 0
    
        # User input
        guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)
    
        # Check the guess
        if st.button("Submit Guess"):
            st.session_state.attempts += 1
            if guess < st.session_state.target:
                st.write("Too low! Try again.")
            elif guess > st.session_state.target:
                st.write("Too high! Try again.")
            else:
                st.write(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
                # Reset the game
                st.session_state.target = random.randint(1, 100)
                st.session_state.attempts = 0

    # Computer Mode
    elif page=="Computer Mode":
        st.subheader("Computer Mode: Think of a number between 1 and 100, and the computer will try to guess it.")
    
        if 'low' not in st.session_state:
            # Initialize the guessing range
            st.session_state.low = 1
            st.session_state.high = 100
            st.session_state.computer_attempts = 0

        # Computer guesses the middle of the current range
        computer_guess = (st.session_state.low + st.session_state.high) // 2
        st.write(f"Computer's Guess: {computer_guess}")
    
        # User feedback buttons
        feedback = st.radio("Is the computer's guess correct?", ("Too low", "Too high", "Correct"))
    
        if st.button("Submit Feedback"):
            st.session_state.computer_attempts += 1
            if feedback == "Too low":
                st.session_state.low = computer_guess + 1
            elif feedback == "Too high":
                st.session_state.high = computer_guess - 1
            else:
                st.write(f"The computer guessed your number in {st.session_state.computer_attempts} attempts!")
                # Reset the game
                st.session_state.low = 1
                st.session_state.high = 100
                st.session_state.computer_attempts = 0

elif page == "Portfolio":

    st.title("Welcome to My Portfolio!")
    st.write("Hello! I'm Tayanithaa.N.S, a passionate Student.")

    st.write("Explore my projects and learn more about me!")


    st.header("About Me")
    st.write("""
    I'm a Cyber security engineering student.
    I would like to work on projects that involve Hacking and Networking.
    """)

    st.write("### Skills")
    st.write(" Fast learner ")
    st.write(" Easily adaptable")
    st.write(" Good Communicator")

   
