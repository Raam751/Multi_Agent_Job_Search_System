from crewai import Crew, Process
from agents.jd_analyst import get_jd_analyst_agent, create_jd_analysis_task
from agents.resume_cl_agent import get_resume_cl_agent, create_resume_cl_task
from agents.messaging_agent import get_messaging_agent, create_messaging_task
from usajobs_api import fetch_usajobs

def load_resume(path="data/sample_resume.txt"):
    with open(path, "r") as file:
        return file.read()

def run_pipeline():
    # Step 1: Fetch job post
    job_posts = fetch_usajobs("business analyst", location="New York")
    if not job_posts:
        print("No job posts found.")
        return

    job_data = job_posts[0]['MatchedObjectDescriptor']
    job_summary = job_data['UserArea']['Details']['JobSummary']
    agency_name = job_data.get('OrganizationName', 'Unknown Agency')
    job_title = job_data.get('PositionTitle', 'Unknown Position')

    # Step 2: Load resume and bio
    resume_text = load_resume()
    user_bio = "I'm a data professional passionate about public service."

    # Step 3: Initialize agents
    jd_agent = get_jd_analyst_agent()
    resume_agent = get_resume_cl_agent()
    message_agent = get_messaging_agent()

    # Step 4: Create tasks
    jd_task = create_jd_analysis_task(jd_agent, job_summary)
    resume_task = create_resume_cl_task(resume_agent, job_summary, resume_text)
    message_task = create_messaging_task(message_agent, job_summary, agency_name, user_bio)

    # Step 5: Create and run the crew
    crew = Crew(
        agents=[jd_agent, resume_agent, message_agent],
        tasks=[jd_task, resume_task, message_task],
        process=Process.sequential
    )
    result = crew.kickoff()

    print("\n=== FINAL OUTPUT ===\n")
    print(result)

if __name__ == "__main__":
    run_pipeline()