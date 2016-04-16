import json
import urllib.request
import threading
def callReddit():
    print('Calling reddit')
    url = 'http://www.reddit.com/r/seattle/.json'
    req = urllib.request.urlopen(url)
    print(req)
    encoding = req.headers.get_content_charset()
    loaded = json.loads(req.read().decode(encoding))
    print("Loaded")
    print(loaded)
    listOfLinks = loaded['data']['children']
    for link in listOfLinks:
        print('title: '+link['data']['title']+ '  URL: '+ link['data']['url']) 
    
    t = threading.Timer(10.0, callReddit)
    t.start()

t = threading.Timer(10.0, callReddit)
t.start()
print("Hi")

