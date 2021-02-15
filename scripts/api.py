import urllib.parse
import requests

main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
address = '07644'
url = main_api + urllib.parse.urlencode({'address': address})

print(url)

json_data = requests.get(url).json()
print(json_data)

"""
Address: 07644
http://maps.googleapis.com/maps/api.geocode/json?address=07644
API Status: OK
"""
