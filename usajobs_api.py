import requests
from utils.config import RAPIDAPI_KEY

def fetch_jobs(query, location="", num_pages=1):
    """
    Fetch job listings from JSearch (RapidAPI).
    Returns a list of job dicts with normalized keys.
    """
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }
    params = {
        "query": f"{query} in {location}" if location else query,
        "page": 1,
        "num_pages": num_pages,
        "country": "us",
        "date_posted": "all"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data", [])
        # Normalize into a simpler format
        jobs = []
        for item in data:
            city = item.get("job_city") or ""
            state = item.get("job_state") or ""
            location_str = f"{city}, {state}".strip(", ")
            jobs.append({
                "title": item.get("job_title") or "Unknown",
                "company": item.get("employer_name") or "Unknown",
                "location": location_str,
                "description": item.get("job_description") or "",
                "apply_link": item.get("job_apply_link") or "",
                "posted": item.get("job_posted_at_datetime_utc") or "",
                "employment_type": item.get("job_employment_type") or "",
            })
        return jobs
    else:
        print(f"JSearch API error: {response.status_code}")
        return []


if __name__ == "__main__":
    jobs = fetch_jobs("business analyst", location="San Francisco")
    for job in jobs:
        print(f"{job['title']} at {job['company']}")
