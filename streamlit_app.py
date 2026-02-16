import streamlit as st
from orchestrator import run_pipeline
from usajobs_api import fetch_usajobs

st.set_page_config(page_title="AI Job Hunt Assistant", layout="centered")

st.title("AI Job Hunt Assistant")
st.markdown("Use AI agents to analyze jobs, tailor your resume, and write outreach messages — all from one interface.")

# Input fields
keyword = st.text_input("Job Keyword", "business analyst")
location = st.text_input("Location", "New York")
resume_text = st.text_area("Paste Your Resume", height=200)
user_bio = st.text_area("Short Bio (for outreach tone)", "I’m a data professional passionate about public service.")

if st.button("Run Job Hunt Assistant"):
    if not resume_text.strip():
        st.warning("Please paste your resume before running the workflow.")
    else:
        with st.spinner("Running AI agents..."):
            job_posts = fetch_usajobs(keyword, location)
            if not job_posts:
                st.error("No job postings found for this search.")
            else:
                job_data = job_posts[0]['MatchedObjectDescriptor']
                result = run_pipeline()
                st.success("✅ Agents completed their tasks!")
                st.markdown("---")
                st.markdown("### 📝 Agent Results")
                st.markdown(result)