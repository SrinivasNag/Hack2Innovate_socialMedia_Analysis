import requests 
from requests_oauthlib import OAuth1 
import json 
from urllib.parse import urlparse 
import pprint 

params = { 
'app_key':'2mM1ISxurDZiulWBJdqa9WDcO', 
 'app_secret':'YtGkV6HuPukSI8OZHsHXLaOQzRPfvm4uwuRZYdsh5pRru79f9e', 
 'oauth_token':'334499616-T6vgrPbGZEc8yWPF3PZlQ9qNWg3cqbHWRwMulZxJ', 
 'oauth_token_secret':'yrKNHO2auoi3KtNBnUTGBGwQnYgX7rkBahOXpmg1s9s7u' 
} 

auth = OAuth1( 
   params['app_key'], 
   params['app_secret'], 
   params['oauth_token'], 
   params['oauth_token_secret'] 
) 

#q = urlparse('Nike') 
url_rest = "https://api.twitter.com/1.1/search/tweets.json" 

payload = {
        'q': 'Nike OR #Nike OR #nike', # May be @user_search or #hash_search also
        'lang' : 'en',  # Based on ISO 639-1 two-letter code
        'result_type': 'mixed',
        'count': '100',  # Number of tweets to return per page, up to a max of 100
        'until': '20161231'
    }

results = requests.get(url_rest, auth=auth, params=payload) 

pprint(results.json())
#for tweet in results.json():
	
	#pprint(tweet["text"])
	#pass

for tweet in results.json(): 
	with open ("C:/Users/SrInaG/Documents/Python Scripts/twitter_nike_data","a+") as loadfile:
			loadfile.write(tweet)


