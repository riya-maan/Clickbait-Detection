# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:29:33 2018

@author: rmaan
"""
from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf(oneGram, twoGram, threeGram, tweets):
    '''
    To calculate tf-idf values correponding to n-grams
    '''
    # concatenate all word lists to calculate tf-idf features
    nGrams = []
    nGrams.extend(oneGram)
    nGrams.extend(twoGram)
    nGrams.extend(threeGram)
    
    # calculate word Gram's Tf-idf
    tfidf = TfidfVectorizer(vocabulary = nGrams, stop_words = 'english', ngram_range=(1,3))
    tfs = tfidf.fit_transform(tweets)
    feature_names = tfidf.get_feature_names()
        
    import pandas as pd
    nGramTfidf = pd.DataFrame(tfs.T.todense(), index=feature_names, columns=tweets)
    
    return nGramTfidf