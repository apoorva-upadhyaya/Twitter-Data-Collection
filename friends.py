import tweepy
import json
import os
import ast
import pandas as pd
import csv
import time


pt=[]
with open("user0.txt",'r',encoding='utf-8') as file:
		for line in file:
			file=""
			line=line.rstrip()
			id_=line
			pt.append(id_)
print("len of users",len(pt))


CONSUMER_KEY=""
CONSUMER_SECRET=""
OAUTH_TOKEN=""
OAUTH_TOKEN_SECRET=""

# dic={}
def get_followers(u_id):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	api = tweepy.API(auth,wait_on_rate_limit_notify=True)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	ids = []
	count=0
	
			
	try:
		# print(u_id)
			
		for page in tweepy.Cursor(api.friends_ids, user_id=u_id).pages():
			ids.extend(page)
			time.sleep(60)
			
		# filepath="2/"+u_id+".txt"
		# with open(filepath,"w") as f:
		# 	for i in range(len(ids))	:
		# 		f.write(str(ids[i]))
		# 		f.write("\n")
		# 		f.flush()

		print("no of followers:",len(ids))

		return ids


	except Exception as e: 
		print(e)
		# time.sleep(60)
		li=[]
		return li

	

if __name__ == '__main__':

	dic_={}
	count=0
	for i in pt:
		list_=get_followers(str(i))
		print("count",count)
		count=count+1
		dic_[i]=list_
		print("len of dic",len(dic_))
		with open("dict_freinds.json", "w+") as f4:
		 	f4.write(json.dumps(dic_))


# import json
# file_ob=open("dict_coords_gbv_100.json",'r')
# dict_=json.load(file_ob)
