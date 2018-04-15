# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:11:34 2018

@author: rmaan
=======================================================================
download stopwords from spyder console ---   nltk.download('stopwords')
=======================================================================
"""
import string
from nltk.corpus import stopwords
from nltk import PorterStemmer
import numpy as np


from wordGrams import wordGram
from charGrams import charGram
from tf_idf_func import tf_idf
from wordLists import listOccurences
from wordLen import wordLen
from charCount import charCount
from vader import vader
from fk_score import flesh_kincaid


def featureExtraction(instances):
    # extract tweet text in "tweets"
    tweets = []
    for i in instances:
        tweets.append(str(i['postText']))
            
    # remove stopwords from tweet text
    cachedStopWords = stopwords.words("english")
    stopTweets = []
    for t in tweets:
        t = ' '.join([word for word in t.split() if word not in cachedStopWords])
        stopTweets.append(t)
     
    # Potter stemming    
    stemTweets = []
    for t in stopTweets:
        t = ' '.join([PorterStemmer().stem(word) for word in t.split()])
        stemTweets.append(t)
        
    # remove punctuation marks from tweet text
    exclude = set(string.punctuation)
    puncTweets = []
    for t in stemTweets:
        t = ' '.join(ch for ch in t if ch not in exclude)
        puncTweets.append(t)
        
    del stemTweets
    
    # Word n-grams with frequency > 2
    [oneGramW, twoGramW, threeGramW] = wordGram(puncTweets)
    
    # Character n-gram with frequency > 2
    [oneGramC, twoGramC, threeGramC] = charGram(stopTweets)
    
    # word n-Gram tf-idf features
    wordGramTfidf = tf_idf(oneGramW, twoGramW, threeGramW, puncTweets)
    
    del oneGramW, twoGramW, threeGramW, puncTweets
    
    # character n-Gram tf-idf features
    charGramTfidf = tf_idf(oneGramC, twoGramC, threeGramC, stopTweets)
    
    del oneGramC, twoGramC, threeGramC, stopTweets
    
    # media and time-stamp presence
    media = []
    timeStamp = []
    for i in instances:
        if(i['postTimestamp'] == ''):
            timeStamp.append(0)
        else: 
            timeStamp.append(1)
        if(i['postMedia']==[]):
            media.append(0)
        else:
            media.append(1)
            
    features = []
    features  = np.concatenate(([media], [timeStamp]), axis = 0)
    del media, timeStamp
            
    # to count number of abreviations and occurences of words from word list
    [numAbbr, numGenInq, numTerrier, numDaleChall, numDownworthy] = listOccurences(tweets)
    
    features  = np.concatenate((features, [numAbbr]), axis = 0)
    features  = np.concatenate((features, [numGenInq]), axis = 0)
    features  = np.concatenate((features, [numTerrier]), axis = 0)
    features  = np.concatenate((features, [numDaleChall]), axis = 0)
    features  = np.concatenate((features, [numDownworthy]), axis = 0)
    
    del numAbbr, numGenInq, numTerrier, numDaleChall, numDownworthy

    
    # To calculate average word length, length of longest word and total character length
    [avg, longest, charLength] = wordLen(tweets)
    
    features  = np.concatenate((features, [avg]), axis = 0)
    features  = np.concatenate((features, [longest]), axis = 0)
    features  = np.concatenate((features, [charLength]), axis = 0)
    
    del avg, longest, charLength
    
    # Count occurence of characters and if tweet starts with number or not
    [atTheRate, hashTag, dot, numStart] = charCount(tweets)
    
    features  = np.concatenate((features, [atTheRate]), axis = 0)
    features  = np.concatenate((features, [hashTag]), axis = 0)
    features  = np.concatenate((features, [dot]), axis = 0)
    features  = np.concatenate((features, [numStart]), axis = 0)
    
    del atTheRate, hashTag, dot, numStart
    
    # Vader sentiment analysis
    vaderSentiment = vader(tweets)
    features  = np.concatenate((features, [vaderSentiment]), axis = 0)
    
    del vaderSentiment
    
    # Flesh-Kincaid score
    #fk = flesh_kincaid(tweets)
    #features  = np.concatenate((features, [fk]), axis = 0)
    
   # del fk
    
    features  = np.concatenate((features, wordGramTfidf.values), axis = 0)
    features  = np.concatenate((features, charGramTfidf.values), axis = 0)
    
    return features