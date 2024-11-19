import streamlit as st
import random

# Title and Description
st.title("Guessing Game")
st.write("Choose a mode and play a fun guessing game!")

# Mode selection
mode = st.radio("Choose a Mode:", ("User Mode", "Computer Mode"))

# User Mode 
if mode == "User Mode":
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
else:
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