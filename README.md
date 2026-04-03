# 🤖 AI Job Hunt Assistant

A multi-agent AI system built with **CrewAI** and **Google Gemini** that automates the job hunting process for US job positions.

## Features

- 🔍 **USAJobs Search** — Fetches live job listings from the USAJobs API  
- 📋 **JD Analysis Agent** — Breaks down job descriptions into key skills, qualifications, and responsibilities  
- 📝 **Resume & Cover Letter Agent** — Tailors your resume summary and generates a personalized cover letter  
- 💬 **Outreach Agent** — Drafts professional LinkedIn/email messages for cold outreach  
- 📊 **Application Tracking** — Logs applications to CSV for easy tracking  

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| AI Framework | CrewAI |
| LLM | Google Gemini (2.0/2.5 Flash) |
| Job Data | USAJobs API |
| Language | Python 3.10+ |

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Raam751/Multi_Agent_Job_Search_System.git
   cd Multi_Agent_Job_Search_System
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   Create a `.env` file in the project root:
   ```env
   USAJOBS_API_KEY=your_usajobs_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. **Run the app**
   ```bash
   streamlit run streamlit_app.py
   ```

## Deployment (Streamlit Cloud)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set your API keys in **Settings → Secrets**:
   ```toml
   USAJOBS_API_KEY = "your_key"
   GEMINI_API_KEY = "your_key"
   ```

## Project Structure

```
├── streamlit_app.py        # Streamlit UI
├── orchestrator.py         # CrewAI pipeline orchestrator
├── usajobs_api.py          # USAJobs API integration
├── agents/
│   ├── jd_analyst.py       # Job description analysis agent
│   ├── resume_cl_agent.py  # Resume & cover letter agent
│   └── messaging_agent.py  # Outreach message agent
├── utils/
│   ├── config.py           # Environment variable loader
│   └── tracking.py         # Application logging utilities
├── data/
│   └── sample_resume.txt   # Sample resume for testing
├── requirements.txt
└── .gitignore
```
