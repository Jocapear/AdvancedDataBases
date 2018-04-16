import tweepy
from tweepy import OAuthHandler
import json
from urllib.parse import quote_plus

def writeJSON(object, name):
	f = open(name + ".json", "w")
	f.write(json.dumps(object))
	f.close()

consumer_key = 'BRlhIseyW8OkG3bQMDmFryCgd'
consumer_secret = 'MvjVeznnPLnVVM6MrkEnw2e3EYf7aCveFHaO11OmCnN1HWPpc6'
access_token = '1155702312-zgNBhNyNNWQrETFe0GlSDL6Jn9zCc3StaucYW5u'
access_secret = 'SHWUkQod5CNC7ifrHJAPN1jTpj4j57hzyQoX5GklkDO04'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True)

#query_all = ["@lopezobrador_", "AMLO"]
#query = quote_plus("({0}) ({1})".format(" OR ".join(query_all)))
subjects = ["@lopezobrador_"]
subjectsids = [82119937]

amlo = {}
#friends = []

try:
	print("RUNNING...")
	#for friend in tweepy.Cursor(api.friends).items():
	#	friends.append(json.dumps(friend._json))

	searchTweets = api.user_timeline(subjectsids[0])
	print(searchTweets)
	searchInfo = api.get_user(subjectsids[0])
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print(searchInfo)
	tweets = []
	for tweet in searchTweets:
		tweets.append(json.dumps(tweet._json))
	amlo["tweets"] = tweets;
	print("TWEETS GOTTEN")
	amlo["info"] = json.dumps(searchInfo._json)
	print("INFO GOTTEN")

except tweepy.RateLimitError as e:
	print("***************** Error RateLimitError **********************")
except tweepy.TweepError as e:
    print(e)

#writeJSON(friends, "friends")
#print("----------------------- FRIENDS WRITTEN -----------------------------")
writeJSON(amlo, subjects[0])
print("----------------------- AMLO WRITTEN -----------------------------")

print("DONE")