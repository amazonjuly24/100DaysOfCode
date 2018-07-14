from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains yours credentials to access Twitter API 
consumer_key = "2D6MaFJEkC3pFetuCF0m8o9OZ"
consumer_secret = "Edv0q3ysy2OhUxJdD2uQYhRfn1EvkwvOqgb5w3Hg2YTffAWeVw"
access_token = "963122883940663296-GuDAdIqxGGlRwJkYQgtXPc5ZiQUNwKp"
access_token_secret = "38Taex5g6UFQnhp1n5AZi7s9AOlaJBN4Y1EjOjMq6jmnh"
 

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter tweets from the words.
    stream.filter(languages=["en"],track=['key1', 'key2'])
