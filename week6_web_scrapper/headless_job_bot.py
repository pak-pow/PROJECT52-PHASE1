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
    
    url = "https://realpython.github.io/fake-jobs/"
    print(f"Connecting to {url}")
    driver.get(url)
    
    time.sleep(1)
    
    jobs_card = driver.find_elements(By.CLASS_NAME, "card-content")
    print(f"found {len(jobs_card)} total listings. Filtering for 'python' ")
    
    data = []
    
    for card in jobs_card:
        title = card.find_element(By.TAG_NAME, "h2").text
        company = card.find_element(By.TAG_NAME, "h3").text
        location = card.find_element(By.CLASS_NAME, "location").text
        
        links= card.find_elements(By.TAG_NAME, "a")
        apply_link = "N/A"
        
        for link in links:
            if link.text == "Apply":
                apply_link = link.get_attribute("href")
                break
        
        if "Python" in title:
            print(f"    MATCH: {title} @ {company}")
            data.append([title, company, location, apply_link])

except Exception as e:
    print(f"Error: {e}")
    
finally:
    driver.quit()
    print("ghost bot deactivated")