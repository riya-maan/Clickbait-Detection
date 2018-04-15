# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:19:17 2018

@author: rmaan
==================================
nltk.download()  -----> in console
select corpus cmudict and download!!
select model punkt and download!!
==================================
"""

from nltk.corpus import cmudict
from nltk.tokenize import sent_tokenize
import numpy as np


def flesh_kincaid(tweets):
    '''
    Calculate Felsh-Kincaid readability score
    '''
    def get_pron(word):
        try:
            return cmudict.dict()[word][0]
        except KeyError:
            return [['1']]
    result = []
    for tweet in tweets:
        _processed = tweet
        word_count = len(_processed)
        sent_count = len(sent_tokenize(tweet))
        syllable_count = np.sum([len([s for s in get_pron(word)
                                      if (s[-1]).isdigit()])
                                 for word in _processed])
        try:
            result.append(0.39 *
                           (word_count / sent_count) + 11.8 *
                           (syllable_count / word_count) - 15.59)
        except ZeroDivisionError:
            result.append(-3.4)  # thats the minimal possible FK-Score
    FKScore = np.asarray(list(result))[:, np.newaxis]
    
    return FKScore
