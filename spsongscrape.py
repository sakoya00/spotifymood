from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
#import urllib2
import re
from time import sleep
from datetime import data, timedelta
from random import randint

#map site

url = "https://spotifycharts.com/regional/us/daily/"
startdate= date(2020, 1, 1)
enddate= date(2020, 9, 1)

delta= end_date-start_date
dates=[]
url_list=[]

for i in range(delta.days+1):
	day = start_date+timedelta(days=i)
	day_string= day.strftime("%Y-%m-%d")
	dates.append(day_string)

def add_url():
	for date in dates:
		c_string = url+date
		url_list.append(c_string)

for u in url_list:
read_pg= urllib.request.urlopen(u).read()
soup=BeautifulSoup(read_pg, "html.parser")
html = response.read().decode('utf-8')

#scrape songs
songs= soup.find("table", {"title":"chart-table"})

def songs(x):
pg = x
artist_list=[]
title_list=[]
id_list= []
url_date=[]
for row in songs.findAll("tr"):

artist= tr.find("td", {"class": "chart-table-track"}).find("span").text
artist= artist.replace("by ","").strip()
artist_list.append(artist)

title= tr.find("td", {"class": "chart-table-track"}).find("strong").text
title_list.append(title)

id= tr.find("td", {"class": "chart-table-image"}).find("a").get("href")
id=url.split("track/")[1]
id_list.append(id)
##song_date= re.search("<script>(.*)</script>", html")



final = []
final.append([title_list, artist_list, id_list, #date])
final_df = pd.DataFrame()
