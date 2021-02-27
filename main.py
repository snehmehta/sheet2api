import pandas as pd
from bs4 import BeautifulSoup 
import requests
from selenium import webdriver 

driver = webdriver.Chrome()
driver.get('https://free-for.dev/#/')
input('Waiting for input')

soup = BeautifulSoup(driver.page_source, 'html.parser')

links = []
datas = []
categories = []
descriptions = []

counter = 0

for ul in soup.find_all('ul'):
    for li in ul.findAll('li'):
        a_tags = li.findAll('a')

        for a in a_tags:
            links.append(a['href'])
            datas.append(a.text)
            descriptions.append(li.text)
            
            counter += 1

        
        
print(len(links), len(datas), len(categories))



data = { 'Name' : datas,'link' : links,'Description' : descriptions }

df = pd.DataFrame(data=data)
df.to_excel('free4dev.xlsx',header=False, index=False)

driver.close()