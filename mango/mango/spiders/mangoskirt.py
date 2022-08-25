import requests
from bs4 import BeautifulSoup
import json

URL = "https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="app")

skirt_elements = results.find_all("div", class_="product-detail-main")
for skirt_element in skirt_elements:
    name_skirt = skirt_elements.find_all("div", class_="product-name")
    price_skirt = skirt_elements.find_all("span", class_="product-sale product-sale--discount")
    colors_skirt = skirt_elements.find_all("div", class_="color-container", id="08, 99")
    sizes_skirt = skirt_elements.find_all("div", class_="selector-list")
    print(name_skirt.text.strip())
    print(price-skirt.text.strip())
    print(colors_skirt.text.strip())
    print(sizes_skirt.text.strip())
    print(output.json)


  