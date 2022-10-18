from analizer import Analizer
from nltk.corpus import twitter_samples
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd


df = pd.DataFrame(columns=['user', 'tweet', 'sentiment', 'polarity'])


# # Setting the X and Y labels




text = twitter_samples.strings('tweets.20150430-223406.json')

x = np.array(["Postitive", "Negative", "Neutral"])
y = np.array([3, 8, 1, 10])

a = Analizer()
c = 0
for i in text[:100]:
    result = a.get_tweet_sentiment(i)
    df.loc[c] = ['name' + str(i), i, result[0], result[1]]
    c += 1


