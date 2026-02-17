from crewai import Crew, Process
from agents.jd_analyst import get_jd_analyst_agent, create_jd_analysis_task
from agents.resume_cl_agent import get_resume_cl_agent, create_resume_cl_task
from agents.messaging_agent import get_messaging_agent, create_messaging_task
from usajobs_api import fetch_jobs

def load_resume(path="data/sample_resume.txt"):
    with open(path, "r") as file:
        return file.read()

def run_pipeline(keyword="business analyst", location="New York", resume_text=None, user_bio=None):
    # Step 1: Fetch job posts from JSearch
    job_posts = fetch_jobs(keyword, location)
    if not job_posts:
        return [], None

    job = job_posts[0]
    job_description = job["description"]
    company_name = job["company"]
    job_title = job["title"]

    # Step 2: Load resume
    if not resume_text:
        resume_text = load_resume()
    if not user_bio:
        user_bio = "I'm a data professional passionate about public service."

    # Step 3: Initialize agents
    jd_agent = get_jd_analyst_agent()
    resume_agent = get_resume_cl_agent()
    message_agent = get_messaging_agent()

    # Step 4: Create tasks
    jd_task = create_jd_analysis_task(jd_agent, job_description)
    resume_task = create_resume_cl_task(resume_agent, job_description, resume_text)
    message_task = create_messaging_task(message_agent, job_description, company_name, user_bio)

    # Step 5: Create and run the crew
    crew = Crew(
        agents=[jd_agent, resume_agent, message_agent],
        tasks=[jd_task, resume_task, message_task],
        process=Process.sequential
    )
    result = crew.kickoff()

    # Extract individual task outputs
    task_outputs = result.tasks_output
    agent_results = {
        "job_title": job_title,
        "company": company_name,
        "jd_analysis": str(task_outputs[0]) if len(task_outputs) > 0 else "",
        "resume_cover_letter": str(task_outputs[1]) if len(task_outputs) > 1 else "",
        "outreach_message": str(task_outputs[2]) if len(task_outputs) > 2 else "",
    }

    return job_posts, agent_results


if __name__ == "__main__":
    jobs, results = run_pipeline()
    print("\n=== FINAL OUTPUT ===\n")
    print(results)