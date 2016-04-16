#python 2.7.3
import oauth2 as oauth
import urlparse
import time

## If you're actually processing requests, you'll want this
# import simplejson 


### GET A REQUEST TOKEN ###

consumer = oauth.Consumer(key="REBGZLTH5RAMAGDVSZM53SDAK1S3LDWKQLFUXLBG5IY3N0ZD", secret="YZN01KFK33IMXXG2A4ZURKIWRIB5CR4EF1MBOAYO3JRJYXBZ")

request_token_url = 'https://api.foursquare.com/v2/oauth/request_token'

client = oauth.Client(consumer)
resp, content = client.request(request_token_url, "GET")
    
request_token = dict(urlparse.parse_qsl(content))
print resp
print content
print request_token
#token = oauth.Token(request_token['REBGZLTH5RAMAGDVSZM53SDAK1S3LDWKQLFUXLBG5IY3N0ZD'], request_token['YZN01KFK33IMXXG2A4ZURKIWRIB5CR4EF1MBOAYO3JRJYXBZ'])

