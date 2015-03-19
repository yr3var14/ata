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
@edited to return features on train data also
"""

import sklearn
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import *
from sklearn.feature_extraction.text import *
from sklearn import svm
import gensim
import nltk
from nltk.corpus import brown
class FeatureExtractor:
	Vocab = []
	Test_cab=[]
	vectoriser=CountVectorizer()
	iris=[]
	target=[]
	def __init__ (self,filetrain,filetest):
		
		#self.iris = load_iris()
		#cat=['alt.atheism','soc.religion.christian','comp.graphics', 'sci.med']
		#filename='/home/sonali/Desktop/20news-bydate-train'
		self.Vocab= sklearn.datasets.load_files(filetrain, description=None, categories=None, load_content=True, shuffle=True, encoding='latin1', charset=None, charset_error=None, decode_error='strict', random_state=42)
		self.Test_cab= sklearn.datasets.load_files(filetest, description=None, categories=None, load_content=True, shuffle=True, encoding='latin1', charset=None, charset_error=None, decode_error='strict', random_state=42)
		
	def getFeatures(self, option):
		if option=='tfidf':
			self.vectorizer=TfidfTransformer()
			X_new=self.vectorizer.fit_transform(self.Vocab.data)
			
		elif option=='bow':
			self.vectorizer = CountVectorizer()
			X_new=self.vectorizer.fit_transform(self.Vocab.data)
		elif option=='svm':
			vectorizer = CountVectorizer()
			X=vectorizer.fit_transform(self.Vocab.data)
			self.vectorizer=TfidfTransformer()
			X_new=self.vectorizer.fit_transform(X)
		elif option=='skB':
			self.vectorizer = SelectKBest(chi2, k=2)
			X_new =self.vectorizer.fit_transform(self.Vocab.data,self.Vocab.target )
		
		elif option=='BOW-lv':
			vectorizer = CountVectorizer()
			X=vectorizer.fit_transform(self.Vocab.data)
			self.vectorizer = VarianceThreshold(threshold=(.8 * (1 - .8)))
			X_new=self.vectorizer.fit_transform(X)
		else:
			print 'Please Select a defined type of feature'
			
		X_test=self.vectorizer.transform(self.Test_cab.data)
                y_test=self.Test_cab.target
		return X_new,self.Vocab.target,X_test,y_test
		
	def word2vecmodel(self):
		b=gensim.models.Word2Vec(brown.sents())
                b.save('/home/sonali/Desktop/corporamodel')
                return b  #returns a model which define vector for each word depending on contex
#compute and return vectors
#more option are to be added
#def any summary print visualize function
