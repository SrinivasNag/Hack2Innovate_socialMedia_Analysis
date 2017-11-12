import json
import pandas
import matplotlib as plt
from pprint import pprint
from textblob import TextBlob
from datetime import datetime
import csv
import matplotlib.pyplot as pyplt



tweeter_Data = 'C:/Users/SrInaG/Documents/Python Scripts/twitter_data'

tweets_data = []

tweets_file = open(tweeter_Data,'r')

for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

#tweets = pandas.DataFrame()

def get_sentiment_polarity(str):
	blob = TextBlob(str)
	return blob.sentiment.polarity

def get_time(str):
	ts = datetime.strptime(str,'%a %b %d %H:%M:%S +0000 %Y')
	return ts.strftime('%Y%m%d%H%M%S')

for d in range(10):
	print("Text: ", tweets_data[d]["text"], "Sentiment Value: ",get_sentiment_polarity(tweets_data[d]["text"]), "Time:", get_time(tweets_data[d]["created_at"]), 
		"location: ", tweets_data[d]["place"])


def get_sentiment_string(value):

	if value < 0 and value > -4:
		return 'NEGITIVE'
	elif value==0 or value <-4 or value > 4:
		return 'NEUTRAL'
	else:
		return 'POSITIVE'

print("Tweets_Data: ", type(tweets_data),"\n\n")

pyplt.plot_date(plt.dates.date2num(get_time(tweets_data["created_at"])),get_sentiment_string(get_sentiment_polarity(tweets_data["text"])))
pyplt.pyplot.show()
#for d in tweets_data:
#	with open("C:/Users/SrInaG/Documents/Python Scripts/output.csv",'a+') as file:
#		file.write(str(d["text"]))
#		file.write(",")
#		file.write(get_sentiment_string(get_sentiment_polarity(d["text"])))
#		file.write(",")
#		file.write(get_time(d["created_at"]))
#		file.write("\n")
#pprint(tweet.keys())

#for key, value in tweets_data:
#	pprint(key)

#for t in tweets_data:
#	pprint(t["text"])
#pprint(tweets_data[0]['timestamp_ms'])


#tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
#tweets['sentiment_polarity'] = map(lambda tweet: get_sentiment_polarity(tweet['text']), tweets_data)

#print(tweets)

#for t in tweets:
#	pprint(t)
#	print("\t")


#tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
#tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

#tweets_by_lang = tweets['lang'].value_counts()

#fig, ax = plt.subplots()
#ax.tick_params(axis='x', labelsize=15)
#ax.tick_params(axis='y', labelsize=10)
#ax.set_xlabel('Languages', fontsize=15)
#ax.set_ylabel('Number of tweets' , fontsize=15)
#ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
#tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')