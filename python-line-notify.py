#!/usr/local/bin/python3
import requests
url = 'https://notify-api.line.me/api/notify'
token = ''
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg = 'Test Notify'
r = requests.post(url, headers=headers, data = {'message':msg})
print (r.text)
