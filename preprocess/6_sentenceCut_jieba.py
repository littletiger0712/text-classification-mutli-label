# -*- coding: utf-8 -*-
import json
import os
import sys
sys.path.append('../')
import jieba

from config import base_dir

data_dir = os.path.join(base_dir, 'data')
src = 'content'
target = 'jieba'

process_name = ['valid', 'test']

def function():
    stopwords = list(map(lambda x: x[:-1], open(os.path.join(data_dir, 'stop_words.txt'))))

    for name in process_name:
        srcfile = open(os.path.join(
            data_dir, 'data_{}_{}.json'.format(name, src)))
        targetfile = open(os.path.join(
            data_dir, 'data_{}_{}.json'.format(name, target)), 'w')

        for line in srcfile:
            x_cut = list(filter(lambda x: x not in stopwords, jieba.cut(line)))
            targetfile.write(json.dumps(x_cut)+'\n')
        srcfile.close()
        targetfile.close()

if __name__ == "__main__":
    function()
