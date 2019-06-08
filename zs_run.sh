head -q -n 10000 data/data_train_fasttext.txt.ori > data/data_train_fasttext.txt
nohup python run_fasttext.py > fasttext_1w_ori.log 2>&1 &
nohup python run_cnn.py > cnn_1w_ori.log 2>&1 &
head -q -n 10000 data/data_train_fasttext.txt.ori data/data_train_fasttext.txt.2 data/data_train_fasttext.txt.3 data/data_train_fasttext.txt.4 > data/data_train_fasttext.txt
nohup python run_fasttext.py > fasttext_1w_aug.log 2>&1 &
nohup python run_cnn.py > cnn_1w_aug.log 2>&1 &

head -q -n 50000 data/data_train_fasttext.txt.ori > data/data_train_fasttext.txt
nohup python run_fasttext.py > fasttext_5w_ori.log 2>&1 &
nohup python run_cnn.py > cnn_5w_ori.log 2>&1 &
head -q -n 50000 data/data_train_fasttext.txt.ori data/data_train_fasttext.txt.2 data/data_train_fasttext.txt.3 data/data_train_fasttext.txt.4 > data/data_train_fasttext.txt
nohup python run_fasttext.py > fasttext_5w_aug.log 2>&1 &
nohup python run_cnn.py > cnn_5w_aug.log 2>&1 &

head -q -n 100000 data/data_train_fasttext.txt.ori > data/data_train_fasttext.txt
nohup python run_fasttext.py > fasttext_10w_ori.log 2>&1 &
nohup python run_cnn.py > cnn_10w_ori.log 2>&1 &
head -q -n 100000 data/data_train_fasttext.txt.ori data/data_train_fasttext.txt.2 data/data_train_fasttext.txt.3 data/data_train_fasttext.txt.4 > data/data_train_fasttext.txt
nohup python run_fasttext.py > fasttext_10w_aug.log 2>&1 &
nohup python run_cnn.py > cnn_10w_aug.log 2>&1 &

