# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:45:54 2018

@author: rmaan
"""

def listOccurences(tweets):
    '''
    to count number of abreviations and occurences of words from word list
    '''
    ## to count occurences of abbreviations
    abbrList = [line.rstrip('\n') for line in open(r'Word lists\abb_list.txt')]
    numAbbr = []
    
    ## to count occurences of words from word-lists
    genInq = [line.rstrip('\n') for line in open(r'Word lists\General Inquirer.txt')]
    terrierStopwords = [line.rstrip('\n') for line in open(r'Word lists\Terrier Stopwords List.txt')]
    daleChall = [line.rstrip('\n') for line in open(r'Word lists\DaleChall.txt')]
    downworthy = [line.rstrip('\n') for line in open(r'Word lists\Downworthy.txt')]
    
    numGenInq = []
    numTerrier = []
    numDaleChall = []
    numDownworthy = []
    
    for t in tweets:
        countAbb = 0
        countGen = 0
        countTerrier = 0
        countDale = 0
        countDownworthy = 0
        for word in t.split():
            if word in abbrList:
                countAbb = countAbb + 1
            if word in genInq:
                countGen = countGen + 1
            if word in terrierStopwords:
                countTerrier = countTerrier + 1
            if word in daleChall:
                countDale = countDale + 1
        numAbbr.append(countAbb)
        numGenInq.append(countGen)
        numTerrier.append(countTerrier)
        numDaleChall.append(countDale)
        
        # check if common clickbait phrases from Downworthy are present in tweet
        for word in downworthy:
            if word in t:
                countDownworthy = countDownworthy + 1
        numDownworthy.append(countDownworthy)
        
    return (numAbbr, numGenInq, numTerrier, numDaleChall, numDownworthy)
