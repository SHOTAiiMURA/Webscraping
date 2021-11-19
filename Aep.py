import requests
from bs4 import BeautifulSoup

url = "https://www.tuj.ac.jp/events/index.html"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

table = soup.find(class_="grid grid-4")

components = table.find_all(class_="tmb-alignleft")

event_list = []
data_dict = {}

for comp in components:
    data_dict["title"] = comp.find("h2").text
    data_dict["date"] = comp.find("h3").text

    event_list.append(data_dict)
    data_dict = {}

for event in event_list:
    print(event)
