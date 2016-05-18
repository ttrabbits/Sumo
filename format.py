#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':

    filename = sys.argv[1]
    dataset = []
    with open('data/row/%s.txt' % filename) as infile:
        for line in infile:
            line = line.strip().split(',')
            if not line:
                continue
            dataset.append(line)


    with open('data/feature/%s.txt' % filename, 'w') as outfile:
        qid = 1
        counter = 0
        for data in dataset:
            y = data[0]
            xs = data[1:]

            if int(y) == 0:
                continue

            features = ['%d:%s' % (i+1, x) for i, x in enumerate(xs)]
            line = '%s qid:%d ' % (y, qid) + ' '.join(features)

            outfile.write(line + '\n')

            counter += 1
            if counter == 2:
                qid += 1
                counter = 0
