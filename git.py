import json
import requests
import csv

r = requests.get('https://api.github.com')
csvFile = open('./export/github.csv','w')
#csvwriter = csv.writer(csvFile)
myJson = r.json()
#print(myJson)
#w = csv.DictWriter(csvFile,myJson)
#w.writerow(myJson)

#csvFile.close()
#row = []
for url in myJson:
    w = csv.DictWriter(csvFile,myJson)
    w.writerow(myJson)
    #print(url,myJson[url])
    ## row.append(myJson[url])
    #csvwriter.writerow(row)

csvFile.close()

"""
import csv
f = open('dict.csv','wb')
w = csv.DictWriter(f,mydict.keys())
w.writerow(mydict)
f.close()
"""