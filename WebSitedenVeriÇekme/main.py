import requests as req
from bs4 import BeautifulSoup
URL2 = "https://www.trendyol.com/riot-games/5250-vp-valorant-points-tr-p-40275317?boutiqueId=61&merchantId=390888&sav=true"
URL = "https://www.trendyol.com/apple/macbook-pro-13-3-m2-10c-gpu-8gb-256-gb-ssd-uzay-grisi-p-335850813?boutiqueId=61&merchantId=203702"
result = req.get(URL2)
result = result.text

html = BeautifulSoup(result,"html.parser")

class1 = html.find(class_ = "prc-dsc")
price = class1.text

class2 = html.find(class_ = "pr-new-br")
span = class2.find("span")
name = span.text
print("***Ürün Bilgileri***")
print(f"Ürün Adı: {name}")
print(f"Ürün Fiyatı: {price}")


