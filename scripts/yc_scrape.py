import requests

def fetch_company_ids():
    '''
    This function fetches all hiring companies from YC's workatastartup.com
    '''
    # Headers for the request
    headers = {
        # Various headers for the request
    }

    # Data for the request
    request_data = '{"requests":[{"indexName":"WaaSPublicCompanyJob_created_at_desc_production","params":"query=&page=0&filters=&attributesToRetrieve=%5B%22company_id%22%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&hitsPerPage=10000&clickAnalytics=true&distinct=true"}]}'

    # Send a POST request to the server
    response = requests.post(
        'https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=ZGRlNGY5ZTU3YTg5Y2Q0ZjQ1M2UyODY0NTFmMmI4YjczNTQwNWUxZTU1NWRiZmZmYTlkNmY5NTJmZjMzYTA1OXRhZ0ZpbHRlcnM9JTVCJTVCJTIyam9ic19hcHBsaWNhbnQlMjIlNUQlNUQmYW5hbHl0aWNzVGFncz0lNUIlMjJ3YWFzJTIyJTVEJnVzZXJUb2tlbj1qOVlXYk5zTE9IQWhTSE44TGNlcUtWSHJVSEx4aHM1Nms4dmdIZGIwa09zJTNE',
        headers=headers,
        data=request_data,
    )

    # Convert the response to JSON
    response_data = response.json()

    # Extract the company IDs from the JSON data
    ids = [hit['company_id'] for result in response_data['results'] for hit in result['hits']]

    # Limit the company IDs to the first 10 for testing
    ids = ids[:10]

    return ids



def fetch_company_info(company_ids):
    '''
    This function takes a list of company IDs and returns their information
    '''
    # Cookies for the request
    cookies = {
        '_sso.key': 'M5WxISkq0Rf1rUa1vHXAat_27SO-LClp',
        '_bf_session_exists': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6ImRISjFaUT09IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuX2JmX3Nlc3Npb25fZXhpc3RzIn19--c09bf3da17accf4c53e92f910eef613c6f99527b',
        '_bf_session_key': '%2BWZ7WUxvc3IU5F9VMXG47a7MqQXFhlwEwhV%2BPQPpAXty3Blsmi0J5gLwmLWC2sobv9BaUJXRDFWEbBYFRfwCJztVO43nTzxRFEgNDWbK4z%2Bk9dDdLjUWVyZCGVDkEqpFxJl7YYCs3NpC%2B5HCDnvS7m31z9CgUfUAscLcL%2FoLuP%2B4V5oOBVWcu4x71dQOPMDgS%2FW4BlAHHrNaAk%2B059EwgX4gJI7gJHKi5Hp4guJHhYpCxHSryY%2B%2BgFXBBfGNvyYot0cv087Tdk5PBg85%2BohujsZo7FS0tUg%3D--2dx%2BSO1TjD3USNOs--hdPfa8ECOzLJ9d%2FjWV7a%2Bg%3D%3D',
    }
    # Headers for the request
    headers = {
        'authority': 'www.workatastartup.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,mt;q=0.8',
        'content-type': 'application/json',
        'cookie': '_sso.key=M5WxISkq0Rf1rUa1vHXAat_27SO-LClp; _bf_session_exists=eyJfcmFpbHMiOnsibWVzc2FnZSI6ImRISjFaUT09IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuX2JmX3Nlc3Npb25fZXhpc3RzIn19--c09bf3da17accf4c53e92f910eef613c6f99527b; _bf_session_key=%2BWZ7WUxvc3IU5F9VMXG47a7MqQXFhlwEwhV%2BPQPpAXty3Blsmi0J5gLwmLWC2sobv9BaUJXRDFWEbBYFRfwCJztVO43nTzxRFEgNDWbK4z%2Bk9dDdLjUWVyZCGVDkEqpFxJl7YYCs3NpC%2B5HCDnvS7m31z9CgUfUAscLcL%2FoLuP%2B4V5oOBVWcu4x71dQOPMDgS%2FW4BlAHHrNaAk%2B059EwgX4gJI7gJHKi5Hp4guJHhYpCxHSryY%2B%2BgFXBBfGNvyYot0cv087Tdk5PBg85%2BohujsZo7FS0tUg%3D--2dx%2BSO1TjD3USNOs--hdPfa8ECOzLJ9d%2FjWV7a%2Bg%3D%3D',
        'origin': 'https://www.workatastartup.com',
        'referer': 'https://www.workatastartup.com/companies?demographic=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=any&layout=list-compact&minExperience=6&sortBy=created_desc&tab=any&usVisaNotRequired=any',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        'x-csrf-token': '2I-xvPcO7YZTOzNasfzoLZdtwAGbIJSwjdFKq5NlbABY-nGrNTJGCCksYNysaokulkmQ_eQxfcoH9ObKS5BWUQ',
        'x-requested-with': 'XMLHttpRequest',
    }

        # Data for the request
    request_data = {
        'ids': ids
    }

    # Send a POST request to the server
    response = requests.post('https://www.workatastartup.com/companies/fetch', cookies=cookies, headers=headers, json=request_data)

    # Convert the response to JSON
    response_data = response.json()

    return response_data

# Get the company IDs
ids = fetch_company_ids()

# Get the company information
info = fetch_company_info(ids)

# Print the company information
print(info)