import os
import sys
import numpy as np
import fastText
from metric import mutli_file_test
from config import *

model_name = 'fasttext'

save_path = save_path.format(model_name)
result_path = result_path.format(model_name)

def train():
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    model = fastText.train_supervised(input=train_dir, dim=64, pretrainedVectors=pretrain_dir, epoch=50)
    print(val_dir)
    print(model.test(val_dir))
    model.save_model(save_path)

def test(test_data):

    model = fastText.load_model(save_path)
    test_data = list(map(lambda x: x.split('__label__')[0], open(test_data)))
    y_pred = model.predict(test_data)[0]
    for item in y_pred:
        if len(item) > 1:
            print(item)
    return y_pred
    y_pred = list(map(lambda x: x[0].split('__label__')[1], y_pred))
    for item in y_pred:
        if len(item.split()) > 1:
            print(item)
    return y_pred

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ['train', 'test']:
        raise ValueError("""usage: python run_fasttext.py [train / test]""")

    if sys.argv[1] == 'train':
        train()
    else:
        mutli_file_test(test, result_path)
