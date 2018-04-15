# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:25:21 2018

@author: rmaan
"""

import collections

def charGram(tweets):
    '''
    To return character 1, 2 and 3-grams with frequency > 2
    '''
    # character ngrams of tweet texts
    oneGramC = []
    twoGramC = []
    threeGramC = []
    for t in tweets:
        oneGramC.extend([t[i:i+1] for i in range(len(t)-2)])
        twoGramC.extend([t[i:i+2] for i in range(len(t)-3)])
        threeGramC.extend([t[i:i+3] for i in range(len(t)-4)])
        
    # count number of occurences of each character n-Gram
    f1 = dict(collections.Counter(oneGramC))
    f2 = dict(collections.Counter(twoGramC))
    f3 = dict(collections.Counter(threeGramC))
    
    oneGramC[:] = []
    twoGramC[:] = []
    threeGramC[:] = []
    for key, value in f1.items():
        if value>2:
            oneGramC.append(''.join(key))
    for key, value in f2.items():
        if value>2:
            twoGramC.append(''.join(key))
    for key, value in f3.items():
        if value>2:
            threeGramC.append(''.join(key))
            
    return (oneGramC, twoGramC, threeGramC)