# AI-Powered Resume Match Predictor

# Install required libraries
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import streamlit as st
import fitz  # PyMuPDF
import re
import os
from openpyxl import load_workbook

# Load model (Sentence-BERT)
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_similarity(resume_text, job_text):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_text, convert_to_tensor=True)
    score = util.cos_sim(resume_embedding, job_embedding).item()
    return round(score, 3)

# Extract data from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_name(text):
    lines = text.strip().split('\n')
    for line in lines[:5]:
        match = re.match(r'^[A-Z][a-z]+\s[A-Z][a-z]+$', line.strip())
        if match:
            return match.group()
    return "Unknown"

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group() if match else "Not found"

def extract_phone(text):
    match = re.search(r'(\+\d{1,3}[-\s]?)?\d{10}', text)
    return match.group() if match else "Not found"

# Streamlit UI
st.title(" Resume–Job Match Predictor")
st.write("Upload your resume PDF and paste a job description to check compatibility.")

uploaded_pdf = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_input = st.text_area("Paste Job Description:", height=200)

if st.button(" Check Match Score"):
    if uploaded_pdf and job_input:
        resume_text = extract_text_from_pdf(uploaded_pdf)
        score = get_similarity(resume_text, job_input)
        st.success(f" Match Score: {score} (out of 1.0)")

        if score > 0.7:
            st.markdown("### Great Match!")
        elif score > 0.5:
            st.markdown("### Partial Match. May need resume tuning.")
        else:
            st.markdown("### Weak Match. Consider updating your resume.")

        # Save to Excel if match is above Partial Match
        if score > 0.5:
            name = extract_name(resume_text)
            email = extract_email(resume_text)
            phone = extract_phone(resume_text)
            data = pd.DataFrame([[name, email, phone, score]], columns=["Candidate Name", "Email", "Phone", "Match Score"])
            file_path = "shortlisted_candidates.xlsx"

            if os.path.exists(file_path):
                with pd.ExcelWriter(file_path, engine="openpyxl", mode='a', if_sheet_exists='overlay') as writer:
                    data.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
            else:
                data.to_excel(file_path, index=False)

            st.success(f"Info saved: {name} | {email} | {phone} → Shortlisted_candidates.xlsx")
    else:
        st.error("Please upload a PDF resume and provide job description text.")



