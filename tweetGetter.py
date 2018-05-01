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
#ID's de Meade, AMLO, Anaya y Margarita
subjects = [237372254, 82119937, 151968088, 97017966]

for candidato in subjects:
	accountGetter(candidato)