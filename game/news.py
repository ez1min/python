# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request


a
client_id ="v99GMgvQyYzWdCAiwrnm"     #"MY_ID"
client_secret = "UNxUyeRapn" #"MY_SECRET"
encText = urllib.parse.quote("속보")
url = "https://openapi.naver.com/v1/search/blog?query="+ encText + '&display=5&start=1&sort=sim'

 # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
ldata = data['items']
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    ldata = dat ['items
    
    for n in ldata:
        print(n['title'].replace('<b>','').replace('<b>',''))
        print(n['description'])
        print(n['originallink'])
else:
    print("Error Code:" + rescode)


   