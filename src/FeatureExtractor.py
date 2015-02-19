# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 13:38:14 2015

@author: anelk-var

The FeatureExtrator class defines various methods to extract different types of features. 
The following feature methods are implemented:
    option='tfidf'  calls tfidf vectorizer from sklearn
    option='bow'    calls sklearn?
    option='lsa'    calls sklearn?
    option='w2v'    internal word2vector implemmentation
    ... additional methods

Example code:

FE = FeatureExtractor(Text)
f_w2v = FE.getFeatures (option='w2v', text [,options])

"""

class FeatureExtractor:
    # define local variables like vocab. etc.
    Vocabulary = [];
    
    def __init__ (self, text):
        # initialize vocab. with text and other necessary variables

    def getFeatures(self, option, text [, additional_parameters]):
        
        if option=='tfidf':
            # compute and return features
        
        elif option=='bow':
            # compute and return features
        
        elif option=='lsa':
            # compute
        
        elif option=='w2v':
            # call word2vec
            
        else:
            print SomeError
    
    def word2vec(self):
        #compute and return vectors

    #def any summary print visualize functions