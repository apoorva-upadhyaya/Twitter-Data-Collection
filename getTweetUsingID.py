import pandas as pd 
import tweepy
import json

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)



df=pd.read_csv("ids.csv",delimiter=",")
list_ids=list(df["tweetId"])
#print(len(list_ids))
print("Starting...................................Wait Please!!!!!!!!!!!!!!!!!!!!!!!")
#count=0
for single_id in list_ids:
	#print(type(single_id))
	#count=count+1
	#print(count)
	try:		
		tweet=api.get_status(single_id, tweet_mode='extended')
				
		#<convert <class 'tweepy.models.Status'> to string representation of dict>
		json_str = json.dumps(tweet._json)
		#<convert string representation of dict to dict>
		tweet=json.loads(json_str)
		with open("file.json","a") as f:
			json.dump(tweet,f)
			f.write("\n")
		
	except:
		continue	
print("Done.........................")
