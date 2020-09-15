import chardet
import csv
import pandas as pd
with open("spmooddata.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
result
#{'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
df= pd.read_csv(r"spmooddata.csv", encoding= "Windows-1252")
songidcol= pd.DataFrame(df, columns= ["Song ID"])
n= 50
songidsub= [ songidcol[i:i+n] for i in range(0, len(songidcol), n) ]
