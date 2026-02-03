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
    
    for book in books:
        title = book.h3.find("a")['title']
        raw_price = book.select_one(".price_color").text
        price_text = raw_price.replace('£', '')
        price_text2 = price_text.replace('Â', '')
        price = float(price_text2)
        stock = book.select_one(".instock.availability").text.strip()
        rating = book.select_one(".star-rating")["class"][1]
        
        all_books.append([title, price, stock, rating])

        