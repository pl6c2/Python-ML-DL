import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Deep_learning'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify())

print(soup.find(id='firstHeading').string)

print(soup.find_all('a'))

for link in soup.find_all('a'):
    print(link.get('href'))
