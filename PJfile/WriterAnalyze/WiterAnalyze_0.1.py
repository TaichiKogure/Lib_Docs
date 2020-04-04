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

#
from janome.tokenizer import Tokenizer
from gensim.models import Word2Vec

#
import copy
import numpy as np
from numpy.random import rand  #
from tqdm import tqdm  #
import torch  #
import torch.nn as nn  #
import torch.nn.functional as F  #
import torch.optim as optim  #
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

#
try:
    from google.colab implort drive#Google Driveグーグルドライブから引き出すとき
    drive.mount('./gdrive')
    #base_dir
    #base_dir = './gdrive/My Drive/Colab Notebooks'
    #base_dir =  'C:\Users\auror\PycharmProjects\Python3.7Gre\PJfile\WriterAnalyze'

except ModuleNotFoundErr:
    base_dir = './'
#るびなどを修正する
RUBY_PATTERN = re.compile('�@�s.*?�t')#
ADDITION_PATTERN = re.compile('[.*\]| �@�@ �i.*\'�j')#
ALPHABET_PATTERN = re.compile('[a-zA-Z]')#

def delete_newline_char(line):
    ''''''
    return line.replace('\r', '').replace('\n','')

def remove_ruby(line):
    ''''''
    return RUBY_PATTERN.sub('', line)

def remove_additions(line):
    ''''''
    return ADDITION_PATTERN.sub('', line)

def remove_escape_char(line):
    ''''''
    return line.replace('\u3000', '')

def remove_symbols(line):
    ''''''
    line = line.replace('-', '').replace(':', '').replace('/', '').replace('(', '').replace('(','')
    return line

def remove_alphabets(line):
    ''''''
    return ALPHABET_PATTERN.sub('', line)

def separate_line_with_puncs(line):
    ''''''
    for line in lines:
        for sentence in line.split('B'):
            yield sentence

def preprocess(data):
    ''''''
    lines = map(delete_newline_char, data)
    lines = map(remove_ruby, lines)
    lines = map(remove_additions, lines)
    lines = map(remove_escape_char, lines)
    lines = map(remove_symbols, lines)
    sentences = separate_line_with_puncs(lines)
    #''''''
    sentences = filter(lambda  x: len(x), sentences)
    return list(sentences)

