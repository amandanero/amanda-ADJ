import json 
import requests

url = 'http://data.cityofnewyork.us/resource/7x9x-zpz6.json'
response = requests.get(url).content


# urllib2.urlopen(url).read()


data = json.loads(response)

print data[0]
# print processed_data