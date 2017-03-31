#!/usr/bin/env	python
#coding:utf-8
#author: zhangjun

import sys

data = {}
data['type'] = {}
data['area'] = {}
data['number'] = {}


def loadData():
    with open("mobilephones.txt") as file:
        lines = file.read() #split('----------\n')

    info = lines.split('----------\n')
    for block in info:
        lines = block.split('\n')
        if lines[0] == 'type':
            for i in  lines[1:]:
                s = i.strip().split(',')
                if len(s) == 2:
                    data['type'][s[0]] = s[1]

        if lines[0] == 'area':
            for i in  lines[1:]:
                s = i.strip().split(',')
                if len(s) == 2:
                    data['area'][s[0]] = s[1]

        if lines[0][:7] == 'number-':
            num = []
            for i in lines[1:]:
                s = i.strip().split(',')
                if len(s) == 2:
                    num.append(s)
            data['number'][lines[0][7:]] = num
    return data


def query(num):
    num = str(num)
    data = loadData()
    i = num[:3]
    j = int(num[3:7],10)
    if data['number'].has_key(i):
        info = data['number'][i][j]
        area = data['area'][info[0]]
        type = data['type'][info[1]]
        print area,type

if __name__=='__main__':
    num = sys.argv[1]
    query(num)
