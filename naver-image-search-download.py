import os
import sys
import urllib.request
import json
import requests

client_id = "client_id"
client_secret = "client_secret"

# image file directory
directory = "" 

# search word
search_word = "search_word"

encText = urllib.parse.quote(search_word)
url = "https://openapi.naver.com/v1/search/image?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    jsonStr = response_body.decode('utf-8')
    resultArr = json.loads(jsonStr)
    cnt = 0

    # Make directory
    if not os.path.exists(directory):
        os.makedirs(directory)

    for item in resultArr['items']:
        remote_url = item['link']
        print(str(cnt) + ' : ' + remote_url)
    
        # Define the local filename to save data
        local_file = directory + "/image_" + str(cnt) + ".jpg"

        # Download remote and save locally
        data = requests.get(remote_url)
        with open(local_file, 'wb')as file:
            file.write(data.content)

        # increment count
        cnt = cnt + 1
else:
    print("Error Code:" + rescode)