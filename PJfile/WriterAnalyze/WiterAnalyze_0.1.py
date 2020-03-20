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

# 形態素解析用の外部モジュール
from janome.tokenizer import Tokenizer
from gensim.models import Word2Vec

# LSTM用のモジュール
import copy
import numpy as np
from numpy.random import rand  # ランダムなベクトルを作るための関数
from tqdm import tqdm  # ループの進捗を示すモジュール
import torch  # 深層学習用のモジュール
import torch.nn as nn  # ニューラルネットワーク用のモジュール
import torch.nn.functional as F  # 活性化関数用のモジュール
import torch.optim as optim  # Pytorchのオプティマイザー
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

#　文章データの読み込み
try:
    from google.colab implort drive#Google Driveからファイルを読み込むための外部モジュール
    drive.mount('./gdrive')
    #base_dir上に各作者のディレクトリがあることを想定
    #base_dir = './gdrive/My Drive/Colab Notebooks'
    #base_dir =  'C:\Users\auror\PycharmProjects\Python3.7Gre\PJfile\WriterAnalyze'

except ModuleNotFoundErr:
    base_dir = './'
#文章からノイズを消す
RUBY_PATTERN = re.compile('　《.*?》')#るびの正規表現パターン
ADDITION_PATTERN = re.compile('[.*\]| 　　 （.*\'）')#文章中の補足情報のパターン
ALPHABET_PATTERN = re.compile('[a-zA-Z]')#アルファベットの正規表現バターン

def delete_newline_char(line):
    '''改行コードをすべて削除する'''
    return line.replace('\r', '').replace('\n','')

def remove_ruby(line):
    '''るびを削除する'''
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
        for sentence in line.split('。'):
            yield sentence

def preprocess(data):
    '''文章を前処理して文のリストにする'''
    lines = map(delete_newline_char, data)
    lines = map(remove_ruby, lines)
    lines = map(remove_additions, lines)
    lines = map(remove_escape_char, lines)
    lines = map(remove_symbols, lines)
    sentences = separate_line_with_puncs(lines)
    #'''文章がからのものを除去する'''
    sentences = filter(lambda  x: len(x), sentences)
    return list(sentences)

