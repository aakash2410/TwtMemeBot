import tweepy
import random
def meme(text):
    memed_text=[]
    for i in text:
        r = random.randint(0,1)
        if r == 1:
            memed_text.append(i.upper())
        else:
            memed_text.append(i.lower())
    return ''.join(memed_text)


cons = open('C:/Users/aakas/Documents/cons api key.txt', 'r')
x = cons.read()
cons_secret = open('C:/Users/aakas/Documents/cons secret api key.txt', 'r')
X = cons_secret.read()
acs_token = open('C:/Users/aakas/Documents/access token.txt', 'r')
y = acs_token.read()
acs_token_scrt = open('C:/Users/aakas/Documents/access token secret.txt', 'r')
Y = acs_token_scrt.read()


def memify_tweet(new_id,count):
    consumer_key = x
    consumer_secret = X  
    access_token = y
    access_token_secret = Y
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    df=[]
    person_tweets = api.user_timeline(id = new_id ,count=count)
    for tweet in person_tweets:
        if "https://t.co" in tweet.text:
            pass
        elif tweet.text[0:3] != "RT ":
            api.update_status(f'@{new_id} '+ (meme(tweet.text)),tweet.id)
            df.append(tweet)
    return None
    


        

