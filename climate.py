import requests
from bs4 import BeautifulSoup

search = "weather in São Paulo"
url = f"https://www.google.com/search?q=weather+{search}"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
update = s.find("div", class_="BNeawe").text
print(update)