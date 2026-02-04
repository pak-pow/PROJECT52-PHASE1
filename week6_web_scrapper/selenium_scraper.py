# Import the Selenium webdriver module to control a web browser
from selenium import webdriver

# Import the By class to locate elements on a webpage (by class, id, name, etc.)
from selenium.webdriver.common.by import By 

# Import time module to pause execution (used to wait for JavaScript to load)
import time

# Print a message to indicate the browser automation is starting
print("Lunching chrome bot")

# Create a new Chrome browser instance controlled by Selenium
driver = webdriver.Chrome()

# Store the target website URL in a variable
url = "https://quotes.toscrape.com/js/"

# Print a message showing which URL the browser will navigate to
print(f"Navigating to {url}")

# Open the specified URL in the Chrome browser
driver.get(url)

# Print a message indicating the script is waiting for JavaScript content to load
print("Wating for JS to load...")

# Pause the script for 3 seconds to allow JavaScript-rendered content to appear
time.sleep(3)

# Find all elements on the page with the class name "quote"
quotes = driver.find_elements(By.CLASS_NAME, "quote")

# Print how many quote elements were found
print(f"found {len(quotes)} Quotes: \n")

# Loop through each quote element found on the page
for quote in quotes:
    
    # Find the child element with class "text" and extract its text content
    text = quote.find_element(By.CLASS_NAME, "text").text
    
    # Find the child element with class "author" and extract the author's name
    author = quote.find_element(By.CLASS_NAME, "author").text
    
    # Print the quote text
    print(f" {text}")
    
    # Print the author name with an em dash for formatting
    print(f"   — {author}")
    
    # Print a separator line for better readability
    print("-" * 20)

# Close the browser and end the Selenium session
driver.quit()
