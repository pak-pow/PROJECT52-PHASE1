# Import BeautifulSoup for parsing and navigating HTML content
from bs4 import BeautifulSoup

# Import csv module to write scraped data into a CSV file
import csv

# Import requests to send HTTP requests to websites
import requests

# Import time to add delays between page requests
import time

# Import urljoin to properly construct full URLs from relative links
from urllib.parse import urljoin

# Define the base URL of the website to scrape
base_url = "https://books.toscrape.com"

# Set the current URL to the base URL (starting page)
current_url = base_url

# Create a list to store all scraped book data
all_books = []

# Print a message indicating the scraping process has started
print("Starting scrapping...")

# Initialize a page counter
page = 0

# Loop until 50 pages are scraped
while page != 50:
    
    # Print which page URL is currently being scraped
    print(f"Scrapping: {current_url}")
    
    # Send an HTTP GET request to the current page
    respone = requests.get(current_url)
    
    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(respone.text, "html.parser")
    
    # Select all book containers on the page
    books = soup.select("article.product_pod")
    
    # Loop through each book found on the page
    for book in books:
        
        # Extract the book title from the anchor tag's title attribute
        title = book.h3.find("a")['title']
        
        # Get the raw price text (e.g., '£51.77')
        raw_price = book.select_one(".price_color").text
        
        # Remove the pound symbol from the price
        price_text = raw_price.replace('£', '')
        
        # Remove unwanted encoding characters (e.g., 'Â')
        price_text2 = price_text.replace('Â', '')
        
        # Convert the cleaned price string into a float
        price = float(price_text2)
        
        # Extract stock availability text and remove extra whitespace
        stock = book.select_one(".instock.availability").text.strip()
        
        # Extract the rating class (e.g., One, Two, Three)
        rating = book.select_one(".star-rating")["class"][1]
        
        # Append the extracted book data as a row to the list
        all_books.append([title, price, stock, rating])
    
    # Look for the "Next" page button
    next_button = soup.select_one("li.next a")
    
    # If a next page exists
    if next_button:
        
        # Get the relative link to the next page
        next_link = next_button['href']
        
        # Build the full URL for the next page
        current_url = urljoin(current_url, next_link)
        
        # Inform that the scraper is moving to the next page
        print(f"Next button found, Moving to the next page")
        
        # Pause for 1 second to avoid sending requests too quickly
        time.sleep(1)

        # Increment the page counter
        page += 1
            
    else: 
        # If no next button is found, stop scraping
        print(f"No Next button found Reach the end")
        break

# Print the total number of books scraped
print(f"Scrapped {len(all_books)} books total")

# Define the output CSV file name
file_name = "complete_library.csv"

# Open the CSV file in write mode
with open(file_name, "w", newline="", encoding='utf-8') as f:
    
    # Create a CSV writer object
    writer = csv.writer(f)
    
    # Write the header row
    writer.writerow(["Title", "Price", "Stock", "Rating"])
    
    # Write all scraped book rows
    writer.writerows(all_books)
    
# Confirm that the data has been saved
print(f"Saved to {file_name}")
