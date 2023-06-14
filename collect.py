import requests
from bs4 import BeautifulSoup

data = []
datalist = []

with open("url.txt", "r") as f:
    data.append(f.readlines())
f.close()

for s in data[0]:
    datalist.append(s.split())

for name, url in datalist:
    r = requests.get(f"https://ja.wikipedia.org{url}")
    soup = BeautifulSoup(r.text, "html.parser")
    soup = soup.find_all("p")
    with open(f"data/{name}.txt", "w", encoding="utf-8") as f:
        for s in soup:
            f.write(s.text)
    f.close()
