import requests
from bs4 import BeautifulSoup #dependecy

page = requests.get("https://www.google.com")
soup = BeautifulSoup(page.content, "html.parser")
print (soup.title.string)