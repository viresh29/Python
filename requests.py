import requests
#from requests.auth import HTTPDigestAuth
import json
import csv
from shutil import copyfile
import datetime
#import ConfigParser
import os, sys

from pprint import pprint

def weather(url,city,appid):
    reponse = requests.get(url + city, + '&'+ appid)
    weather = reponse.json()
    pprint(weather)
    print("The weather for", weather['name'])
    print(weather['main']['temp'])
    print(weather['weather'][0]['description'])


if __name__ == '__main__':
    weather('api.openweathermap.org/data/2.5/weather?q=','New York','APPID=0c008576ee1b2087b0240bc8c2e46f85')


