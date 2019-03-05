import os

num_classes = 202

base_dir = '/home/dl/zs/text-classification-mutli-label'
data_dir = os.path.join(base_dir, 'data')

train_dir = os.path.join(data_dir, 'data_train_fasttext.txt')
val_dir = os.path.join(data_dir, 'data_valid_fasttext.txt')
test_dir = os.path.join(data_dir, 'data_test_fasttext.txt')
vocab_dir = os.path.join(data_dir, 'cail_vocab')
pretrain_dir = os.path.join(data_dir, 'zh.bin')

save_dir = os.path.join(base_dir, 'checkpoints')
save_path = os.path.join(save_dir, '{}/model')
result_path = os.path.join(base_dir, '{}/result')