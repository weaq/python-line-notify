#!/usr/local/bin/python3
import requests
def lineNotifyImg(msg, imgPath) :
  url = 'https://notify-api.line.me/api/notify'
  token = ''
  img = {'imageFile': open(imgPath,'rb')}
  data = {'message': msg}
  headers = {'Authorization':'Bearer ' + token}
  session = requests.Session()
  session_post = session.post(url, headers=headers, files=img, data =data)
  print(session_post.text)

msg = 'Test send image from local'
imgPath = 'img/test.png'
lineNotifyImg(msg, imgPath)
