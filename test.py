import requests
from bs4 import BeautifulSoup

r = requests.get("https://ja.wikipedia.org/wiki/都道府県")

soup = BeautifulSoup(r.text, "html.parser")

soup = soup.find(name="div", attrs={"class":"mw-parser-output"})

soup = soup.find_all(name="tbody")

soup = soup[6]

soup = soup.find_all(name="a")

with open("url.txt", "w", encoding="utf-8") as f:
    for i in soup:
        if i.get("title") == None:
            f.write("None ")
        else:
            f.write(i.get("title") + " ")
        if i.get("href") == None:
            f.write("None\n")
        else:
            f.write(i.get("href") + "\n")

f.close()
