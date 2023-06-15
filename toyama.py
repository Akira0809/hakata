import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.nta.co.jp/media/tripa/articles/NKqad")
soup = BeautifulSoup(r.text, "html.parser")
name = soup.find(name="h1", attrs={"class":"media-heading"}).text
name = name.replace("旅行完全ガイド！おすすめ観光スポット・グルメ・お土産をチェック", "")
soup = soup.find_all(name="a", attrs={"class":"btn btn-item-link noext"})
datalist = []
url_list = []
for i in soup:
    datalist.append(i.get("href"))
url_list += (datalist[:4])
url_list += (datalist[6:9])
for i in url_list:
    response = requests.get(i)
    s = BeautifulSoup(response.text, "html.parser")
    title = s.find_all(name="h2", attrs={"class":"item-body"})
    text = s.find_all(name="div", attrs={"class":"item-body-hbr"})
    with open(f"data_sightseeing/{name}_sightseeing.txt", "a", encoding="utf-8") as f:
        for j, k in zip(title, text):
            f.write(j.text + "\n")
            f.write(k.text + "\n")
    f.close()
