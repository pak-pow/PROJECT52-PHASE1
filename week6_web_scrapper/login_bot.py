from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "https://quotes.toscrape.com/login"
print(f"Connecting to {url}")
driver.get(url)