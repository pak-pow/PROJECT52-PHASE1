from bs4 import BeautifulSoup
import csv
import requests
import time
from urllib.parse import urljoin

base_url = "https://books.toscrape.com"
current_url = base_url
all_books = []

print("Starting scrapping...")

while True:
    print(f"Scrapping: {base_url}")
    respone = requests.get(base_url)
    soup = BeautifulSoup(respone.text, "html.parser")
    
    books = soup.select("article.product_pod")