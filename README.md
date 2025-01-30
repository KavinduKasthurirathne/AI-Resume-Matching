# AI Resume Matching, Analysis, and Chat

This is a web application built with Streamlit that allows users to upload resumes (PDF format), match them against a provided job description, analyze their content, and interact with them via a chat interface.

### Features:
1. **Resume Filter**: Matches uploaded resumes with a given job description based on text similarity.
2. **Resume Analysis**: Extracts key information such as skills, experience, and education from a resume and provides a summary.
3. **Resume Chat**: Allows users to chat with a resume, asking specific questions about its content.

### Technologies Used:
- **Streamlit**: For building the web app interface.
- **pdfplumber**: For extracting text from PDF files.
- **Sentence Transformers**: For comparing text similarity between resumes and job descriptions.
- **Google Gemini (Generative AI)**: For advanced analysis, summary, and extraction of information from resumes.

## Setup Instructions

### Prerequisites:
- Python 3.x
- Google Cloud Account (for Gemini API key)

### Installation:
1. Clone this repository:
   ```bash
   git clone https://github.com/KavinduKasthurirathne/AI-Resume-Matching.git
   cd ai-resume-matching

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the Streamlit app:
   ```bash
   streamlit run app.py

### How It Works
1. **Resume Filter:**
Upload multiple resumes (in PDF format).
Provide a job description in the input box.
The app will compare the resumes to the job description using a pre-trained Sentence Transformer model and return the top matching resumes based on cosine similarity.
2. **Resume Analysis:**
Upload a single resume (in PDF format).
The app will summarize the resume using Google Gemini and extract key information, including skills, years of experience, and education.
3. **Resume Chat:**
Upload a single resume (in PDF format).
You can interact with the resume by typing in questions about its content, and Google Gemini will respond with relevant information.
