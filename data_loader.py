# coding: utf-8

from collections import Counter
import json
import numpy as np
import tensorflow.keras as kr
import os

def read_file(filename):
    """读取文件数据"""
    contents, labels = [], []
    with open(filename) as f:
        for line in f:
            try:
                content, *label = line.strip().split(' __label__')
                if content:
                    contents.append(content.split())
                    labels.append(label)
            except:
                pass
    return contents, labels


def build_vocab(train_dir, vocab_dir, vocab_size=5000):
    """根据训练集构建词汇表，存储"""
    data_train, data_label = read_file(train_dir)
    all_data = []
    all_label = set()
    
    for content in data_train:
        all_data.extend(content)
    counter = Counter(all_data)
    count_pairs = counter.most_common(vocab_size - 1)
    words, _ = list(zip(*count_pairs))
    words = ['<PAD>'] + list(words)
    
    for label in data_label:
        all_label.update(label)
    all_label = list(all_label)

    open(os.path.join(vocab_dir, 'vocab.txt'), mode='w').write('\n'.join(words) + '\n')
    open(os.path.join(vocab_dir, 'label.txt'), mode='w').write('\n'.join(all_label) + '\n')

def read_vocab(vocab_dir):
    
    with open(os.path.join(vocab_dir, 'vocab.txt')) as fp:
        words = [_.strip() for _ in fp.readlines()]
    word_to_id = dict(zip(words, range(len(words))))
    return words, word_to_id


def read_category(vocab_dir):

    with open(os.path.join(vocab_dir, 'label.txt')) as fp:
        categories = [_.strip() for _ in fp.readlines()]
    cat_to_id = dict(zip(categories, range(len(categories))))

    return categories, cat_to_id


def to_words(content, words):
    
    return ''.join(words[x] for x in content)


def process_file(filename, word_to_id, cat_to_id, max_length=600):
    
    contents, labels = read_file(filename)

    data_id, label_id = [], []
    for i in range(len(contents)):
        data_id.append([word_to_id[x] for x in contents[i] if x in word_to_id])
        label_id.append([cat_to_id[x] for x in labels[i]])

    x_pad = kr.preprocessing.sequence.pad_sequences(data_id, max_length)
    class_matrix = np.eye(len(cat_to_id))
    y_pad = np.array(list(map(lambda x: np.sum(class_matrix[x], axis=0), label_id)))

    return x_pad, y_pad


def batch_iter(x, y, batch_size=64):
    """生成批次数据"""
    data_len = len(x)
    num_batch = int((data_len - 1) / batch_size) + 1

    indices = np.random.permutation(np.arange(data_len))
    x_shuffle = x[indices]
    y_shuffle = y[indices]

    for i in range(num_batch):
        start_id = i * batch_size
        end_id = min((i + 1) * batch_size, data_len)
        yield x_shuffle[start_id:end_id], y_shuffle[start_id:end_id]
