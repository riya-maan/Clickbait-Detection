# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:20:40 2018

@author: rmaan
"""
from nltk import ngrams
import collections

def wordGram(tweets):
    '''
    To return word 1, 2 and 3-grams with frequency > 2
    '''
    # word ngrams of tweet texts
    oneGramW = []
    twoGramW = []
    threeGramW = []
    for i in tweets:
        nGram1 = ngrams(i.split(),1);
        nGram2 = ngrams(i.split(),2);
        nGram3 = ngrams(i.split(),3);
        for gr in nGram1:
            oneGramW.append(gr)
        for gr in nGram2:
            twoGramW.append(gr)
        for gr in nGram3:
            threeGramW.append(gr)
    
    # count number of occurences of each Word n-Gram
    f1 = dict(collections.Counter(oneGramW))
    f2 = dict(collections.Counter(twoGramW))
    f3 = dict(collections.Counter(threeGramW))
    
    oneGramW[:] = []
    twoGramW[:] = []
    threeGramW[:] = []
    for key, value in f1.items():
        if value>2:
            oneGramW.append(''.join(key))
    for key, value in f2.items():
        if value>2:
            twoGramW.append(''.join(key))
    for key, value in f3.items():
        if value>2:
            threeGramW.append(''.join(key))
            
    return (oneGramW, twoGramW, threeGramW)