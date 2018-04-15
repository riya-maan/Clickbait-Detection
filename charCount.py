# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:28:16 2018

@author: rmaan
"""

import re

def charCount(tweets):
    '''
    Count occurences of @, #, '.' and if tweet starts with a number
    '''
    #character occurences
    atTheRate = []
    hashTag = []
    dot = []
    numStart = []
    
    #number occurences in tweets
    for t in tweets:
        numAtTheRate = 0
        numHashTag = 0
        numDot = 0
        m=re.match('^1|^2|^3|^4|^5|^6|^7|^8|^9|^0',t)
        if m:
            numStart.append(1)
        else:
            numStart.append(0)
        
        oneGramC = []
        oneGramC.extend([t[i:i+1] for i in range(len(t)-2)])
        
        for char in oneGramC:
            if (char == '@'):
                numAtTheRate = numAtTheRate + 1
            if (char == '#'):
                numHashTag = numHashTag + 1
            if (char == '.'):
                numDot = numDot + 1
        
        atTheRate.append(numAtTheRate)
        hashTag.append(numHashTag)
        dot.append(numDot)
        
    return (atTheRate, hashTag, dot, numStart)
            