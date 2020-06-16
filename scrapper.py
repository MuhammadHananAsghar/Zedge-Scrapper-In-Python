import requests
from bs4 import BeautifulSoup
def Zedge(search):
    import requests
    from bs4 import BeautifulSoup
    html_data = requests.get(f"https://www.zedge.net/find/wallpapers/{search}")
    html = html_data.content
    soup = BeautifulSoup(html,"html.parser")
    anchors = soup.find_all("a",class_="igLGYr")
    values = []
    for i in anchors:
        value = "https://www.zedge.net"+i.attrs.get("href")
        values.append(value)
    values2 = []
    for i in values:
        soup2 = BeautifulSoup(requests.get(i).content,"html.parser")
        values2.append(soup2)
    values3 = []
    link = ""
    for i in range(len(values2)):
        a = values2[i].find_all("script")
        a = a[0]
        b = a.string[355:]
        c = [i for i in b]
        c.pop()
        c.pop()
        link = "".join(c)
        values3.append(link)
    values4 = []
    for i in range(len(values3)):
        value = values3[i].find("=")
        value2 = values3[i][value+1:]
        value3 = "https://fsa.zobj.net/crop.php?r="+value2
        values4.append(value3)
    return values4
a = Zedge("bikes")
