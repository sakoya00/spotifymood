from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from time import sleep
from datetime import date, timedelta
from random import randint

#map site

url = "https://spotifycharts.com/regional/us/daily/"
start_date= date(2020, 1, 1)
end_date= date(2020, 1, 2)

delta= end_date-start_date
dates=[]
url_list=[]
artist_list=[]
title_list=[]
id_list= []
url_date_ls=[]
final = []

for i in range(delta.days+1):
	day = start_date+timedelta(days=i)
	day_string= day.strftime("%Y-%m-%d")
	dates.append(day_string)

def add_url():
	for date in dates:
		c_string = url+date
		url_list.append(c_string)

add_url()

def song_scrape(x):
    pg = x
    for tr in songs.find("tbody").findAll("tr"):
        artist= tr.find("td", {"class": "chart-table-track"}).find("span").text
        artist= artist.replace("by ","").strip()
        artist_list.append(artist)

        title= tr.find("td", {"class": "chart-table-track"}).find("strong").text
        title_list.append(title)

        songid= tr.find("td", {"class": "chart-table-image"}).find("a").get("href")
        songid= songid.split("track/")[1]
        id_list.append(songid)
        
        url_date= x.split("daily/")[1]
        url_date_ls.append(url_date)

for u in url_list:
    read_pg= requests.get(u)
    sleep(2)
    soup= BeautifulSoup(read_pg.text, "html.parser")
    songs= soup.find("table", {"class":"chart-table"})
    song_scrape(u)
    final.append([title_list, artist_list, id_list, url_date_ls])
    
final_df = pd.DataFrame(final, columns= ["Title", "Artist", "Song ID", "Chart Date"])
with open('spscrape3.csv', 'w') as f:
        final_df.to_csv(f, header=False, index=False)
