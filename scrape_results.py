#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import datetime
import requests
from pyquery import PyQuery as pq


class Scraper:
    dom = None

    def __init__(self):
        pass


    def fetchUrl(self, url):
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        self.dom = pq(res.text)


    def loadLocalHtml(self, filename):
        if not os.path.exists(filename):
            print('Error: %s not found' % filename)

        infile = open(filename)
        html = infile.read()
        infile.close()
        self.dom = pq(html)


    def printHtml(self):
        if not self.dom:
            print('ERROR: not loaded')
            return
        p = self.dom('html')
        print(p.html())


    def parseHtml(self):
        if not self.dom:
            print('ERROR: not loaded')
            return

        tables = self.dom.find('.tk_table')
        for table in tables('table').items():
            break

        results = []
        for i, tr in enumerate(pq(table).find('tr').items()):
            if i == 0:
                continue

            td_htmls = []
            for td in pq(tr).find('td').items():
                td_htmls.append(pq(td).html())

            data = self._extractData(td_htmls)
            results += data
            print(data)
        print(results)
        return


    def _extractData(self, td_htmls):
        left_img = pq(td_htmls[0]).attr('src')
        right_img = pq(td_htmls[4]).attr('src')
        left_banzuke, left_score = [elem.text() for elem in pq(td_htmls[1]).find('font').items()]
        right_banzuke, right_score = [elem.text() for elem in pq(td_htmls[3]).find('font').items()]
        past_record = pq(td_htmls[2]).find('a').text()

        past_left_win, past_right_win = self._extractPastMatchRecord(past_record)
        left_data = self._makeResultData(left_score, past_left_win, past_right_win, left_banzuke, left_img)
        right_data = self._makeResultData(right_score, past_right_win, past_left_win, right_banzuke, right_img)

        return (left_data, right_data)


    def _makeResultData(self, score, past_win, past_lose, banzuke, img_name):
        win, lose = self._extractCurrentScore(score)
        vector = [
            win,
            lose,
            past_win,
            past_lose,
        ] + self._makeBanzukeVector(banzuke)
        result = self._getResultFromImgName(img_name)
        return (vector, result)


    def _makeBanzukeVector(self, banzuke):
        if '横綱' in banzuke:
            return [1, 0, 0, 0, 0]
        elif '大関' in banzuke:
            return [0, 1, 0, 0, 0]
        elif '関脇' in banzuke:
            return [0, 0, 1, 0, 0]
        elif '小結' in banzuke:
            return [0, 0, 0, 1, 0]
        else:
            return [0, 0, 0, 0, 1]


    def _extractPastMatchRecord(self, record):
        record = re.sub('\[.*?\]', '', record)
        record = re.sub('\(.*?\)', '', record)
        return [int(x) for x in record.split('-')]


    def _extractCurrentScore(self, score):
        scores = splitByRegExp('^([0-9]+)勝([0-9]+)敗', score)
        if not scores:
            return [0, 0]
        return [int(x) for x in scores]


    def _getResultFromImgName(self, img_name):
        if 'hoshi_kuro' in img_name:
            return -1
        elif 'hoshi_shiro' in img_name:
            return 1
        else:
            return 0


def splitByRegExp(regexp, string):
    m = re.search(regexp, string.strip())
    if not m:
        return []
    return m.groups()


if __name__ == '__main__':
    scraper = Scraper()
    scraper.loadLocalHtml('testdata.html')
    #scraper.fetchUrl('http://sumodb.sumogames.de/Results.aspx?b=201603&d=9&l=j')
    scraper.parseHtml()
