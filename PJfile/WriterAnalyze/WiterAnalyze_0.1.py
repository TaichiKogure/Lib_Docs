# %%
import torch

torch.cuda.is_available()

# %%
import os
import glob
import codecs
import logging
import re
import random
from itertools import chain

# �`�ԑf��͗p�̊O�����W���[��
from janome.tokenizer import Tokenizer
from gensim.models import Word2Vec

# LSTM�p�̃��W���[��
import copy
import numpy as np
from numpy.random import rand  # �����_���ȃx�N�g������邽�߂̊֐�
from tqdm import tqdm  # ���[�v�̐i�����������W���[��
import torch  # �[�w�w�K�p�̃��W���[��
import torch.nn as nn  # �j���[�����l�b�g���[�N�p�̃��W���[��
import torch.nn.functional as F  # �������֐��p�̃��W���[��
import torch.optim as optim  # Pytorch�̃I�v�e�B�}�C�U�[
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

#�@���̓f�[�^�̓ǂݍ���
try:
    from google.colab implort drive#Google Drive����t�@�C����ǂݍ��ނ��߂̊O�����W���[��
    drive.mount('./gdrive')
    #base_dir��Ɋe��҂̃f�B���N�g�������邱�Ƃ�z��
    #base_dir = './gdrive/My Drive/Colab Notebooks'
    #base_dir =  'C:\Users\auror\PycharmProjects\Python3.7Gre\PJfile\WriterAnalyze'

except ModuleNotFoundErr:
    base_dir = './'
