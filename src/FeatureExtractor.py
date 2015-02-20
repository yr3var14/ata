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

import sklearn
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import *
from sklearn.feature_extraction.text import *
from sklearn import svm
from sklearn.datasets import load_iris
class FeatureExtractor:
	Vocab = []
	iris=[]
	
	def __init__ (self,filename):
		
		#self.iris = load_iris()
		#cat=['alt.atheism','soc.religion.christian','comp.graphics', 'sci.med']
		#filename='/home/sonali/Desktop/20news-bydate-train'
		self.Vocab= sklearn.datasets.load_files(filename, description=None, categories=None, load_content=True, shuffle=True, encoding='latin1', charset=None, charset_error=None, decode_error='strict', random_state=42)

	def getFeatures(self, option):
		if option=='tfidf':
			tf=TfidfTransformer()
			X_new=tf.fit_transform(self.Vocab.data)
			
		elif option=='bow':
			vectorizer = CountVectorizer()
			X_new=vectorizer.fit_transform(self.Vocab.data)
		elif option=='svm':
			vectorizer = CountVectorizer()
			X=vectorizer.fit_transform(self.Vocab.data)
			tf=TfidfTransformer()
			X_new=tf.fit_transform(X)
		elif option=='w2v':
			word2vec()
		elif option=='BOW-lv':
			vectorizer = CountVectorizer()
			X=vectorizer.fit_transform(self.Vocab.data)
			sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
			X_new=sel.fit_transform(X)
		else:
			print 'Please Select a difined type of feature'
		return X_new
	def word2vec(self):
		print 'have to work on it word2vec'
#compute and return vectors
#more option are to be added
#def any summary print visualize function
