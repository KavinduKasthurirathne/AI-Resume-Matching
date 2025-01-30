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
   git clone https://github.com/your-username/ai-resume-matching.git
   cd ai-resume-matching
