import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def clear_chat():
    st.session_state.messages = []

def chat_ui(navigate=None):  
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "submit" not in st.session_state:
        st.session_state.submit = False
    
    st.markdown("""
    <style>
        body { background-color: #121212; color: #ffffff; font-family: 'Arial', sans-serif; }
        .header-section {
            padding: 2rem; background: rgba(0, 0, 0, 0.6);
            border-radius: 12px; margin-bottom: 2rem; text-align: center;
            border: 1px solid rgba(0, 255, 0, 0.3); box-shadow: 0 0 20px rgba(0, 255, 0, 0.2);
            max-width: 800px; margin-left: auto; margin-right: auto;
        }
        .main-title { font-size: 2.5rem; font-weight: 600; color: #00ff00; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="header-section">
        <h1 class="main-title">AI Chatbot</h1>
        <p>Your intelligent chat companion</p>
    </div>
    """, unsafe_allow_html=True)

    if navigate:
        with st.container():
            if st.button("🏠 Home", key="home_button"):
                navigate("home")  

    chat_container = st.container()
    with chat_container:
        for role, text in st.session_state.messages:
            if role == "user":
                st.markdown(f'<div style="background: rgba(0,100,0,0.3); padding: 10px; border-radius: 10px; margin: 5px;">{text}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="background: rgba(0,50,0,0.3); padding: 10px; border-radius: 10px; margin: 5px;">{text}</div>', unsafe_allow_html=True)

    with st.container():
        col1, col2, col3 = st.columns([6, 1, 1])

        def process_input():
            if st.session_state.user_input.strip():
                st.session_state.messages.append(("user", st.session_state.user_input))
                ai_response = get_gemini_response(st.session_state.user_input)
                st.session_state.messages.append(("bot", ai_response))
                st.session_state.user_input = ""
        
        with col1:
            st.text_input("", placeholder="Type your message...", key="user_input", 
                         on_change=process_input, label_visibility="collapsed")
        with col2:
            st.button("Send", on_click=process_input, key="send_button")
        with col3:
            st.button("Clear", on_click=clear_chat, key="clear_button")

if __name__ == "__main__":
    chat_ui()
