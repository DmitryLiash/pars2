import requests
from bs4 import BeautifulSoup
import json

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
#                   "Chrome/116.0.0.0 Safari/537.36"
# }
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

with open("index.html", encoding="utf-8") as file:
    scr = file.read()

soup = BeautifulSoup(scr, "lxml")
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
all_categories_dict = {}
for el in all_products_hrefs:
    el_text = el.text
    el_href = "https://health-diet.ru" + el.get("href")
    # print(f"{el_text}: {el_href}")
    all_categories_dict[el_text] = el_href

with open("all_categories_dict.json", "w", encoding="utf-8") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
