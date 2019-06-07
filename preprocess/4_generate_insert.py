# -*- coding: utf-8 -*-
import json
import os
import random
import sys
sys.path.append('../')
import jieba

from config import base_dir

data_dir = os.path.join(base_dir, 'data')
src = 'content'
target = 'insert'

process_name = ['train']
generate_cnt = 1
insert_cnt = 1

def sentence_sample(datas, labels, target_label):
    idxs = []
    assert len(datas) == len(labels)
    l = len(labels)
    for i in range(l):
        if len(labels[i]) == len(target_label):
            flag = True
            for j in range(len(labels[i])):
                if labels[i][j] != target_label[j]:
                    flag = False
                    break
            if flag:
                idxs.append(i)
    idx = random.choice(idxs)
    return random.choice(datas[idx])    

def function():
    random_dir = os.path.join(data_dir, 'insert')
    if not os.path.isdir(random_dir):
        os.mkdir(random_dir)
    for name in process_name:

        label_dir = os.path.join(data_dir, 'data_{}_{}_label.json'.format(name, src))
        labels = [json.loads(line) for line in open(label_dir)]
        for i in range(len(labels)):
            labels[i].sort()
        data_dir = os.path.join(data_dir, 'data_{}_{}.json'.format(name, src))
        datas = [line.split('。') for line in open(data_dir)]

        for cnt in range(generate_cnt):
            targetfile = open(os.path.join(
                random_dir, 'data_{}_{}_{}.txt'.format(name, target, cnt)), 'w')
            
            for rawx, label in zip(datas, labels):
                
                for _i in range(insert_cnt):
                    sentence = sentence_sample(datas, labels, label)
                    loc = random.randrange(0, len(rawx), 1)
                    rawx.insert(loc, sentence)
                
                targetfile.write('。'.join(rawx)+'\n')

            targetfile.close()

if __name__ == "__main__":
    function()
