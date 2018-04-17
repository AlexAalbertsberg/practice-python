import requests
from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
req = requests.get(base_url)
soup = BeautifulSoup(req.text)
text_body = soup.select("div.article-main > div.content > section.content-section > p")

for elem in text_body:
    print(elem.text)
