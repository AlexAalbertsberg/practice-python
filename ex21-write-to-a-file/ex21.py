import requests
from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
req = requests.get(base_url)
soup = BeautifulSoup(req.text)
text_body = soup.select("div.article-main > div.content > section.content-section > p")


with open('test.txt', 'w') as open_file:
    for elem in text_body:
        open_file.write(elem.text)
