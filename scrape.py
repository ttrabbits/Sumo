#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from scraper import Scraper


if __name__ == '__main__':
    scraper = Scraper()

    month_list = ('01', '03', '05', '07', '09', '11')

    for year in range(2011, 2017):
        for month in month_list:
            dataset = []
            basho = '%d%s' % (year, month)
            if basho == '201605':
                break
            if basho == '201103':
                continue

            for day in range(1, 16):
                print('%s-%d' % (basho, day))
                scraper.fetchUrl(scraper.makeUrl(basho, day))
                scraper.parseHtml()
                dataset += scraper.getData()

            with open(basho + '.txt', 'w') as outfile:
                print('write ' + basho + '.txt')
                for data in dataset:
                    y = str(data[0])
                    x = [str(v) for v in data[1]]
                    outfile.write('%s,%s\n' % (y, ','.join(x)))
