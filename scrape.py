#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from scraper import Scraper


if __name__ == '__main__':
    scraper = Scraper()

    month_list = ('01', '03', '05', '07', '09', '11')

    dataset = []
    for year in range(2016, 2017):
        for month in month_list:
            if year == 2016 and month == '05':
                break
            for day in range(1, 3):
                basho = '%d%s' % (year, month)
                print('%s-%d' % (basho, day))
                scraper.fetchUrl(scraper.makeUrl(basho, day))
                scraper.parseHtml()
                dataset += scraper.getData()
            break

    # TODO: for SVMrank format
    for data in dataset:
        y = str(data[0])
        x = [str(v) for v in data[1]]
        print('%s,%s' % (y, ','.join(x)))
