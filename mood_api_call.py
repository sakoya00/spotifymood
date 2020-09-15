import chardet
import csv
import requests
import json
import pandas as pd
with open("spmooddata.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
result
#{'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
df= pd.read_csv(r"spmooddata.csv", encoding= "Windows-1252", usecols="Song ID")
songidcol= df.to_json()
songidcol2= json.dumps(songidcol)
songidparsed= songidcol2["Song ID"]

def get_concat_query(k=0, concatls=[]):
    concatpre=[]
    for i in range (0, len(songidparsed)):
        while i<10+10*k:
            songidval= songidparsed.get(str(i))
            concatpre.append(songidval)
            joined= ",".join(concatpre))
        concatls.append(joined)
        k=k+1
        get_concat_query(k, concatls)
            
#songidcol= pd.DataFrame(df, columns= ["Song ID"])
#n= 50
#songidsub= [ songidcol[i:i+n] for i in range(0, len(songidcol), n) ]
