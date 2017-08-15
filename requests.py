import requests
#from requests.auth import HTTPDigestAuth
import json
import csv
from shutil import copyfile
import datetime
#import ConfigParser
import os, sys

from pprint import pprint

def main():
    reponse = requests.get("http://api.openweathermap.org/data/2.5/weather?q=NewYork&appid=0c008576ee1b2087b0240bc8c2e46f85&unit=imperial")
    weather = reponse.json()
    pprint(weather)
    print(weather['main']['temp'])


if __name__ == '__main__':
    main()


