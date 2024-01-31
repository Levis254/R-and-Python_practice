import requests
from bs4 import BeautifulSoup
import pandas as pd
#set the range
years=list(range(1991,2000))
url_start="https://www.basketball-reference.com/awards/awards_{}.html"
for year in years:
    url=url_start.format(year)
    data=requests.get(url).text

    with open("mvp/{}.html".format(year), "w+", encoding='utf-8') as f:
      f.write(data)
    
dfs=[]
for year in years:
  with open ("mvp/{}.html".format(year)) as f:
    page=f.read()

  soup=BeautifulSoup(page, "html.parser")
  soup.find('tr', class_="over_header").decompose()
  mvp_table=soup.find(id="mvp")
  mvp=pd.read_html(str(mvp_table))[0]
  mvp["year"]=year
  dfs.append(mvp)

#combining the dfs in the list into 1

mvps=pd.concat(dfs)


