
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "297464452-FrrKD8s9FmhqMrQ5DA1p8LszL9utvzQEVemLgfL8"
access_token_secret = "22t8EQDkhUFtR6ndzcJavbxLnznMRTiDVFnumcx3iW4HP"
consumer_key = "aV8xnkVxQ3I2vHIhYjPGN0qLh"
consumer_secret = "0VchJi61lUGpP4S9LJiiVWGURLzf5OsWYEkJMMyPruvJSToor7"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
