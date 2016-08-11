import sys
import json
import calendar
import tweepy
import pymysql
import datetime

consumer_key = 'xxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
search_term = '#euref'


# This is the listener, resposible for receiving data

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first

        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users



        print('@%s: %s Time %s Place: %s' % (
        decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'), decoded['created_at'],
        decoded['place']))

        print('')

        tweettext = decoded['text']
        tweettime = datetime.datetime.now()
        tweetcoordinates = decoded['coordinates']
        tweetplace = decoded

   
        return True


def on_error(self, status):
    print(status)


if __name__ == '__main__':
    l = StdOutListener()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    print("Showing all new tweets for " + search_term)

    # There are different kinds of streams: public stream, user stream, multi-user streams

    # In this example follow #programming tag

    # For more details refer to https://dev.twitter.com/docs/streaming-apis

    stream = tweepy.Stream(auth, l)

    stream.filter(track=[search_term])


