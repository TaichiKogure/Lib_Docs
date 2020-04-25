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

except ModuleNotFoundError:
    base_dir = './'
#るびなどを修正する
RUBY_PATTERN = re.compile('　《.*?》')#ルビの正規表現パターン
ADDITION_PATTERN = re.compile('[.*\]|　　　（.*\）')#文章中の補足情報のパターンカッコは全角
ALPHABET_PATTERN = re.compile('[a-zA-Z]')#アルファベットの正規表現パターン

def delete_newline_char(line):
    '''改行コードをすべて削除する'''
    return line.replace('\r', '').replace('\n','')

def remove_ruby(line):
    '''ルビを削除する'''
    return RUBY_PATTERN.sub('', line)

def remove_additions(line):
    '''補足情報を消す'''
    return ADDITION_PATTERN.sub('', line)

def remove_escape_char(line):
    '''エスケープされた文字を消す'''
    return line.replace('\u3000', '')

def remove_symbols(line):
    '''記号を消す'''
    line = line.replace('-', '').replace(':', '').replace('/', '').replace('(', '').replace('(','')
    return line

def remove_alphabets(line):
    '''アルファベットを消す'''
    return ALPHABET_PATTERN.sub('', line)

def separate_line_with_puncs(line):
    '''句点で区切った文を吐き出す'''
    for line in lines:
        for sentence in line.split('B'):
            yield sentence

def preprocess(data):
    '''文章を前処理して文のリストにする'''
    lines = map(delete_newline_char, data)
    lines = map(remove_ruby, lines)
    lines = map(remove_additions, lines)
    lines = map(remove_escape_char, lines)
    lines = map(remove_symbols, lines)
    sentences = separate_line_with_puncs(lines)
    #'''文がからのものを削除する・'''
    sentences = filter(lambda  x: len(x), sentences)
    return list(sentences)

Remake from Linux PC
