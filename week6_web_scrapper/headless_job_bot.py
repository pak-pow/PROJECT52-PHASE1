import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")

print("Initializing ghost bot without the window.")
driver = webdriver.Chrome(options=chrome_options)

try:
    pass

except Exception as e:
    print(f"Error: {e}")
    
finally:
    driver.quit()
    print("ghost bot deactivated")