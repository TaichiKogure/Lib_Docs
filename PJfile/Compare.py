import pygame
from pygame.locals import *
import sys
import random

#Agent class
class Agent:
  def __init__(self, x, y, vx, vy):
    self.x, self.y = x, y # 位置
    self.vx, self.vy = vx, vy # 速度

  def update(self, WINDOW_W, WINDOW_H):
    # 位置に速度を足して移動する
    self.x += self.vx
    self.y += self.vy
    # ウインドウの端で跳ね返るための処理
    if self.x > WINDOW_W: # 右端
      self.vx, self.x = -self.vx, WINDOW_W
      return
    if self.x < 0: # 左端
      self.vx, self.x = -self.vx, 0
      return
    if self.y > WINDOW_H: # 下
      self.vy, self.y = -self.vy, WINDOW_H
      return
    if self.y < 0: # 上
      self.vy, self.y = -self.vy, 0
