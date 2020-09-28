import time
import tweepy
import csv
import sys
import time
import datetime
import json
import sys  
import oauth2 as oauth


consumer_key="YIB3EqaobBQJ1qPoDK9hGQyz3"
consumer_secret="IbU4gzAiQLYnLAM9ALHGC5lIAhPNDqtk0ilMdZIw8xO8u33eNp"
access_key="1448464110-ZXIx1hoQTEM4pAX3awESEYR9dewGoxKQikGTSYy"
access_secret="g473pYP1txNcGkKJTpYTKhFYzn6oTArS5wh5fTd2XstQI"

def get_rt_ts(client,tid):
	endpoint2="https://api.twitter.com/1.1/statuses/retweets/%s.json"%(tid)
	response2, data2 = client.request(endpoint2)
	# print("data2::",data2)
	return data2
consumer = oauth.Consumer(key = consumer_key, secret = consumer_secret)
access_token = oauth.Token(key = access_key, secret = access_secret)
client = oauth.Client(consumer, access_token)



list_tweets=[]
with open("viral_tweets_ids.txt",'r',encoding='utf-8') as file:
		for line in file:
			file=""
			line=line.rstrip()
			id_=line
			list_tweets.append(id_)

print("len of tweets",len(list_tweets))



count=0
dic_={}
for i in list_tweets :
	count=count+1
	time.sleep(30)
	print("count :",count)	
	try:
		if (count==20):
			print("Done")
			time.sleep(60)
		data=json.loads(get_rt_ts(client,i))
		dic_[i]=data
		print("len of dic:",len(dic_))
		with open("dict_retweets.json", "w+") as f4:
			f4.write(json.dumps(dic_))

	except Exception as e:
		print("exception",e)

