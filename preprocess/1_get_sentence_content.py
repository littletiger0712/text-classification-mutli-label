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


def get_label(y_raw):
    if y_raw['death_penalty'] == True:
        return 0
    if y_raw['life_imprisonment'] == True:
        return 1
    
    month = y_raw['imprisonment']

    if month >= 180:
        return 2
    if month >= 84:
        return 3
    if month >= 48:
        return 4
    return 5

def get_label_origin(y_raw):
    if y_raw['death_penalty'] == True:
        return 'death_penalty'
    if y_raw['life_imprisonment'] == True:
        return 'life_imprisonment'
    return str(y_raw['imprisonment'])

def get_name(y_raw):
    pass

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
