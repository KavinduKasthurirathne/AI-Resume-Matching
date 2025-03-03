import streamlit as st
import pdfplumber
from sentence_transformers import SentenceTransformer, util
import pdfplumber
import os
import google.generativeai as gemini_ai
from google.oauth2 import service_account


# Load Google Gemini API Key
gemini_ai.configure(api_key="AIzaSyBkJZiw5pEUPP9Wg5HTadicGVVoMeIBydg")

# Function to get a response from Google Gemini
def get_gemini_repsonse(input):
    model = gemini_ai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(input)
    return response.text

# Load pre-trained model from Hugging Face
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Title and sidebar
st.title("AI Resume Matching, Analysis and Chat")
menu = ["Resume Filter", "Resume Analysis", "Resume Chat"]
choice = st.sidebar.selectbox("Select Activity", menu)

if choice == "Resume Filter":

    st.subheader("Upload Resumes and Provide Job Description")

     # Job description input
    job_description = st.text_area("Enter Job Description")
    
    # File uploader for multiple resumes
    resumes = st.file_uploader("Upload Resumes (PDF only)", accept_multiple_files=True, type=['pdf'])

    # Function to extract text from PDF resumes
    def extract_text_from_pdf(pdf_file):
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text
        

    submit1 = st.button("Filter Resumes")
    # Extract text from uploaded resumes
    if submit1:
        resume_texts = []
        if resumes:
            for resume in resumes:
                text = extract_text_from_pdf(resume)
                resume_texts.append(text)
                st.write(f"Uploaded {resume.name}")
       
    
        # Matching resumes with job description
        if job_description and resume_texts:
            job_embedding = model.encode(job_description, convert_to_tensor=True)

            resume_scores = []
            for i, resume_text in enumerate(resume_texts):
                resume_embedding = model.encode(resume_text, convert_to_tensor=True)
                similarity_score = util.pytorch_cos_sim(job_embedding, resume_embedding)[0][0].item()
                resume_scores.append((resumes[i].name, similarity_score))

            # Sort and display top 5 matching resumes
            resume_scores = sorted(resume_scores, key=lambda x: x[1], reverse=True)
            st.subheader("Top Matching Resumes")
            for resume_name, score in resume_scores[:5]:
                st.write(f"Resume: {resume_name} | Match Score: {score * 100:.2f}%")
        else:
            st.write("Missing job description or resume")


if choice == "Resume Analysis":
    st.subheader("Upload Resume for Analysis")

    # File uploader for a single resume
    resume = st.file_uploader("Upload Resume (PDF only)", type=['pdf'])

    # Function to extract text from PDF resumes
    def extract_text_from_pdf(pdf_file):
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text


    # Summarize Resume using Google Gemini
    def summarize_resume(resume_text):
        
            prompt = (
            "Hey, you act like a highly skilled and experienced ATS (Applicant Tracking System) "
            "with deep knowledge in tech fields such as software engineering, Test Automation, "
            "Software Testing, and Automation framework development. Please provide a concise summary "
            "in one single sentence for the following resume:\n"
            f"{resume_text}"
            )
            response = get_gemini_repsonse(prompt)       
            return response

    # Extract key information using Google Gemini
    def extract_resume_info(resume_text):
        prompt = (
            "Extract the following information from this resume:\n"
            "1. Key Skills\n"
            "2. Years of Experience\n"
            "3. Education\n"
            f"Resume: {resume_text}"
        )
        response = get_gemini_repsonse(prompt)
        return response

    # Chat with the resume
    def chat_with_resume(user_question, resume_text):
        prompt = (
            f"Here is a resume:\n{resume_text}\n"
            f"Answer the following question about the resume: {user_question}"
        )
        response = get_gemini_repsonse(prompt)
        return response

    submit1 = st.button("Analyze Resume")
    # Extract text from uploaded resumes
    if submit1:
        # Process the uploaded resume
        if resume:
            st.write(f"Uploaded {resume.name}")
            resume_text = extract_text_from_pdf(resume)
            st.write("Resume Text Extracted")

            # Resume Summary
            resume_summary = summarize_resume(resume_text)
            st.subheader("Resume Summary")
            st.write(resume_summary)

            # Key Information Extraction
            resume_info = extract_resume_info(resume_text)
            st.subheader("Key Information")
            st.write(resume_info)
        else:
            st.write("No resume uploaded")
                       
if choice == "Resume Chat":
    st.subheader("Upload Resume for Chat")

    # File uploader for a single resume
    resume = st.file_uploader("Upload Resume (PDF only)", type=['pdf'])

    # Function to extract text from PDF resumes
    def extract_text_from_pdf(pdf_file):
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text


    # Summarize Resume using Google Gemini
    def summarize_resume(resume_text):
        
        prompt = (
            "Hey, you act like a highly skilled and experienced ATS (Applicant Tracking System) "
            "with deep knowledge in tech fields such as software engineering, Test Automation, "
            "Software Testing, and Automation framework development. Please provide a concise summary "
            "in one single sentence for the following resume:\n"
            f"{resume_text}"
            )
        response = get_gemini_repsonse(prompt)       
        return response

    # Extract key information using Google Gemini
    def extract_resume_info(resume_text):
        prompt = (
            "Extract the following information from this resume:\n"
            "1. Key Skills\n"
            "2. Years of Experience\n"
            "3. Education\n"
            f"Resume: {resume_text}"
        )
        response = get_gemini_repsonse(prompt)
        return response

    # Chat with the resume
    def chat_with_resume(user_question, resume_text):
        prompt = (
            f"Here is a resume:\n{resume_text}\n"
            f"Answer the following question about the resume: {user_question}"
        )
        response = get_gemini_repsonse(prompt)
        return response

    # Chat with the resume
    user_question = st.text_input("Ask something about the resume")
    submit1 = st.button("Send Message")
    if submit1:
        if resume:
            st.write(f"Uploaded {resume.name}")
            resume_text = extract_text_from_pdf(resume)
            chat_response = chat_with_resume(user_question, resume_text)
            st.subheader("Chat Reply")
            st.write(chat_response)
        else:
            st.write("No resume uploaded")