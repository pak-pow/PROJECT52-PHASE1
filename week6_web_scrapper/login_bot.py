# Import the Selenium webdriver module to control a web browser
from selenium import webdriver

# Import the By class to locate elements on a webpage (by id, class, name, etc.)
from selenium.webdriver.common.by import By

# Import Keys to simulate keyboard inputs (like ENTER, RETURN)
from selenium.webdriver.common.keys import Keys

# Import time module to pause execution (used for waiting)
import time

# Create a new Chrome browser instance controlled by Selenium
driver = webdriver.Chrome()

# Define the URL of the login page
url = "https://quotes.toscrape.com/login"

# Print a message showing which URL the browser will connect to
print(f"Connecting to {url}")

# Open the specified URL in the Chrome browser
driver.get(url)

# Locate the username input field by its ID
username_input = driver.find_element(By.ID, "username")

# Locate the password input field by its ID
password_input = driver.find_element(By.ID, "password")

# Print a message indicating that credentials are being typed
print("typing credentials..")

# Type the username into the username input field
username_input.send_keys("my_secret_bot")

# Pause for 2 seconds to simulate human typing delay
time.sleep(2)

# Type the password into the password input field
password_input.send_keys("password123")

# Pause for 2 seconds to simulate human typing delay
time.sleep(2)

# Print a message indicating that the login process is starting
print("Logging in the web..")

# Simulate pressing the RETURN (Enter) key to submit the form
password_input.send_keys(Keys.RETURN)

# Wait 3 seconds for the login to process and the page to load
time.sleep(3)

# Check if there is a "Logout" link, which indicates successful login
if driver.find_elements(By.LINK_TEXT, "Logout"):
    
    # Print a message confirming that login was successful
    print("Access Granted, We are logged in...")
    
    # Get the username display element (usually inside <small> tag) to confirm site login
    user_display = driver.find_element(By.TAG_NAME, "small").text
    
    # Print the username confirmation from the site
    print(f"Site Confirms: {user_display}")
    
else:
    # Print a message if login failed
    print("Access Denied Log in failed")

# Print a message indicating that the browser session will close
print("Clossing off")

# Close the browser and end the Selenium session
driver.quit()
