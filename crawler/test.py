#-*- encoding:utf-8 -*-

import xlrd
import os
import requests
from collections import defaultdict
from selenium import webdriver
import types
import re
from redis import Redis
from pymongo import MongoClient
import time
import threading
# from Queue import Queue
import Queue
import pdb
import xlwt
import sys
from gevent.pool import Pool
import codecs

complete = [False] * 10

def test():

    complete[1] = True
    complete[2] = True
    complete[3] = True

    for i in complete:
        print i

def test2():

    print '*' * 100

    print complete

if __name__ == '__main__':
    os.system('printf "\033c"')

    test()
    test2()

    # pools = Pool(3)
    # pools.map(test, xrange(1000))
    # print codecs.open('200.txt', 'r', 'utf-8').readlines()
