import requests
import re

# The API endpoint
url = "https://bidplus.gem.gov.in/all-bids"

# A GET request to the API
response = requests.get(url)
print(response.status_code)
cookie_string = response.cookies

print(cookie_string)
cookiesCsrf = re.search(r'csrf_gem_cookie=([a-f0-9]+)', str(cookie_string)).group(1)
print(cookiesCsrf)

cookiesSession = re.search(r'ci_session=([a-f0-9]+)', str(cookie_string)).group(1)
print(cookiesSession)

cookies = "ci_session="+cookiesSession+"; csrf_gem_cookie="+cookiesCsrf

# The API endpoint
url1 = "https://bidplus.gem.gov.in/all-bids-data"

# New headers
headers1 = {
     "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Content-Length":"380",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":cookies,
    "DNT": "1",
    "Host": "bidplus.gem.gov.in",
    "Origin": "https://bidplus.gem.gov.in",
    "Referer": "https://bidplus.gem.gov.in/all-bids",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "X-Requested-With": "XMLHttpRequest"
}

# New payload
payload = {
    "param": {"searchBid": "data+entry", "searchType": "fullText"},
    "filter": {"bidStatusType": "ongoing_bids", "byType": "all", "highBidValue": "", "byEndDate": {"from": "", "to": ""}, "sort": "Bid-End-Date-Oldest"},
    "csrf_bd_gem_nk": cookiesCsrf
}

# Making the request
response2 = requests.post(url1, headers=headers1, data=payload)
base_url_ra = "https://bidplus.gem.gov.in/showradocumentPdf/"
base_url_bid = "https://bidplus.gem.gov.in/showbidDocument/"
# Processing the response
if response2.status_code == 200:
    # Process the response here
    print(response2.json())
    data =response2.json()
    print(data)
    for doc in data['response']['response']['docs']:
        b_id = doc['b_id'][0]
        print(b_id)
        '''b_ra_to_bid = doc['b_ra_to_bid'][0]

        # Construct the URL based on the value of 'b_ra_to_bid'
        if b_ra_to_bid == 1:
            url = base_url_ra + str(b_id)
        else:
            url = base_url_bid + str(b_id)

        print("URL for b_id:", b_id)
        print("URL:", url)
        # Make a request to fetch the document
        response = requests.get(url)

        # Process the response
        if response.status_code == 200:
            # Process the document here
            # For example, you can save it to a file or further process it
            pass
        else:
            print("Error fetching document:", response.status_code)'''
else:
    pass
    print("Error:", response2.status_code)





# Print the response headers


