import streamlit as st

def home_page(navigate):
    st.title('Home Page')
    
    st.button('Check Your ATS Score', on_click=lambda: navigate('ats_score'))
    st.button('Certificates', on_click=lambda: navigate('certificates'))
    st.button('AI Chatbot', on_click=lambda: navigate('chatbot')) 
    st.button('Logout', on_click=lambda: navigate('login'))

