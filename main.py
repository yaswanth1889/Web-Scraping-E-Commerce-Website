#IMPORT REQUIRED PACKAGES

from bs4 import BeautifulSoup
import requests
import pandas as pd

#SELECT YOUR TARGET URL/LINK
url="https://www.boat-lifestyle.com/collections/true-wireless-earbuds"
allow=requests.get(url)

print(allow)

#PARSE THE TARGET HTML USING BEAUTIFULSOUP
soup=BeautifulSoup(allow.text)

print(soup)

#SCRAPE YOUR REQUIRED DATA USING SELECTORS

data=soup.select(".tile-title")

print(data)

Earbuds=[]
for item in data:
    Earbuds.append(item.text)
    
print(Earbuds)

price_data=soup.select(".price--highlight")

print(price_data)

Price=[]
for item in price_data:
    Price.append(item.text)
    
print(Price)

#CREATE A DATAFRAME USING SCRAPED DATA
wirelessearbuds=pd.DataFrame(Earbuds,columns=["Boat Wireless Earbuds"])

print(wirelessearbuds)

wirelessearbuds["Price"]=Price

print(wirelessearbuds)


#STRIP EXTRAS USING STRIP METHODS
wirelessearbuds["Price"]=wirelessearbuds["Price"].str.strip("\nSale priceFrom")

print(wirelessearbuds)

#SAVE AS CSV FILE
wirelessearbuds.to_csv("FILE NAME.csv")
