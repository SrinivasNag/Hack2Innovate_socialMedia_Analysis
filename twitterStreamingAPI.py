import tweepy

consumer_key = "2mM1ISxurDZiulWBJdqa9WDcO"
consumer_secret = "YtGkV6HuPukSI8OZHsHXLaOQzRPfvm4uwuRZYdsh5pRru79f9e"
access_token = "334499616-T6vgrPbGZEc8yWPF3PZlQ9qNWg3cqbHWRwMulZxJ"
access_secret = "yrKNHO2auoi3KtNBnUTGBGwQnYgX7rkBahOXpmg1s9s7u"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

public_tweet = api.home_timeline()

#for tweet in public_tweet:
#	print (tweet.text)

class MyStreamListener(tweepy.StreamListener):
	"""This is a basic listener that prints recieved tweets to stdout"""
	
	def on_data(self, data):
		#print (data)
		print(data)
		with open ("C:/Users/SrInaG/Documents/Python Scripts/twitter_nike_data","a+") as loadfile:
			loadfile.write(data)
		return True

	def on_status(self, status):
		print (status)

	def on_error(self, status):
		print(status)

if __name__ == '__main__':
	
	l = MyStreamListener()

	myStream = tweepy.Stream(api.auth,l)

	myStream.filter(track=["#Nike OR #NIKE OR nike OR Nike OR NIKE"], async=True,languages=["en"])		

	#for tweet in myStream:
	#	print (tweet.text)