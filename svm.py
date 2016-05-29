#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import util
from sklearn import svm
from sklearn import grid_search
from sklearn import preprocessing
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score


def printParams(clf):
    try:
        print(clf.coef_)
        print(clf.intercept_)
    except:
        print('Error: svm must use linear kernel.')


def loadData(filename):
    dataset = util.loadFeaturesFromFile(filename)
    y = dataset[:, 0]
    X = dataset[:, 1:]
    return y, X

if __name__ == '__main__':
    train_file = sys.argv[1]
    test_file = sys.argv[2]
    use_scaler = False

    print('load features...')
    y, X = loadData(train_file)
    test_y, test_X = loadData(test_file)

    if use_scaler:
        scaler = preprocessing.StandardScaler().fit(X)
        X = scaler.transform(X)
        test_X = scaler.transform(test_X)

    print('train SVM...')
    #clf = svm.SVC(kernel='linear', C=10**-5)
    clf = svm.SVC(kernel='rbf', C=0.1, gamma=0.1)
    clf.fit(X, y)

    pred = clf.predict(test_X)

    accuracy = accuracy_score(test_y, pred)
    print('Accuracy: %.2f' % accuracy)
