Python 3.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
import urlib2
import json

while True:
        ip = raw_input("Input IP: ")
        url = "http://ip-api.com/json"
        
        response = urlib2.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)

        print(" IP: " + values['query'])
        print(" City: " + values['city'])
        print(" ISP: " + values['isp'])
        print(" Country " + values['country'])
        print(" Region: " + values['region'])
        print(" Time Zone: " + values['timezone'])

        break
