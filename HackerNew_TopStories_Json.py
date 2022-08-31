import requests
import json

#Make the API call and store response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')


#Review data
response_dict = r.json()

readable_file = 'readable_hs_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
    
