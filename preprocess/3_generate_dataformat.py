# -*- coding: utf-8 -*-
import json
import os
import random
import sys
sys.path.append('../')

from config import base_dir, test_dirs

data_dir = os.path.join(base_dir, 'data')
src = 'jieba'
target = 'fasttext'
test_dir = os.path.join(data_dir, 'test')
if not os.path.isdir(test_dir):
    os.mkdir(test_dir)

generate_cnt = 10
process_name = ['train', 'valid', 'test']

def function():

    for name in process_name:
        content =open(os.path.join(data_dir, 'data_{}_jieba.json'.format(name)))
        lables = open(os.path.join(data_dir, 'data_{}_content_label.json'.format(name)))
        targetfile = open(os.path.join(data_dir, 'data_{}_{}.txt'.format(name, target)), 'w')

        for x_cut, label in zip(content, lables):
            x_cut = json.loads(x_cut)
            label = json.loads(label)
            targetfile.write('{} __label__{}\n'.format(' '.join(x_cut), ' __label__'.join(label)))
        content.close()
        lables.close()
        targetfile.close()

if __name__ == "__main__":
    function()
