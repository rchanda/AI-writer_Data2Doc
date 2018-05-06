"""The file contains name settings."""
import torch
file_loc = '../boxscore-data/rotowire/'
use_cuda = torch.cuda.is_available()

MAX_LENGTH = 800
LAYER_DEPTH = 2
MAX_SENTENCES = 5
MAX_TRAIN_NUM = 200

Model_name = 'pretrain_copy_ms5'
#Model_name = 'pretrain_ms8'
iterNum = 22000
USE_MODEL = None
if Model_name is not None:
    USE_MODEL = ['../models/'+Model_name + '_' + s + '_' + str(iterNum) for s in ['encoder', 'decoder', 'optim']]
# USE_MODEL = ['./models/clipped_encoder_25440', './models/clipped_decoder_25440']
# USE_MODEL = ['./models/long3_encoder_36040',
#              './models/long3_decoder_36040',
# './models/long3_optim_36040']

# Parameter for training
EMBEDDING_SIZE = 600
LR = 0.01  # Adagrad
# LR = 0.003  # Adam
ITER_TIME = 220
BATCH_SIZE = 2
GRAD_CLIP = 5

# Parameter for display
GET_LOSS = 1
SAVE_MODEL = 5

# Choose models

# ENCODER_STYLE = 'LIN'
#ENCODER_STYLE = 'BiLSTM'
#ENCODER_STYLE = 'RNN'
#DECODER_STYLE = 'RNN'

# ENCODER_STYLE = 'HierarchicalBiLSTM'
ENCODER_STYLE = 'HierarchicalRNN'
DECODER_STYLE = 'HierarchicalRNN'
OUTPUT_FILE = 'pretrain_copy_ms5'
COPY_PLAYER = True
TOCOPY = True

# DATA PREPROCESSING
""" Ken added """
MAX_PLAYERS = 31  # information taken from rotowire
PLAYER_PADDINGS = ['<PAD' + str(i) + '>' for i in range(0, MAX_PLAYERS)]
