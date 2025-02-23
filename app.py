import streamlit as st

st.set_page_config(
    page_title="Auth Portal",
    page_icon="C:/Users/nialr/Downloads/internshipicon.jpg",
    layout="centered",
    initial_sidebar_state="collapsed"
)

from login_page import login_page
from home_page import home_page
from ats_score_page import ats_score_page
from certificates_page import certificates_page
from hi import chat_ui  
import time  

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

def navigate(page_name):
    st.session_state['page'] = page_name
    st.rerun()

if not st.session_state['authenticated']:
    login_page(navigate)
else:
    st.title("Dashboard")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("🏠 Home"):
            navigate('home')
    with col2:
        if st.button("📊 ATS Score"):
            navigate('ats_score')
    with col3:
        if st.button("📜 Certificates"):
            navigate('certificates')
    with col4:
        if st.button("🤖 AI Chatbot"):
            navigate('chatbot')
    with col5:
        if st.button("🚪 Logout"):
            st.session_state['authenticated'] = False
            navigate('login')

    if st.session_state['page'] == 'home':
        home_page(navigate)
    elif st.session_state['page'] == 'ats_score':
        ats_score_page(navigate)
    elif st.session_state['page'] == 'certificates':
        certificates_page(navigate)
    elif st.session_state['page'] == 'chatbot':
        chat_ui(navigate)
