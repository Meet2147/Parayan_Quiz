import streamlit as st

# Define quiz questions and answers
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'correct_option': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
        'correct_option': 'Mars'
    },
    # Add more questions here
]

# Initialize variables
users = []
current_question = 0

# Streamlit app
st.title('Quiz App')

# User registration
user_name = st.text_input('Enter your name:')
if user_name:
    users.append({'name': user_name, 'score': 0})
    st.success(f'Welcome, {user_name}!')

if len(users) > 0:
    if current_question < 10:  # Allow a total of 10 questions
        st.write(f'Question {current_question + 1}: {questions[current_question]["question"]}')
        options = questions[current_question]['options']
        selected_option = st.radio('Choose an option:', options)

        if selected_option == questions[current_question]['correct_option']:
            st.write('Correct!')
            # Update the user's score
            users[-1]['score'] += 1
        else:
            st.write(f'Incorrect! The correct answer is {questions[current_question]["correct_option"]}')

        current_question += 1
    else:
        st.write('Quiz completed!')
        st.write(f'Your score: {users[-1]["score"]}/{len(questions)}')

# Display user scores
if users:
    st.write('\n**User Scores:**')
    for user in users:
        st.write(f'{user["name"]}: {user["score"]}')

st.write('Thank you for playing!')
