# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 14:17:17 2015

@author: anelk-var

The Classifier class defines various methods to learns (simple training and cross-validation), test and evaluate various models. 
The following methods are implemented:
    option='nbm'  calls Multinomial naviebayes from sklearn
    option='nbb'  calls Bernoulli naivebayes sklearn?
    option='svm'  support vector machine
    ... additional methods

Example code:

Cls = Classifier()

# simple learning for a given C
c_svm1 = Cls.learn (option='svm', train=f_w2v_train [,options])
# learning with crossvalidation for C
c_svm2 = Cls.learn (option='svm', train=f_w2v_train, CrossValidate=True [,options])

# c_svm is a dictionary with various fields filled in like
# c_svm[option]='svm', c_svm['CrossValidate']=True; and so on.
# The learn function fills up an additional field called c_svm[parameters].

# infer labels on test data
y_predicted = Cls.infer (predictor=cls_svm, test=f_w2v_test)

# evaluate predictions using various measures like f1(f1 measure), auc(area under ROC curve), acc(accuracy) etc.
Cls.evaluate (option='f1', predictions=y_predicted, truth=y_actual)


Classifier1 = ['svm', True, CRange, any_other_options] #True for CrossValidation
Classifier2 = ['nbm', True, CRange, any_other_options]
Classifiers = [Classifier1, Classifier2, Classifier3]
Metrics = ['f1', 'auc', 'acc']

results = Cls.learn_infer_evaluate (train, test, classifiers=Classifiers, metrics=Metrics)

Cls.plot(results)
"""

"""
@author:- rohitguptacse12 and sonacse12
this is the classifier class which takes the features from the featureExtractor class

"""

# p = FeatureExtractor()
# X_train , y_train = p.getFeatures('BOW-lv')

# q = FeatureExtractor()
# X_test , y_test = q.getFeatures('BOW-lv')
#
from __future__ import print_function

import logging
import numpy as np
from optparse import OptionParser
import sys
from time import time
import sklearn

from sklearn.svm import SVC
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.utils.extmath import density
from sklearn import metrics




class Classifier:
	
    results = []

    def getLearn(self, option):

	if option == 'svm':
	    results.append(evaluation(SVC(C=1)))

	elif option == 'multinomial':
	    results.append(evaluation(MultinomialNB(alpha=.01)))

	elif option == 'bernouli':
	    results.append(evaluation(BernoulliNB(alpha=.01)))

    def evaluation(clf):
    	print('_' * 80)
    	print("Training: ")
    	print(clf)
    	t0 = time()
    	clf.fit(X_train, y_train)
    	train_time = time() - t0
    	print("train time: %0.3fs" % train_time)

    	t0 = time()
    	pred = clf.predict(X_test)
    	test_time = time() - t0
    	print("test time:  %0.3fs" % test_time)
	
    	score = metrics.f1_score(y_test, pred)
    	print("f1-score:   %0.3f" % score)
	
    	if hasattr(clf, 'coef_'):
    	    print("dimensionality: %d" % clf.coef_.shape[1])
    	    print("density: %f" % density(clf.coef_))
    	    print()
	
	
    	print()
    	clf_descr = str(clf).split('(')[0]
    	return clf_descr, score, train_time, test_time
	
Cls=Classifer()
p.getLearn('svm')
		
		
