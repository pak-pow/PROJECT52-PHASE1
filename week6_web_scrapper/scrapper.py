import requests
from bs4 import BeautifulSoup
import csv

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
    
    # We will store our data in this list
    data_to_save = []
    
    # Loop through ONLY the top 10 headlines ([:10])
    print("\n🔍 Extracting Top 10 Headlines & Links:\n")
    
    for i, headline in enumerate(headlines[:10], 1):
        # 1. Get the Text
        text = headline.find("a").get_text()
        
        # 2. Get the Link (The 'href' attribute inside the <a> tag)
        link = headline.find("a")['href']
        
        # 3. Print to console (so we can see it working)
        print(f"{i}. {text}")
        print(f"   👉 {link}")
        
        # 4. Add to our list
        data_to_save.append([i, text, link])
    
    
    filename = "hackernews.csv"
    print(f"\n💾 Saving to {filename}...")
    
    # 'w' = write mode
    # newline='' prevents empty lines between rows
    # encoding='utf-8' handles special characters (like emojis or quotes)
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write the Header Row
        writer.writerow(["Rank", "Headline", "Link"])
        
        # Write the Data Rows
        writer.writerows(data_to_save)
        
    print("✅ Done! Check your folder.")
    
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