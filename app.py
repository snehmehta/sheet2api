import json
import requests 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/sheetapi')
async def api(url: str):

    parsed_url = url.split('/')   
    google_sheet_id = parsed_url[5]
    google_data_url = f'https://spreadsheets.google.com/feeds/cells/{google_sheet_id}/1/public/full?alt=json'

    response = requests.get(google_data_url)

    if response.status_code == 200:
        data = response.json()

        current_row = '1'
        index = 0
        headers = []
        parse_data = []
        row = {}
        for entry in data['feed']['entry']:
            cell = entry['gs$cell']

            if cell['row'] == '1':
                headers.append(cell['inputValue'])
                continue

            if cell['row'] != current_row:
                current_row = cell['row']
                parse_data.append(row)
                row = {}
                index = 0
            
            row[headers[index]] = cell['inputValue']
            index += 1

        parse_data.append(row)

        return {'status' : 'success','data' : parse_data[1:]}

    return {'status' : 'failed'}