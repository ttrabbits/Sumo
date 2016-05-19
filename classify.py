#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import numpy as np


weights = np.array([
    0.02621, # win in this basho
    -0.02636, # lose in this basho
    0.05265, # total win for this opponent
    -0.05265, # total lose for this opponent
    0.00334, # yokozuna
    0.00463, # ozeki
    0.00133, # sonotsugi
    -0.00154, # sono
    -0.00776, # sono
    -0.02621, # opponent win in this basho
    0.02636, # opponent lose in this basho
    -0.00334, # opponent yokozuna
    -0.00463, # opponent ozeki
    -0.00133, # ika ryaku
    0.00154,
    0.00776,
])

bias = -1.85745516e-14


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
    test_file = sys.argv[1]
    dataset = loadFeaturesFromFile(test_file)

    y = dataset[:,0]
    X = dataset[:,1:]

    for i, x in enumerate(list(X)):
        if i % 2 == 1:
            continue
        if np.dot(weights,x) + bias >= 0:
            print('left')
        else:
            print('right')
