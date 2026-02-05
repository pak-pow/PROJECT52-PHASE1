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
time.sleep(3)

if driver.find_elements(By.LINK_TEXT, "Logout"):
    print("Access Granted, We are logged in...")
    user_display = driver.find_element(By.TAG_NAME, "small").text
    print(f"Site Confirms: {user_display}")
    
else:
    print("Access Denied Log in failed")
    
print("Clossing off")
driver.quit()