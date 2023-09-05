import streamlit as st
import random

# Define a list of sample questions and answers (you can replace these with your own data).
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

# Initialize variables to track the user's score and current question.
user_score = 0
current_question_index = 0

# Shuffle the questions for randomness.
random.shuffle(questions)

# Streamlit app header.
st.title('Quiz App')

# Function to display a question and collect user's answer.
def display_question():
    global current_question_index, user_score
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

# Main quiz interface.
if current_question_index < len(questions):
    display_question()
else:
    st.subheader('Quiz Finished!')
    st.write(f'Your Score: {user_score}')

# Add a button to restart the quiz.
if st.button('Restart Quiz'):
    current_question_index = 0
    user_score = 0
    random.shuffle(questions)
