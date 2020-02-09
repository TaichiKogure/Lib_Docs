# %%
# じゃんけんプログラム　Janken Program
# 　クラスを使わないで書いた場合↓ Program not used "Class".
import random

hands = ['チョキ', 'パー', 'グー']
print("グー : 0 , チョキ: 1 , パー: 2")
you = int(input())
enemy = random.randint(0, 2)
print('あなた：{0},　相手：{1}'.format(hands[you], hands[enemy]))
result = (you - enemy) % 3

if result == 0:
    print("Draw")
elif result == 1:
    print("Lose")
else:
    print("win")

# %%
# Janken　Class　を使った場合

import random


class Janken:
    HANDS2 = ['チョキ', 'パー', 'グー']

    @classmethod
    def description(cls):
        print("グー : 0 , チョキ: 1 , パー: 2")

    @classmethod
    def your_and_enemy_hand(cls, you2, enemy2):
        print('あなた：{0},　相手：{1}'.format(cls.HANDS2[you2], cls.HANDS2[enemy2]))

    @classmethod
    def enemy_hand(cls):
        return random.randint(0, 2)

    @classmethod
    def judge(cls, you2, enemy2):
        result2 = (you2 - enemy2) % 3
        if result2 == 0:
            print("Draw")
        elif result2 == 1:
            print("Lose")
        else:
            print("win")


class GameFlow:
    @classmethod
    def play(cls):
        Janken.description()
        you2 = int(input())
        enemy2 = Janken.enemy_hand()
        Janken.your_and_enemy_hand(you2, enemy2)
        Janken.judge(you2, enemy2)


GameFlow.play()
