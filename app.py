import streamlit as st
from profile_data import profile
import random
import base64

# Page config
st.set_page_config(page_title="Kapil's Resume Chatbot", page_icon="🤖", layout="centered")

# Theme toggle with icon
theme = st.sidebar.radio("🌗 Theme", ("🌞 Light", "🌙 Dark"))

# Theme styles
if "Light" in theme:
    bg_color = "#FFFDE7"
    text_color = "#FCF652"
    box_color = "#3D3D3D"
    btn_color = "#FFD54F"
else:
    bg_color = "#2C2C2C"
    text_color = "#F0F0F0"
    box_color = "#424242"
    btn_color = "#FF8A65"

# CSS styling
st.markdown(f"""
    <style>
        .main {{
            background-color: {bg_color};
            color: {text_color};
        }}
        .center {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }}
        .avatar {{
            border-radius: 50%;
            width: 140px;
            margin-bottom: 20px;
        }}
        .chat-bubble {{
            background-color: {box_color};
            color: {text_color};
            padding: 15px 20px;
            border-radius: 15px;
            margin: 10px auto;
            width: fit-content;
            max-width: 80%;
            box-shadow: 0 2px 10px rgba(0,0,0,0.15);
            animation: typing 0.6s steps(30, end);
        }}
        @keyframes typing {{
            from {{ width: 0 }}
            to {{ width: 100% }}
        }}
        .btn-download {{
            margin-top: 20px;
            padding: 12px 24px;
            border-radius: 10px;
            background-color: {btn_color};
            color: {text_color};
            text-align: center;
            font-weight: bold;
            border: none;
        }}
    </style>
""", unsafe_allow_html=True)

# Avatar and Intro
st.markdown('<div class="center">', unsafe_allow_html=True)

import requests

url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Flovepik.com%2Fimages%2Fpng-anime.html&psig=AOvVaw2uT0TOwDtd-FEE7B0dwPRF&ust=1749765636572000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMChsaKv6o0DFQAAAAAdAAAAABAE"  # Example URL
response = requests.get(url)

if response.status_code == 200:
    image_data = response.content
else:
    raise Exception("Could not fetch image from URL.")

st.markdown(f"<center><h1 style='color:{text_color}'>Hi,<br>🤖I am Kapil's Resume Chatbot🤖</h1></center>", unsafe_allow_html=True)
st.markdown(f"<center><p style='color:{text_color}'>Ask me anything about Kapil Patil!</p></center>", unsafe_allow_html=True)

# Query input
query = st.text_input("💭 What do you want to know?", "")

# PDF download
with open("Kapil_Patil_Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📄 Download Resume",
    data=PDFbyte,
    file_name="Kapil_Patil_Resume.pdf",
    mime='application/octet-stream',
    help="Click to download Kapil's resume.",
    key="download_btn"
)

st.markdown('</div>', unsafe_allow_html=True)  # End center div

# Logic
def answer_question(q):
    q = q.lower()
    if "name" in q:
        return f"My name is {profile['name']}. I’m a {profile['title']}."
    elif "about" in q:
        return profile["about"]
    elif "skill" in q:
        return ", ".join(profile["skills"])
    elif "project" in q:
        return "\n\n".join([f"*{k}*: {v}" for k, v in profile["projects"].items()])
    elif "education" in q:
        return profile["education"]
    elif "contact" in q or "email" in q:
        c = profile["contact"]
        return f"📧 {c['email']} | 🔗 [LinkedIn]({c['linkedin']}) | 🐱 [GitHub]({c['github']})"
    elif "hr" in q or "interview" in q:
        return "👔 I bring a creative, solution-driven approach, backed by real projects and a learning mindset."
    elif "joke" in q:
        return random.choice([
            "Why did the developer go broke? Because he used up all his cache! 💸",
            "Why do Python devs wear glasses? Because they can't C! 🐍"
        ])
    else:
        return "❌ I didn’t get that. Try asking about skills, education, or projects."

# Show response
if query:
    response = answer_question(query)
    st.markdown(f'<div class="chat-bubble">{response}</div>', unsafe_allow_html=True)
