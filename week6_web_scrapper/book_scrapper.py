import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
print(f"Connecting to {url}...")
response = requests.get(url)

if response.status_code == 200:
    print(f"Connection Succesfull Parsing Books")

else:
    print("Failed to connect")