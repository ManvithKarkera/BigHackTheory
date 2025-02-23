import streamlit as st
from db_config import ats_collection
import fitz  # PyMuPDF for PDF processing
from docx import Document
import re

def ats_score_page(navigate):
    st.title('ATS Score Checker')

    st.button('Home', on_click=lambda: navigate('home'))

    uploaded_file = st.file_uploader('Upload Your Resume (PDF/DOCX)', type=['pdf', 'docx'])
    job_description = st.text_area('Job Description')

    if uploaded_file and job_description:
        ats_score, feedback = calculate_ats_score(uploaded_file, job_description)
        st.write(f'Your ATS Score: {ats_score}%')
        st.write('Feedback:')
        for tip in feedback:
            st.write(f"- {tip}")

        if 'user_email' in st.session_state:
            ats_collection.insert_one({
                'email': st.session_state['user_email'],
                'ats_score': ats_score,
                'feedback': feedback
            })
            st.success('ATS Score saved successfully!')

def calculate_ats_score(uploaded_file, job_description):
    resume_text = ""
    
    if uploaded_file.type == "application/pdf":
        pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        for page in pdf_doc:
            resume_text += page.get_text()
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(uploaded_file)
        resume_text = "\n".join([para.text for para in doc.paragraphs])

    job_keywords = re.findall(r'\b\w+\b', job_description.lower())
    resume_keywords = re.findall(r'\b\w+\b', resume_text.lower())

    matching_keywords = set(job_keywords) & set(resume_keywords)
    score = (len(matching_keywords) / len(job_keywords)) * 40 if job_keywords else 0

    feedback = []
    if score < 40:
        feedback.append('Try to include more relevant keywords from the job description.')
    if len(resume_text) < 500:
        feedback.append('Expand on your experiences and skills to make your resume more comprehensive.')

    return score, feedback
