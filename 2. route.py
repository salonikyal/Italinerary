#creating route and charts
from math import sin, cos, sqrt, atan2, radians
def distance(lat1, lon1, lat2, lon2):
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c
def closest(data, v):
    if len(data)!=0:
        return min(data, key=lambda p: distance(v['lat'],v['lon'],p['lat'],p['lon']))
o = {'name': 'Torre Pendente ', 'lat': 43.72301, 'lon': 10.39663}
v = closest(latlonglist, o)
i=1
tempList= latlonglist
while len(tempList)!=0:
    tempList = [x for x in tempList if not x == v]
    print(i,".",v['name'])
    v = closest(tempList, o) 
    i = i+1