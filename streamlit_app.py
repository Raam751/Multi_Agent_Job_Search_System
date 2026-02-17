import streamlit as st
from orchestrator import run_pipeline

st.set_page_config(page_title="AI Job Hunt Assistant", layout="centered")

st.title("🤖 AI Job Hunt Assistant")
st.markdown("Use AI agents to analyze jobs, tailor your resume, and write outreach messages — all from one interface.")

# Input fields
keyword = st.text_input("Job Keyword", "business analyst")
location = st.text_input("Location", "New York")
resume_text = st.text_area("Paste Your Resume", height=200)
user_bio = st.text_area("Short Bio (for outreach tone)", "I'm a data professional passionate about public service.")

if st.button("🚀 Run Job Hunt Assistant"):
    if not resume_text.strip():
        st.warning("Please paste your resume before running the workflow.")
    else:
        with st.spinner("Running AI agents... this may take a minute ⏳"):
            try:
                jobs, agent_results = run_pipeline(
                    keyword=keyword,
                    location=location,
                    resume_text=resume_text,
                    user_bio=user_bio
                )

                if not jobs:
                    st.error("❌ No job posts found for this search.")
                else:
                    # --- Job Listings ---
                    st.markdown("---")
                    st.markdown("### 🔍 Jobs Found")
                    for i, job in enumerate(jobs, 1):
                        with st.expander(f"**{i}. {job['title']}** — {job['company']}"):
                            st.markdown(f"📍 **Location:** {job['location']}")
                            st.markdown(f"💼 **Type:** {job['employment_type']}")
                            st.markdown(f"📅 **Posted:** {job['posted'][:10] if job['posted'] else 'N/A'}")
                            if job['apply_link']:
                                st.markdown(f"🔗 [Apply Here]({job['apply_link']})")
                            st.markdown("**Description:**")
                            desc = job['description']
                            st.markdown(desc[:500] + "..." if len(desc) > 500 else desc)

                    # --- Agent Results ---
                    st.success(f"✅ Agents analyzed: **{agent_results['job_title']}** at **{agent_results['company']}**")
                    st.markdown("---")

                    # 1. Job Analysis
                    with st.expander("📋 Job Analysis", expanded=True):
                        st.markdown(agent_results["jd_analysis"])

                    # 2. Tailored Resume & Cover Letter
                    with st.expander("📄 Tailored Resume & Cover Letter", expanded=True):
                        st.markdown(agent_results["resume_cover_letter"])

                    # 3. Outreach Message
                    with st.expander("✉️ Outreach Message", expanded=True):
                        st.markdown(agent_results["outreach_message"])

            except Exception as e:
                st.error(f"❌ Something went wrong: {str(e)}")