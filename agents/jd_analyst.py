from crewai import Agent, Task, LLM
from utils.config import GEMINI_API_KEY

def _get_llm():
    return LLM(
        model="gemini/gemini-2.5-flash",
        api_key=GEMINI_API_KEY,
        temperature=0.2
    )


def get_jd_analyst_agent():
    return Agent(
        role="JD Analyst",
        goal="Understand and summarize job postings",
        backstory="You're an expert in job market analysis with deep knowledge of tech and business roles.",
        llm=_get_llm(),
        verbose=True
    )


def create_jd_analysis_task(agent, jd):
    return Task(
        description=f"""
        Analyze the following job posting and extract:
        - A summary of the role
        - Key skills required
        - Any specific qualifications or eligibility

        Job Description:
        {jd}
        """,
        expected_output="A structured markdown summary containing sections for Qualifications, Required Skills, and Responsibilities.",
        agent=agent,
    )