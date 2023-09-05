
import streamlit as st
import random
import pandas as pd
import time

# Sample questions and answers (you can replace these with your own data).
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin'],
        'correct_answer': 'Paris',
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Earth', 'Mars', 'Venus'],
        'correct_answer': 'Mars',
    },
    # Add more questions here...
]

# Initialize user data for registration.
user_data = []

# Initialize variables for the quiz.
user_score = 0
current_question_index = 0
quiz_in_progress = False
start_time = None

# Load leaderboard data from a CSV file (or database) if available.
leaderboard_data = pd.DataFrame(columns=['User', 'Score'])

# Streamlit app header.
st.title('Quiz App')

# Function to display the registration form.
def registration():
    st.subheader('User Registration')
    username = st.text_input('Enter your name:')
    if st.button('Register'):
        user_data.append({'name': username, 'score': 0})
        st.success(f'Welcome, {username}! You are now registered.')

# Function to display a question and collect user's answer.
def display_question():
    global current_question_index, user_score, quiz_in_progress, start_time
    if current_question_index < len(questions):
        question_data = questions[current_question_index]
        st.subheader(f'Question {current_question_index + 1}: {question_data["question"]}')
        selected_option = st.radio('Select an option:', question_data['options'])
        
        if st.button('Submit Answer'):
            if selected_option == question_data['correct_answer']:
                user_score += 10
            else:
                user_score += 1
            current_question_index += 1
            start_time = time.time()  # Start the timer for the next question.
    else:
        quiz_in_progress = False
        st.subheader('Quiz Finished!')
        st.write(f'Your Score: {user_score}')

# Function to update the leaderboard.
def update_leaderboard():
    global leaderboard_data
    leaderboard_data = leaderboard_data.append({'User': user_data[-1]['name'], 'Score': user_score}, ignore_index=True)
    leaderboard_data = leaderboard_data.sort_values(by='Score', ascending=False)
    leaderboard_data.to_csv('leaderboard.csv', index=False)
    st.subheader('Leaderboard')
    st.dataframe(leaderboard_data)

# Main quiz interface.
if not user_data:
    registration()
elif not quiz_in_progress:
    if st.button('Start Quiz'):
        current_question_index = 0
        user_score = 0
        random.shuffle(questions)
        quiz_in_progress = True
        start_time = time.time()  # Start the timer for the first question.
else:
    display_question()
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, 10 - elapsed_time)
    st.write(f'Time Remaining: {remaining_time} seconds')
    if elapsed_time >= 10:
        current_question_index += 1
        start_time = time.time()  # Reset the timer for the next question.

# Display the user's score and the leaderboard.
if not user_data:
    pass
elif quiz_in_progress:
    pass
else:
    st.write(f'Your Final Score: {user_score}')
    update_leaderboard()
