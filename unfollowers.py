import tweepy
import time
import sys
import os
from keys import keys

SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)

os.system('clear')
start = time.time()
green = '\033[01;32m'
reset = '\033[1;0m'

def counter_unfollowers():
    k=0
    for f in friends:
        if f not in followers:
            k+=1
    return k

def unfollow_not_followback():
    i=0
    print("Do u want unfollow {0} users?\n".format(counter_unfollowers()))
    if input(reset+"Y/N?: ") == 'y' or 'Y':
        os.system('clear')
        for f in friends:
            if f not in followers:
                #print ("Unfollow {0}?".format(api.get_user(f).screen_name))
                api.destroy_friendship(f)
                i+=1
                elapsed = (time.time() - start)
                sys.stderr.write(reset+ " Unfollow {0} / {1} users in {2:.1f} seconds \r".format(i,counter_unfollowers(),elapsed))

if __name__ == "__main__":
    while(1):
        try:
            if counter_unfollowers() == 0:
                print(reset + " You have 0 unfollowers\r")
                break
            else:
                unfollow_not_followback()
        except:
            print ("Possibly Rate limited? sleeping 60 seconds")
            time.sleep(60)
