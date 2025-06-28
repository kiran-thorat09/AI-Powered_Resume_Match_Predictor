# AI-Powered Resume Match Predictor

An end-to-end deep learning project that predicts how well a candidate's resume matches a job description using Sentence-BERT embeddings. This tool provides clear match scores and recommendations, with an interactive Streamlit interface and Excel logging for shortlisted candidates.



## Features

- **Semantic Similarity Scoring:** Leverages Sentence-BERT (`all-MiniLM-L6-v2`) to compute cosine similarity between resume text and job description.
- **PDF Resume Parsing:** Extracts resume text and candidate details (name, email, phone) automatically using PyMuPDF and regular expressions.
- **Interactive Web App:** Built with Streamlit for an easy-to-use interface to upload resumes, input job descriptions, and view results instantly.
- **Excel Logging:** Automatically saves information of candidates with partial or strong matches into an Excel file (`shortlisted_candidates.xlsx`).

---
## Architecture
![image](https://github.com/user-attachments/assets/35bf08c3-4333-4eb4-a9a1-0f75636a8ec1)



---

## Working
1) Upload Resume: Upload a PDF resume.

2) Paste Job Description: Enter the job description text.

3) Compute Match Score: The app calculates a similarity score between 0–1.0.

4) View Recommendations: Displays if the match is Strong, Partial, or Weak.

5) Log Shortlisted Candidates: If the score >0.5, candidate details are saved into an Excel file.


### Shortlisted_Candidates.xlsx

![image](https://github.com/user-attachments/assets/1abd97f3-2090-42ea-8461-3e1a77f608d0)

