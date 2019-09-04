
import requests
from bs4 import BeautifulSoup
import pandas as pd

def number_extractor_from_string(strg):
    '''
    accepts <strg> : string, that has \n and space char in it
    return the int value of the price that comes after $
    '''
    number = ''
    for char in strg:
        if char != '\n' and char != ' ':
            number += char
    return number

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", 
    headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

soup = BeautifulSoup(r.content)

alll= soup.find_all("div", {"class":"propertyRow"}) # len = 10

price_ls = []
for item in alll:
    price_ls.append( item.find("h4", {"class":"propPrice"}).text )
price_ls = list(map(number_extractor_from_string, price_ls))
addr_ls = []
for item in alll:
    addr_ls.append( item.find_all("span", {"class":"propAddressCollapse"})[0].text +', '+
            item.find_all("span", {"class":"propAddressCollapse"})[1].text )
bed_ls = []
sqft_ls = []
for item in alll:
    if item.find("span", {"class":"infoBed"}) != None:
        bed_ls.append( item.find("span", {"class":"infoBed"}).text[0])
    else:
        bed_ls.append(None)
    if item.find("span", {"class":"infoSqFt"}) != None:
        sqft_ls.append( item.find("span", {"class":"infoSqFt"}).text.replace("Sq. Ft", ""))
    else:
        sqft_ls.append(None)

bath_ls = []
for item in alll:
    Tag = item.find("div", {"class":"infoLine2"}).find("span", {"class":"infoValueFullBath"}) 
    if Tag != None:
        bath_ls.append(Tag.text[0])
    else:
        bath_ls.append(None)

pd.DataFrame({"Address": addr_ls, 
              "Price" : price_ls,
              "Sq Ft" : sqft_ls,
              "Number of Bedrooms" : bed_ls,
              "Number of Bathrooms" : bath_ls,
                }).to_csv("data.csv")