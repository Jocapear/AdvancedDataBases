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

def accountGetter(accountID): #Recibe el ID de una cuenta de twitter
	subject = "" #For storing the subject name -> later used on JSON file's name.

	account = {} #Target account dictionary with alst 20 tweets and account information.

	try:
		print("RUNNING ACCOUNT_GETTER...")
		#regresa los primeros 20 tweets
		searchTweets = api.user_timeline(accountID)
		#regresa Info
		searchInfo = api.get_user(accountID)

		tweets = []
		for tweet in searchTweets:
			tweets.append(json.dumps(tweet._json, sort_keys = True))

		account["tweets"] = tweets;
		print("TWEETS GOTTEN")

		account["info"] = json.dumps(searchInfo._json, sort_keys = True)
		print("INFO GOTTEN")

		subject = searchInfo._json["screen_name"] 
		print("Name gotten: " + subject)

	except tweepy.RateLimitError as e:
		print("****************** Error RateLimitError **********************")
	except tweepy.TweepError as e:
	    print(e)

	writeJSON(account, subject)
	print("ACCOUNT WRITTEN")

	print("DONE")
	return account

def accountGetterNoWritting(accountID): #Recibe el ID de una cuenta de twitter

	account = {} #Target account dictionary with alst 20 tweets and account information.

	try:
		print("RUNNING ACCOUNT_GETTER...")
		#regresa los primeros 20 tweets
		searchTweets = api.user_timeline(accountID)
		#regresa Info
		searchInfo = api.get_user(accountID)

		tweets = []
		for tweet in searchTweets:
			tweets.append(json.dumps(tweet._json, sort_keys = True))

		account["tweets"] = tweets;
		print("TWEETS GOTTEN")

		account["info"] = json.dumps(searchInfo._json, sort_keys = True)
		print("INFO GOTTEN")

	except tweepy.RateLimitError as e:
		print("****************** Error RateLimitError **********************")
	except tweepy.TweepError as e:
	    print(e)
	return account

def tweetGetter(tweetIDs):
	tweets = []
	query = api.statuses_lookup(tweetIDs)
	for tweet in query:
		tweets.append(json.dumps(tweet._json, sort_keys = True))

	writeJSON(tweets, "tweets_lists")
	print("TWEETS GOTTEN")
	return tweets

def getReplies(subject, tweetID):
	tweets = []
	query = subject
	search = api.search(query, count=1000)
	for tweet in search:
		if tweet.in_reply_to_status_id == tweetID:
			tweets.append(json.dumps(tweet._json, sort_keys = True))

	writeJSON(tweets, "replies_to_"+subject+"_"+str(tweetID))
	print("REPLIES GOTTEN")
	return tweets


def getMentions(subject):
	tweets = []
	query = subject
	search = api.search(query, rpp= 100, count=1000)
	for tweet in search:	
		tweets.append(json.dumps(tweet._json, sort_keys = True))

	writeJSON(tweets, "mentions_to_"+ str(subject))
	print("MENTIONS GOTTEN")
	return tweets


#ID's de Meade, AMLO, Anaya y Margarita
#subjects = [237372254, 82119937, 151968088, 97017966]

#for candidato in subjects:
#	accountGetter(candidato)

#Target https://twitter.com/yare_quinones/status/991392931389964288
#tweetsIDS = []
#tweetsIDS.append(991392931389964288)
#tweetGetter(tweetsIDS)

#Target 991392862490316801 AMLO
#getReplies("@lopezobrador_", 991392862490316801)
#Obtuvo el 991419266183368704 y el 991419120406138880
