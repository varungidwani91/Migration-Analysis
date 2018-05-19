# Import package
import tweepy
import json
from tweepy import OAuthHandler

import twitter_credentials


# this code is for streaming tweets

# Pass OAuth details to tweepy's OAuth handler
auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 10000:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:
stream.filter(track=['#proimmigration','#preimmigrationReform','#proOpenBorders','#NoWallNoBan','#ImmigrantsAreWelcome',
                     '#AntiIllegalImmigration','#nationOfImmigrants','#RefugeesWelcome',
                     '#ImmigrantsWelcome','#fightIgnoranceNotImmigrants','#noHumansIllegal',
                     '#noBanNoWallNoRaids'])