import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
print(f"Connecting to {url}...")
response = requests.get(url)

if response.status_code == 200:
    print(f"Connection Succesfull Parsing Books")
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = soup.select("article.product_pod")
    print(f"Found {len(books)} Books on the page. Extracting Data...")
    
    all_books = []
    
    for book in books:
        title = book.h3.find("a")['title']
        raw_price = book.select_one(".price_color").text
        stock = book.select_one(".instock.availability").text.strip()
        star_class = book.select_one(".star-rating")['class']
        rating = star_class[1] 
        
        print(f"📖 {title}")
        print(f"   💰 {raw_price} | 📦 {stock} | ⭐ {rating}")
        print("-" * 20)
    
    file_name = "books_inventory.csv"
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Stock", "Rating"])
        writer.writerows(all_books)
        
    print(f"Inventory Saved to {file_name}")
else:
    print("Failed to connect")