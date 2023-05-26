import requests
from bs4 import BeautifulSoup #dependecy

def get_title(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.title.string