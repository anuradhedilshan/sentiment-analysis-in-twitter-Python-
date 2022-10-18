from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import re
import string


class Analizer:
    stop_words = stopwords.words('english')


    def remove_noise(self,tweet_tokens):
        tweet_tokens = word_tokenize(tweet_tokens)

        cleaned_tokens = ""

        for token, tag in pos_tag(tweet_tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'
                        '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
            token = re.sub("(@[A-Za-z0-9_]+)", "", token)

            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token) > 0 and token not in string.punctuation and token.lower() not in self.stop_words:
                cleaned_tokens += " "+token
        return cleaned_tokens


    def get_tweet_sentiment(self,tweet):

        analysis = TextBlob(self.remove_noise(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive' , analysis.sentiment.polarity
        elif analysis.sentiment.polarity == 0:
            return 'neutral' , analysis.sentiment.polarity
        else:
            return 'negative' , analysis.sentiment.polarity
