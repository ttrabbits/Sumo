#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import numpy as np
from sklearn import svm
from sklearn import grid_search
from sklearn import preprocessing
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score

def loadFeaturesFromFile(filename):
    dataset = []
    with open(filename) as infile:
        for line in infile:
            line = [float(x) for x in line.strip().split(',')]
            if not line:
                continue
            if line[0] == 0:
                continue
            dataset.append(line)
    return np.array(dataset)


if __name__ == '__main__':
    train_file = sys.argv[1]
    test_file = sys.argv[2]

    print('load features...')
    dataset = loadFeaturesFromFile(train_file)
    y = dataset[:,0]
    X = dataset[:,1:]
    scaler = preprocessing.StandardScaler().fit(X)
    #X = scaler.transform(X)

    testdata = loadFeaturesFromFile(test_file)
    testy = testdata[:,0]
    testX = testdata[:,1:]
    #testX = scaler.transform(testX)

    # if rbf, C = 0.1 gamma = 0.1
    # if linear, C = 10**-5
    print('train SVM...')
    #clf = svm.SVC(kernel='linear', C=10**-5)
    clf = svm.SVC(kernel='rbf', C=0.1, gamma=0.1)
    clf.fit(X, y)

    #for w in clf.coef_[0]:
    #    print(w)

    pred = clf.predict(testX)

    #print(pred)

    print(accuracy_score(testy, pred))

    #print(clf.coef_)
    #print(clf.intercept_)
