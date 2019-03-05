import json
import os
from collections import Counter

import numpy as np
import pandas as pd
from sklearn import metrics

from config import base_dir

origin_test_path = os.path.join(base_dir, 'data/data_test_fasttext.txt')

def mutli_file_test(function, path):
    y_pred = []
    for test_dir in test_dirs:
        y_pred.append(function(test_dir))
    np.save(path, np.concatenate(y_pred, 0))
    

def get_y_true():
    f = map(lambda x: x.split('__label__')[1], open(origin_test_path))
    return np.array(list(f))

models = ['fasttext']
y_true = get_y_true()

if __name__ == "__main__":

    result = []
    item = {
        'acc': 1,
        'mov': 0,
    }
    item.update(Counter(y_true))
    result.append(item)


    for model in models:

        y_preds =np.load(os.path.join(base_dir, 'checkpoints/{}/result.npy'.format(model)))
        l = y_true.shape[0]    
        y_preds = y_preds.reshape(-1, l)[0]
        y_origin = y_preds[0]
        for y_pred in y_preds:
            item = {
                'acc': np.sum(y_true==y_pred)/l,
                'mov': np.sum(y_pred==y_origin)/l,
            }
            print(y_pred)
            item.update(Counter(y_pred))
            result.append(item)
        print(metrics.classification_report(y_true, y_pred))
        print(metrics.confusion_matrix(y_true, y_pred))
    result = pd.DataFrame(result)
    result.to_csv(os.path.join(base_dir, 'checkpoints/result.csv'))
