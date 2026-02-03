from bs4 import BeautifulSoup
import csv
import requests
import time
from urllib.parse import urljoin

base_url = "https://books.toscrape.com"
current_url = base_url
all_books = []

print("Starting scrapping...")

page = 0

while page != 50:
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
        
    next_button = soup.select_one("li.next a")
    
    if next_button:
        next_link = next_button['href']
        current_url = urljoin(current_url, next_link)
        print(f"Next button found, Moving to the next page")
        time.sleep(1)

        page+=1
            
    else: 
        print(f"No Next button found Reach the end")
        break
    
print(f"Scrapped {len(all_books)} books total")
file_name = "complete_library.csv"

with open(file_name, "w", newline="", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Stock", "Rating"])
    writer.writerows(all_books)
    
print(f"Saved to {file_name}")