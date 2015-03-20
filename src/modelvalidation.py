"""
@author:- sonacse12 and rohitguptacse12 
this is a function used to find out best value of alpha for different model and to choose best model according to that value.
"""


def validationerror(option,X_train,X_test,y_train,y_test):
	alphas = np.logspace(-5, 1, 60)
	train_errors = list()
	test_errors = list()

	for alpha in alphas:
		if option == 'svm':
			clf=SGDClassifier(alpha=alpha, n_iter=50,penalty="elasticnet")

		elif option == 'multinomial':
			clf=MultinomialNB(alpha=alpha)

		elif option == 'bernouli':
			clf=BernoulliNB(alpha=alpha)
		
		clf.fit(X_train, y_train)
		train_errors.append(mean_squared_error(y_train, clf.predict(X_train)))
		test_errors.append(mean_squared_error(y_test, clf.predict(X_test)))
	print test_errors
	print alphas
	i_alpha_optim = np.argmin(test_errors)
	alpha_optim = alphas[i_alpha_optim]
	print i_alpha_optim
	print alpha_optim
	print X_train.shape[0]
	plt.subplot(2, 1, 1)
	plt.semilogx(alphas, train_errors, label='Train')
	plt.semilogx(alphas, test_errors, label='Test')
	plt.vlines(alpha_optim, plt.ylim()[0], np.max(test_errors), color='k',
           linewidth=3, label='Optimum on test')
	plt.legend(loc='lower left')
	plt.ylim([0, 1.2])
	plt.xlabel('Regularization parameter')
	plt.ylabel('Performance')
	plt.legend()
	plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.26)
	plt.show()

