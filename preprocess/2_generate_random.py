# -*- coding: utf-8 -*-
import json
import os
import random
import sys
sys.path.append('../')

from config import base_dir

data_dir = os.path.join(base_dir, 'data')
src = 'content'
target = 'random'

process_name = ['train']
generate_cnt = 1

def function():

    random_dir = os.path.join(data_dir, 'delete')
    if not os.path.isdir(random_dir):
        os.mkdir(random_dir)
    
    for name in process_name:
        for cnt in range(generate_cnt):
            srcfile = open(os.path.join(
                data_dir, 'data_{}_{}.json'.format(name, src)))
            targetfile = open(os.path.join(
                random_dir, 'data_{}_{}_{}.json'.format(name, target, cnt)), 'w')
    
            for line in srcfile:
                rawx = line.split('。')
                random.shuffle(rawx)
                targetfile.write('。'.join(rawx)+'\n')
            srcfile.close()
            targetfile.close()


if __name__ == "__main__":
    function()
