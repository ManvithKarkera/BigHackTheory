import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Configure page
st.set_page_config(
    page_title="Newsletter",    
    page_icon="⚡",
    layout="centered",  # Centered layout for a narrower appearance
    initial_sidebar_state="collapsed"
)

# Load environment variables
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")

# Fetch functions
def fetch_tech_news():
    url = f"https://newsapi.org/v2/top-headlines?category=technology&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])

def fetch_internships():
    url = "https://remoteok.io/api"
    response = requests.get(url)
    return response.json()

def fetch_hiring_companies():
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1?app_id={ADZUNA_APP_ID}&app_key={ADZUNA_APP_KEY}"
    response = requests.get(url)
    return response.json().get("results", [])

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }

        .header-section {
            padding: 2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            margin-bottom: 2rem;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        .main-title {
            font-size: 3rem;
            font-weight: 700;
            color: #00ff00;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            font-size: 1.25rem;
            color: rgba(255, 255, 255, 0.8);
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }

        .content-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1.25rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        .content-card:hover {
            transform: translateY(-2px);
            background: rgba(255, 255, 255, 0.15);
            box-shadow: 0 8px 16px rgba(0, 255, 0, 0.5);
        }

        .section-title {
            font-size: 2rem;
            font-weight: 700;
            color: #00ff00;
            margin-bottom: 1rem;
            text-align: center;
            border-bottom: 2px solid rgba(0, 255, 0, 0.5);
            padding-bottom: 0.5rem;
        }

        .badge {
            display: inline-block;
            padding: 0.375rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
            margin-right: 0.75rem;
            background: rgba(0, 255, 0, 0.2);
            color: #00ff00;
        }

        .content-link {
            color: #00ff00;
            font-weight: 500;
            text-decoration: none;
            transition: all 0.2s ease;
        }

        .content-link:hover {
            color: #aaffaa;
            text-decoration: underline;
        }

        .footer {
            text-align: center;
            padding: 2rem 0;
            color: rgba(255, 255, 255, 0.8);
            margin-top: 3rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="header-section">
        <h1 class="main-title">TechPulse</h1>
        <p class="subtitle">Your premier destination for tech news, career opportunities, and industry insights.</p>
    </div>
""", unsafe_allow_html=True)

# Stats Section
st.markdown("""
    <div class="stat-container" style="display: flex; justify-content: space-around; margin-bottom: 2rem;">
        <div class="stat-card" style="text-align: center;">
            <div class="stat-number" style="font-size: 2rem; font-weight: 700; color: #00ff00;">500+</div>
            <div class="stat-label" style="color: rgba(255, 255, 255, 0.8);">Daily Updates</div>
        </div>
        <div class="stat-card" style="text-align: center;">
            <div class="stat-number" style="font-size: 2rem; font-weight: 700; color: #00ff00;">50K+</div>
            <div class="stat-label" style="color: rgba(255, 255, 255, 0.8);">Tech Jobs</div>
        </div>
        <div class="stat-card" style="text-align: center;">
            <div class="stat-number" style="font-size: 2rem; font-weight: 700; color: #00ff00;">100+</div>
            <div class="stat-label" style="color: rgba(255, 255, 255, 0.8);">Partner Companies</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Main Content Tabs
tabs = st.tabs(["📱 Tech News", "🎯 Internships", "🏢 Companies"])

# Tech News Tab
with tabs[0]:
    st.markdown('<h2 class="section-title">Latest in Tech</h2>', unsafe_allow_html=True)
    articles = fetch_tech_news()
    
    if not articles:
        st.error("We're temporarily unable to fetch the latest news. Please check back soon!")
    else:
        for article in articles[:5]:
            st.markdown(f"""
                <div class="content-card">
                    <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.75rem;">{article["title"]}</h3>
                    <p style="margin-bottom: 1rem;">{article["description"]}</p>
                    <div>
                        <span class="badge">Tech News</span>
                        <a href="{article["url"]}" target="_blank" class="content-link">Read Full Story</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Internships Tab
with tabs[1]:
    st.markdown('<h2 class="section-title">Featured Internships</h2>', unsafe_allow_html=True)
    internships = fetch_internships()
    
    if not internships:
        st.error("No internships available at the moment. Please check back later!")
    else:
        for job in internships[:5]:
            st.markdown(f"""
                <div class="content-card">
                    <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.75rem;">
                        {job.get("position", job.get("title", "Unknown Position"))}
                    </h3>
                    <p style="margin-bottom: 0.5rem;">
                        <strong>Company:</strong> {job.get("company", "Unknown")}
                    </p>
                    <p style="margin-bottom: 1rem;">
                        <strong>Location:</strong> {job.get("location", "Remote")}
                    </p>
                    <div>
                        <span class="badge">Internship</span>
                        <a href="{job.get("url", "#")}" target="_blank" class="content-link">Apply Now</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Companies Tab
with tabs[2]:
    st.markdown('<h2 class="section-title">Top Companies Hiring</h2>', unsafe_allow_html=True)
    jobs = fetch_hiring_companies()
    
    if not jobs:
        st.error("Company information is temporarily unavailable. Please try again later!")
    else:
        for job in jobs[:5]:
            st.markdown(f"""
                <div class="content-card">
                    <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.75rem;">
                        {job.get("title", "Unknown Position")}
                    </h3>
                    <p style="margin-bottom: 0.5rem;">
                        <strong>Company:</strong> {job.get("company", {}).get("display_name", "Unknown")}
                    </p>
                    <p style="margin-bottom: 1rem;">
                        <strong>Location:</strong> {job.get("location", {}).get("display_name", "Unknown")}
                    </p>
                    <div>
                        <span class="badge">Full-time</span>
                        <a href="{job.get("redirect_url", "#")}" target="_blank" class="content-link">View Position</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p style="font-size: 1rem; margin-bottom: 0.5rem;">Designed & Developed by Pranav Koradiya</p>
        <p style="font-size: 0.875rem;">Empowering tech professionals with curated opportunities</p>
    </div>
""", unsafe_allow_html=True)