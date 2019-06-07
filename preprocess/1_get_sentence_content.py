# -*- coding: utf-8 -*-
import json
import os
import sys
sys.path.append('../')
from config import base_dir
import math

data_dir = os.path.join(base_dir, 'data')
src = 'json'
target = 'content'
process_name = ['train', 'valid', 'test']


def function():
    for name in process_name:
        srcfile = open(os.path.join(
            data_dir, 'data_{}_{}.json'.format(name, src)))
        targetfile = open(os.path.join(
            data_dir, 'data_{}_{}.json'.format(name, target)), 'w')
        targetfile_label = open(os.path.join(
            data_dir, 'data_{}_{}_label.json'.format(name, target)), 'w')

        for line in srcfile:
            item = json.loads(line)
            rawx = item['fact']
            rawy = item['meta']['accusation']
            targetfile.write(rawx+'\n')
            targetfile_label.write(json.dumps(rawy)+'\n')
        srcfile.close()
        targetfile.close()
        targetfile_label.close()


if __name__ == "__main__":
    function()
