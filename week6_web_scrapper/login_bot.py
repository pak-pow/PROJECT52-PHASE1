from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "https://quotes.toscrape.com/login"
print(f"Connecting to {url}")
driver.get(url)

username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

print("typing credentials..")
username_input.send_keys("my_secret_bot")
time.sleep(2)

password_input.send_keys("password123")
time.sleep(2)

print("Logging in the web..")
password_input.send_keys(Keys.RETURN)

