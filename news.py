import requests
from bs4 import BeautifulSoup

# URL of website
url = "https://www.bbc.com/news"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

#  headline tags (BBC)
headlines = soup.find_all("h3")

# store in list
headline_list = []
for h in headlines:
    text = h.text.strip()
    if text != "":
        headline_list.append(text)

# Save to text
with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headline_list:
        file.write(headline + "\n")

print("Headlines saved successfully!")