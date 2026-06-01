# AI Resume Screener

A Python-based web application that uses AI to analyze a resume against a job description and returns a match score, matched skills, missing skills, and feedback.

Built with Streamlit and powered by Groq's LLaMA model.

---

## What it does

- Upload a resume in PDF format
- Paste any job description
- Get an instant AI analysis including:
  - Match score out of 100
  - Skills that match the job description
  - Skills that are missing
  - A short summary with feedback

---

## Project Structure

```
resume_screener/
│
├── app.py          # Streamlit UI — what the user sees
├── screener.py     # AI logic — calls the Groq API
└── .env            # Stores your API key (never share this)
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web UI framework |
| Groq API | AI inference (LLaMA 3.3 70b model) |
| PyPDF2 | Extracts text from PDF resumes |
| python-dotenv | Loads API key from .env file |

---

## Setup Instructions

### 1. Clone or download the project

```bash
git clone <your-repo-link>
cd resume_screener
```

### 2. Install dependencies

```bash
pip install streamlit groq PyPDF2 python-dotenv
```

### 3. Get your Groq API key

- Go to [console.groq.com](https://console.groq.com)
- Sign up with your Google account
- Click API Keys on the left sidebar
- Click Create API Key
- Copy the key (starts with `gsk_...`)

### 4. Create your .env file

Create a file called `.env` in the project folder and add:

```
GROQ_API_KEY=gsk_...your key here...
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## How it works

1. The user uploads a PDF resume — PyPDF2 extracts the text from it
2. The user pastes a job description into the text box
3. On clicking Analyze, the app builds a prompt combining both inputs
4. The prompt is sent to the Groq API (LLaMA 3.3 70b model)
5. The AI returns a structured JSON response with score, skills, and feedback
6. Streamlit displays the results on screen

---

## Model Used

**LLaMA 3.3 70b Versatile** hosted on Groq

- 70 billion parameter model by Meta
- Hosted on Groq's infrastructure for fast inference
- Free to use on Groq's free tier
- More than sufficient for resume analysis tasks

---

## Important Notes

- Never commit your `.env` file to GitHub. Add it to `.gitignore`
- The app only accepts PDF resumes at this time
- Results depend on the quality and detail of the job description provided

---

## Sample Output

```
Match Score     : 78 / 100

Matched Skills  : Python, TensorFlow, PyTorch, Docker, AWS, FastAPI, REST APIs

Missing Skills  : SIEM tools, Penetration Testing, NIST framework, OWASP

Summary         : Strong engineering background with solid Python and cloud
                  experience. Missing domain-specific security knowledge and
                  certifications required for this role.
```

---

## Future Improvements

- Support for DOCX resume format
- Export results as a PDF report
- Batch screening for multiple resumes at once
- Deploy to Streamlit Cloud for online access

---

## Author

Built as part of AI placement project for Hexaware Technologies selection process.