import requests
from bs4 import BeautifulSoup


r = requests.get("http://www.pyclass.com/example.html",
     headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    
soup = BeautifulSoup(r.content,"html.parser")

content = soup.find_all("div", {"class":"cities"})
data = {}
for item in content:
    data[item.find_all("h2")[0].text] = item.find_all("p")[0].text
    # print(item.find_all("h2"))
    # print(item.find_all("p"))
    # print('\n')
print(data)