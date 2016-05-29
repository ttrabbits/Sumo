#!/usr/bin/python

import numpy as np


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
