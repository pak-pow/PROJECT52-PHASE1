from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

print("Lunching chrome bot")
driver = webdriver.Chrome()

url = "https://quotes.toscrape.com/js/"
print(f"Navigating to {url}")
driver.get(url)

print("Wating for JS to load...")
time.sleep(3)

quotes = driver.find_elements(By.CLASS_NAME, "quote")
print(f"found {len(quotes)} Quotes: \n")

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    
    print(f" {text}")
    print(f"   — {author}")
    print("-" * 20)
    
driver.quit()