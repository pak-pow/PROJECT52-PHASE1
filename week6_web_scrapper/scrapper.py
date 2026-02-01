import requests
from bs4 import BeautifulSoup

# our targer 
# we are going to be scrapping the hacker news it is a simple text-based tech news site
url = "https://news.ycombinator.com/"

# getting the request
print(f"Connecting to {url}...")
response = requests.get(url)

if response.status_code == 200:
    
    # soup 
    # this turns the raw text into a navigatable tree
    soup = BeautifulSoup(response.text, "html.parser")
    
    # searching
    # looking for a span tags that have a class titleline
    headlines = soup.select("span.titleline")
    
    # looping
    # iterating through the list of headlines we found
    print(f"\nFound {len(headlines)} Headlines:\n")
    
    for i, headline in enumerate(headlines, 1):
        # The actual text is inside an <a> tag inside the <span>
        text = headline.find("a").get_text()
        print(f"{i}. {text}")

else:
    print("Failed to Connect")



# ============================================================
# 200 ok
# 404 not found
# 403 forbidden, it means they blocked our bot
#print(f"Status Code: {response.status_code}")

# "response.text" is the raw HTML code of the website.
# We will print just the first 500 characters to verify it worked.
#print("\nRAW HTML PREVIEW:")
#print("--------------------------------------------------")
#print(response.text[:500])  # Slicing the string to show only start
#print("--------------------------------------------------")