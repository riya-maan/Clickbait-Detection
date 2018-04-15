# -*- coding: utf-8 -*-
"""
Spyder Editor
====================================================
Change file location here and in wordLists.py

import nltk  -----> in console
nltk.download()  -----> in console
select model vader_lexicon and download!! (for Vader sentiment analysis)
select corpus cmudict and download!! (for FK-score)
select model punkt and download!! (for FK-score)

download stopwords from spyder console --->   nltk.download('stopwords')

install json-lines using spyder console   ---->   !pip install json-lines
====================================================

""" 
import json_lines
from featureExtraction import featureExtraction
from sklearn.decomposition import PCA
import random
from sklearn.svm import SVR

# number of tweets in dataset (can be changed to test code with smaller dataset)
nTweets = 2459


# read file and store all instances in one variable
instances = []
with open(r'dataset\instances.jsonl', 'rb') as f: # opening file in binary(rb) mode    
   for item in json_lines.reader(f):
       instances.append(item)
 
# read labels (true class)
labels = []
with open(r'dataset\truth.jsonl', 'rb') as f: # opening file in binary(rb) mode    
   for item in json_lines.reader(f):
       labels.append(item)
       
trueClass = []
for i in labels:
    if(str(i['truthClass'])=='clickbait'):
        trueClass.append(1)
    else:
        trueClass.append(0)
        
del labels

# Extract features
features = featureExtraction(instances)
features = features.transpose()
del instances


# n-fold cross-validation
n = 5
error = 0
avgRecall = 0
avgPrecision = 0

for i in range(0,n):
    nTr = nTweets - int(nTweets/n)
    trainingNum = random.sample(range(1, nTweets), nTr)
    trainingSet = []
    trainingLabels = []
    testingSet = []
    testingLabels = []
    # divide dataset into training and testing randomly
    for j in range(0,nTweets):
        if j in trainingNum:
            trainingSet.append(features[j])
            trainingLabels.append(trueClass[j])
        else:
            testingSet.append(features[j])
            testingLabels.append(trueClass[j])
            
            
    # feature selection using PCA preserving 99% variance
    my_PCA = PCA(n_components=0.99, svd_solver='full')
    trainingSet = my_PCA.fit_transform(trainingSet)
    
    # fit SVR on training data
    clf = SVR(C=1.0, epsilon=0.01, kernel = 'linear')
    clf.fit(trainingSet, trainingLabels) 
    
    # transform testing dataset features 
    testingSet = my_PCA.fit_transform(testingSet)
    
    # predict classes of testing dataset using trained SVR
    result = clf.predict(testingSet)
    
    correct11 = 0  # clickbait class
    correct00 = 0  # no-clickbait
    incorrect10 = 0  # trueClass is clickbait and classified as no-clickbait
    incorrect01 = 0   # trueClass is no-clickbait and classified as clickbait
    for i in range(0,int(nTweets/n)):
        if(result[i] <0.5):
            result[i] = 0
        else:
            result[i] = 1
            
        if(result[i] == testingLabels[i] and result[i] == 1):
            correct11 = correct11 + 1
        elif (result[i] == testingLabels[i] and result[i] == 0):
            correct00 = correct00 + 1
        elif (result[i] != testingLabels[i] and result[i] == 0):
            incorrect10 = incorrect10 + 1
        else:
            incorrect01 = incorrect01 + 1
            
    error = error + ((incorrect10 + incorrect01)/(correct00 + correct11 + incorrect10 + incorrect01))
    precision = correct11 / (correct11 + incorrect01)
    recall = correct11 / (correct11 + incorrect10)
    recall = 0
    precision = 0
    avgRecall = avgRecall + recall
    avgPrecision = avgPrecision + precision
    
error = error/n
avgRecall = avgRecall / n
avgPrecision = avgPrecision / n
print("error ", error, " avgRecall ", avgRecall, " avgPrecision ", avgPrecision)