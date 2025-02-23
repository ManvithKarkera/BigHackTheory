import streamlit as st
from db_config import users_collection

def login_page(navigate):
    st.title('Login Page')
    
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    
    if st.button('Login'):
        if email and password:
            user = users_collection.find_one({'email': email, 'password': password})
            if user:
                st.success('Login successful!')
                st.session_state['authenticated'] = True
                st.session_state['user_email'] = email
                navigate('home')
            else:
                st.error('Invalid email or password.')
        else:
            st.warning('Please enter both email and password.')
