import requests

# our targer 
# we are going to be scrapping the hacker news it is a simple text-based tech news site
url = "https://news.ycombinator.com/"

# getting the request
print(f"Connecting to {url}...")
response = requests.get(url)