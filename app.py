import streamlit as st
import PyPDF2
import io
from screener import screen_resume

st.set_page_config(page_title="AI Resume Screener", page_icon="📄")

st.title("📄 AI Resume Screener")
st.write("Upload a resume and paste a job description to get an instant AI match analysis.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Resume")
    uploaded_file = st.file_uploader("Upload PDF resume", type=["pdf"])

    resume_text = ""

    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
        for page in pdf_reader.pages:
            resume_text += page.extract_text()
        st.success("Resume loaded successfully!")

with col2:
    st.subheader("Job Description")
    job_desc = st.text_area(
        "Paste the job description here",
        height=250,
        placeholder="Copy and paste the full job description..."
    )

if st.button("Analyze Resume", type="primary"):
    if not resume_text:
        st.error("Please upload a resume first.")
    elif not job_desc.strip():
        st.error("Please enter a job description.")
    else:
        with st.spinner("Analyzing with AI..."):
            result = screen_resume(resume_text, job_desc)

        st.divider()
        st.subheader("Analysis Results")

        score = result["score"]
        st.metric("Match Score", f"{score} / 100")
        st.progress(score / 100)

        col3, col4 = st.columns(2)

        with col3:
            st.subheader("Matched Skills")
            for skill in result["matched_skills"]:
                st.success(f"• {skill}")

        with col4:
            st.subheader("Missing Skills")
            for skill in result["missing_skills"]:
                st.error(f"• {skill}")

        st.subheader("AI Feedback")
        st.info(result["summary"])