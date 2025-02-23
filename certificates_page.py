import streamlit as st
from db_config import certificates_collection
import fitz 

def certificates_page(navigate):
    st.title('Certificates Page')

    st.sidebar.title("Navigation")
    if st.sidebar.button("Home"):
        navigate('home')
    if st.sidebar.button("ATS Score"):
        navigate('ats_score')
    if st.sidebar.button("Certificates"):
        navigate('certificates')

    st.header('Upload Your Certificate')

    uploaded_file = st.file_uploader('Upload Certificate (PDF only)', type=['pdf'])

    if uploaded_file is not None:
        try:
            pdf_data = uploaded_file.read()
            certificates_collection.insert_one({
                'email': st.session_state.get('user_email'),
                'certificate': pdf_data
            })
            st.success('Certificate uploaded successfully!')
        except Exception as e:
            st.error(f'Error uploading certificate: {e}')

    st.header('Your Uploaded Certificates')
    user_email = st.session_state.get('user_email')
    
    if user_email:
        certificates = list(certificates_collection.find({'email': user_email}))
        
        if certificates:
            for cert in certificates:
                st.subheader(f'Certificate ID: {cert["_id"]}')
                
                try:
                    with fitz.open(stream=cert['certificate'], filetype='pdf') as doc:
                        page = doc.load_page(0)
                        image = page.get_pixmap()
                        st.image(image.tobytes(), caption="First Page Preview", use_column_width=True)
                except Exception as e:
                    st.error(f'Error displaying certificate preview: {e}')
                
                if cert['certificate']:
                    st.download_button(
                        'Download Certificate',
                        data=cert['certificate'],
                        file_name=f'certificate_{cert["_id"]}.pdf',
                        mime='application/pdf'
                    )
                else:
                    st.warning('No certificate data found.')
        else:
            st.info('No certificates uploaded yet.')
    else:
        st.warning('Please log in to view your certificates.')
