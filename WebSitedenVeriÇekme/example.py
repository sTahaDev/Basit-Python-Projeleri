import requests as req
from bs4 import BeautifulSoup
URL = "https://stahadev.github.io"
response = req.get(URL)
html = response.text
doc = BeautifulSoup(html,"html.parser")

"""tag = doc.title
tag.string = "hello"
print(tag)"""

tags = doc.find_all("label")
print(tags[0])
