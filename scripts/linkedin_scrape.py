from linkedin_api import Linkedin
from dotenv import load_dotenv
import os
import re

load_dotenv()

def extract_number(s):
    number = re.findall(r'\d+', s)
    return number[0] if number else None

# LinkedIn API Docs (unofficial)
# https://linkedin-api.readthedocs.io/en/latest/api.html

# Authenticate using any Linkedin account credentials
api = Linkedin(os.getenv("LINKEDIN_EMAIL"), os.getenv("LINKEDIN_PASSWORD"))

query_jobs = api.search_jobs(keywords="software developer", experience=["1", "2", "3"], location_name=None, listed_at=2628000, limit=-1)
for query in query_jobs:
    dash_entity_urn = query["dashEntityUrn"]
    job_id = extract_number(dash_entity_urn)
    job_info = api.get_job(job_id)
    company = job_info["companyDetails"]["com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany"]["companyResolutionResult"]["name"]
    job_title = job_info["title"]
    print(f"{job_title} at {company}")