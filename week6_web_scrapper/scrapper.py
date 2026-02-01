import requests

# our targer 
# we are going to be scrapping the hacker news it is a simple text-based tech news site
url = "https://news.ycombinator.com/"

# getting the request
print(f"Connecting to {url}...")
response = requests.get(url)

# 200 ok
# 404 not found
# 403 forbidden, it means they blocked our bot
print(f"Status Code: {response.status_code}")

# "response.text" is the raw HTML code of the website.
# We will print just the first 500 characters to verify it worked.
print("\nRAW HTML PREVIEW:")
print("--------------------------------------------------")
print(response.text[:500])  # Slicing the string to show only start
print("--------------------------------------------------")