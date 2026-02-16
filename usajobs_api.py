import requests
from utils.config import USAJOBS_API_KEY

# import http.client

# conn = http.client.HTTPSConnection("jsearch.p.rapidapi.com")

# headers = {
#     'x-rapidapi-key': "69bbcbdaaemsh61fb2f8e0bc8e83p1a10f3jsn0010555c1646",
#     'x-rapidapi-host': "jsearch.p.rapidapi.com"
# }

# conn.request("GET", "/search?query=developer%20jobs%20in%20chicago&page=1&num_pages=1&country=us&date_posted=all", headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

def fetch_usajobs(keyword, location, results_per_page=5):
    headers = {
        'Authorization-Key' : USAJOBS_API_KEY,
        'User-Agent': "yadnyawalka7@gmail.com",  
        'Host': "data.usajobs.gov"
        
    }
    params = {
        'keyword' : keyword,
        'LocationNamer': location,
        'ResultsPerPage': results_per_page
    }

    url = f"https://data.usajobs.gov/api/search?{keyword}&LocationName={location}&ResultsPerPage={results_per_page}"
    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        return response.json().get('SearchResult', {}).get('SearchResultItems', [])
    else:
        return []


if __name__ == "__main__":
    jobs = fetch_usajobs("business analyst", location="San Francisco", results_per_page=10)
    for job in jobs:
        title = job['MatchedObjectDescriptor']['PositionTitle']
        agency = job['MatchedObjectDescriptor']['OrganizationName']
        print(f"{title} at {agency}")


