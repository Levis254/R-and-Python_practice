from bs4 import BeautifulSoup
import requests

url="https://nairobicomputershop.co.ke/"
result=requests.get(url)

doc=BeautifulSoup(result.text, "html.parser")

#To see the title of the website
doc.head.title.string

#to create the price list for old prices
prices_span_2=doc.body.find_all( "span", "stockrecord-price-old")
price_list_old=[]
for price in prices_span_2:
  stripped_price=price.string.strip()
  price_list_old.append(stripped_price)


#to create the price list for current prices
prices_span_1=doc.body.find_all( "span", "stockrecord-price-current")
price_list_current=[]
for price in prices_span_1:
  stripped_price=price.string.strip()
  price_list_current.append(stripped_price)


