import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for i, item in enumerate(soup.select("div.feed-post-body-title a"), 1):
    titulo = item.get_text(strip=True)
    link = item.get("href")
    
    print(f"{i}. {titulo}")
    print(f"   {link}\n")
