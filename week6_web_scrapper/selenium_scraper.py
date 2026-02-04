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