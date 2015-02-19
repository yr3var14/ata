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

