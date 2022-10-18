
from twitter import Twitter
from driver import init
from analizer import Analizer
import pandas as pd


df = pd.DataFrame(columns=['user', 'tweet', 'sentiment', 'polarity'])


tw = Twitter(driver=init())
# tw.login()

# tw.fetch_tweet("https://twitter.com/WhatsApp/status/1554860158303539206")
tweets = tw.fetch_tweet(
    "https://twitter.com/kanchana_wij/status/1555524217696690176")


analizer = Analizer()

c = 0
for i in tweets:
    result = analizer.get_tweet_sentiment(i['tweet'])
    df.loc[c] = [i['user'], i['tweet'], result[0], result[1]]
    c += 1


print(df) 

# visulaizer

