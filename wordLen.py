# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:04:04 2018

@author: rmaan
"""
from nltk import ngrams

def wordLen(tweets):
    '''
    To calculate average word length, length of longest word and total character length
    '''
    avg = []
    longest = []
    charLen = []
    for t in tweets:
        oneGramW = []
        nGram1 = ngrams(t.split(),1);
        for gr in nGram1:
            oneGramW.append(gr)
        
        sortedWords = sorted(oneGramW, key=len)
        wordLengthSum = 0
        wordLengthMax = 0
        for tuple in sortedWords:
            wordLength = len(tuple[0])
            wordLengthSum+= wordLength
            if wordLengthMax < wordLength:
                wordLengthMax = wordLength
         
        avg.append(wordLengthSum/len(oneGramW))
        longest.append(wordLengthMax)
        charLen.append(len(t))
        
    return (avg, longest, charLen)
        