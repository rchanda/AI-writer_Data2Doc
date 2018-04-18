"""The file contains name settings."""
import torch
file_loc = '../boxscore-data/rotowire/'
use_cuda = torch.cuda.is_available()
MAX_LENGTH = 664
LAYER_DEPTH = 2
MAX_SENTENCES = None
# USE_MODEL = None
USE_MODEL = ['../model/demo/ALL_BiLSTM_encoder_10000', '../model/demo/ALL_BiLSTM_decoder_10000']

# Parameter for training
EMBEDDING_SIZE = 600
LR = 0.01
ITER_TIME = 10000
BATCH_SIZE = 8

# Parameter for display
GET_LOSS = 1
SAVE_MODEL = 5000
ENCODER_STYLE = 'BiLSTM'
#ENCODER_STYLE = 'RNN'
OUTPUT_FILE = 'default'
USE_MODEL = None
