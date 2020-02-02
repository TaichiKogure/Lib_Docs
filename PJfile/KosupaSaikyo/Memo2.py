import pygame
from pygame.locals import *
import sys
import math
import random

class Agent:
    def __init__(self, x, y, vx, vy):
        self.x, self.y = x, y  # 位置
        self.vx, self.vy = vx, vy  # 速度

    def update(self, WINDOW_W, WINDOW_H):
        # 　位置に速度を足して移動する
        self.x += self.vx
        self.y += self.vy
        # ウィンドウの端で跳ね返るための処理
        if self.x > WINDOW_W:  # 右端
            self.vx, self.x = -self.vx, WINDOW_W
            return
        if self.x < 0:  # 左端
            self.vx, self.x = -self.vx, 0
            return
        if self.y > WINDOW_H:  # 下
            self.vy, self.y = -self.vy, WINDOW_H
            return
        if self.y < 0:  # 上
            self.vy, self.y = -self.vy, 0

    def draw(self, screen):
        x, y = int(self.x), int(self.y)
        # 小さな赤い丸を描く
        pygame.draw.circle(screen, (255, 100, 0), (x, y), 7)

# 分離のルール
    def separation(self,r_s):
        tvx = tvy = c = 0
        #自分以外の全エージェントを処理する
        for a in self.others:
# 近すぎるか？[1]は距離
        if a[1] < r_s and a[1] != 0:
# 離れる方向の単位ベクトルを蓄積



