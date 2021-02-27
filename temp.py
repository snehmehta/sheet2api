#%%
import urllib
# %%
url = 'https://docs.google.com/spreadsheets/d/1U_mGrerkvUZvyL84nqk8GfT4cmTsPKw1UmBSXb-8Crg/edit?usp=sharing'

parsed_url_list = url.split('/')
# %%
google_sheet_id = parsed_url_list[5]

json_response = f'https://spreadsheets.google.com/feeds/cells/{google_sheet_id}/1/public/full?alt=json'
# %%
print(json_response)
import requests

url = f'http://localhost:8000/sheetapi?url={json_response}'
response = requests.get(url)
# %%
import json
print(json.loads(response.content))
# %%
