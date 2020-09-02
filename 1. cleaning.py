import requests
import json
import re
import codecs
import pprint

#Fetching data
URL = "https://en.wikivoyage.org/w/api.php?action=query&format=json&prop=revisions&rvprop=content&rvsection=11&titles=Pisa"
r = requests.get(url = URL) 

#Fetching data related to our query
data = r.json()
querydata=data["query"]["pages"]

#converting to string for parsing 
detaileddata="".join(str(items) for items in querydata.values())

#parsing to get the attraction list
datalist=re.findall(r"name=(.+?)\|",detaileddata)


#cleaning
finallist=[]
for i in datalist:
    finallist.append(codecs.decode(i, 'unicode_escape'))

#fetching latitude longitude
j=0
latlonglist=[]
for i in finallist:
    idict={}
    placename=i.split("\'")
    regexp=placename[-1]+"(.+?)directions"
    try:
        latlongdata=re.search(regexp,detaileddata).group(1)
        latdata=re.search(r"lat=(.+?)\|",latlongdata).group(1)
        longdata=re.search(r"long=(.+?)\|",latlongdata).group(1)
        idict["name"]=i
        idict["lat"]=float(latdata)
        idict["lon"]=float(longdata)
        latlonglist.append(idict)
    except:
            pass
pp = pprint.PrettyPrinter(depth=3)
pp.pprint(“List:”,latlonglist)




