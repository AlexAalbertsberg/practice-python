import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com"
req = requests.get(url)
req_html = req.text

soup = BeautifulSoup(req_html)

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
