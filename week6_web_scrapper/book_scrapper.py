import requests
# Imports the requests library, which allows the program to send HTTP requests to websites

import csv
# Imports the csv module, which lets us write data into a CSV file

from bs4 import BeautifulSoup
# Imports BeautifulSoup from bs4 to parse and navigate HTML content


url = "https://books.toscrape.com"
# Stores the website URL that we want to scrape in a variable

print(f"Connecting to {url}...")
# Prints a message showing which website the program is trying to connect to

response = requests.get(url)
# Sends an HTTP GET request to the URL and stores the server's response


if response.status_code == 200:
    # Checks if the request was successful (200 means OK)

    print(f"Connection Succesfull Parsing Books")
    # Prints a confirmation message when the connection is successful

    soup = BeautifulSoup(response.text, "html.parser")
    # Converts the HTML content of the response into a BeautifulSoup object for easy parsing
    
    books = soup.select("article.product_pod")
    # Selects all HTML elements that represent individual books and stores them in a list

    print(f"Found {len(books)} Books on the page. Extracting Data...")
    # Prints how many books were found on the page
    
    all_books = []
    # Creates an empty list to store all extracted book data
    
    for book in books:
        # Loops through each book element found on the page

        title = book.h3.find("a")['title']
        # Extracts the book title from the 'title' attribute of the anchor tag

        raw_price = book.select_one(".price_color").text
        # Gets the raw price text (including symbols) from the price element

        price_text = raw_price.replace('£', '')
        # Removes the pound (£) symbol from the price string

        price_text2 = price_text.replace('Â', '')
        # Removes unwanted encoding characters from the price string

        price = float(price_text2)
        # Converts the cleaned price string into a floating-point number

        stock = book.select_one(".instock.availability").text.strip()
        # Extracts stock availability text and removes extra whitespace

        star_class = book.select_one(".star-rating")['class']
        # Gets the list of CSS classes that describe the star rating

        rating = star_class[1]
        # Extracts the rating value (e.g., One, Two, Three) from the class list
        
        print(f"📖 {title}")
        # Prints the book title

        print(f"   💰 {raw_price} | 📦 {stock} | ⭐ {rating}")
        # Prints the price, stock status, and rating of the book

        print("-" * 20)
        # Prints a separator line for readability
        
        all_books.append([title, price, stock, rating])
        # Adds the book's data as a list into the all_books list
    
    file_name = "books_inventory.csv"
    # Defines the name of the CSV file to be created

    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        # Opens (or creates) the CSV file in write mode using UTF-8 encoding

        writer = csv.writer(file)
        # Creates a CSV writer object to write data into the file

        writer.writerow(["Title", "Price", "Stock", "Rating"])
        # Writes the header row into the CSV file

        writer.writerows(all_books)
        # Writes all book records into the CSV file
        
    print(f"Inventory Saved to {file_name}")
    # Prints a message confirming the CSV file was saved

else:
    # Executes if the website connection failed

    print("Failed to connect")
    # Prints an error message if the request was unsuccessful
