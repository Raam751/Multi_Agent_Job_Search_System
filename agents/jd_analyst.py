from crewai import Agent
from crewai import Task
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.2,
    google_api_key = GEMINI_API_KEY
)


def get_jd_analyst_agent():
    return Agent(
        role="JD Analyst",
        goal="Understand and summarize government job postings",
        backstory="You're an expert in job market analysis with a focus on US federal job listings.",
        llm =llm,
        verbose=True
    )


def create_jd_analysis_task(agent, jd):
    return Task(
        description=f"""
        Analyze the following USAJobs job posting and extract:
        - A sumary of the role
        - key skills required
        - Any specific qualifications or eligibility
        \n\nJob Description:\n{jd}
        """,
        expected_output="A structured markdown summary containing sections for Qualifications, Required Skills, and Responsibilities.",
        agent = agent,
        output_file='/data/report.md'
    )