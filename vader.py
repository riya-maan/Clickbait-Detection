# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 00:09:21 2018

@author: rmaan

==================================
nltk.download()  -----> in console
select model
vader_lexicon and 
download
==================================
"""
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk.tokenize import TweetTokenizer

global tknzr
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
def tokenize(text):
        return [token for token in tknzr.tokenize(text)]

def vader(tweets):
    '''
    Calculate Vader sentiment analysis score
    '''
    polarity_scores = []
    for tweet in tweets:
        _processed = tokenize(tweet)
        try:
            polarity_scores.append(SIA().polarity_scores(" ".join(_processed))["compound"])
        except Exception:
            polarity_scores.append(0)
            
    return polarity_scores
