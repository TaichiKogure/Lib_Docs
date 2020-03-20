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
#���͂���m�C�Y������
RUBY_PATTERN = re.compile('�@�s.*?�t')#��т̐��K�\���p�^�[��
ADDITION_PATTERN = re.compile('[.*\]| �@�@ �i.*\'�j')#���͒��̕⑫���̃p�^�[��
ALPHABET_PATTERN = re.compile('[a-zA-Z]')#�A���t�@�x�b�g�̐��K�\���o�^�[��

def delete_newline_char(line):
    '''���s�R�[�h�����ׂč폜����'''
    return line.replace('\r', '').replace('\n','')

def remove_ruby(line):
    '''��т��폜����'''
    return RUBY_PATTERN.sub('', line)

def remove_additions(line):
    '''�⑫��������'''
    return ADDITION_PATTERN.sub('', line)

def remove_escape_char(line):
    '''�G�X�P�[�v���ꂽ����������'''
    return line.replace('\u3000', '')

def remove_symbols(line):
    '''�L��������'''
    line = line.replace('-', '').replace(':', '').replace('/', '').replace('(', '').replace('(','')
    return line

def remove_alphabets(line):
    '''�A���t�@�x�b�g������'''
    return ALPHABET_PATTERN.sub('', line)

def separate_line_with_puncs(line):
    '''��_�ŋ�؂�������f���o��'''
    for line in lines:
        for sentence in line.split('�B'):
            yield sentence

def preprocess(data):
    '''���͂�O�������ĕ��̃��X�g�ɂ���'''
    lines = map(delete_newline_char, data)
    lines = map(remove_ruby, lines)
    lines = map(remove_additions, lines)
    lines = map(remove_escape_char, lines)
    lines = map(remove_symbols, lines)
    sentences = separate_line_with_puncs(lines)
    #'''���͂�����̂��̂���������'''
    sentences = filter(lambda  x: len(x), sentences)
    return list(sentences)

