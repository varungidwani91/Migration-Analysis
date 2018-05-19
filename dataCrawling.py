import tweepy
from tweepy import OAuthHandler
import csv

from venv.src import twitter_credentials

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('FavourTweetsWorld.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

"""def process_or_store(tweet):
    print(json.dumps(tweet))"""

#'immigrant OR refugee OR migration'

hashtag_list =  '#proimmigration OR #preimmigrationReform OR #proOpenBorders OR #NoWallNoBan OR #ImmigrantsAreWelcome OR #AntiIllegalImmigration OR #nationOfImmigrants OR #RefugeesWelcome OR #ImmigrantsWelcome OR #fightIgnoranceNotImmigrants OR #noHumansIllegal OR #noBanNoWallNoRaids'
for tweet in tweepy.Cursor(api.search,q=hashtag_list,lang="en",count=500, since="2018-03-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
   # process_or_store(tweet._json)

"""place:96683cc9126741d1  #ImmigrationNotWelocme OR #AntiImmigration OR #DayWithoutImmigrants OR #BuildTheWall OR #Illegalaliens OR #ImmigrationReform OR #crimmigrants OR #immigration OR #immigrants OR #migration OR #ImmigrationBan OR #TravelBan'"""

# OR immigrant ban OR immigration ban OR immigrant ban OR immigration ban OR travel ban OR immigration order