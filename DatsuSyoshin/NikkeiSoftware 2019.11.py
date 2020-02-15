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
<<<<<<< HEAD
# Janken　Class　を使った場合,GameFlowのPlayメソッドがゲーム全体の流れになっている。
# 　ただじゃんけん以外のゲームにもGameFlowクラスを使おうと思ったら　Playメソッド中のJankenクラスを全部修正する必要が出てくる。
=======
# Janken　Class　を使った場合
>>>>>>> origin/master

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
<<<<<<< HEAD

# %%
# GameFlow classからJankanを全部消して　代わりにgameっていう変数をつけている。

import random


class Janken2:
    HANDS = ['グー', 'チョキ', 'パー']

    def description(self):
        print("グー：0,チョキ：１,パー:2")

    def your_and_enemy_hand(self, you3, enemy3):
        print('あなた：{0} , 相手：{1}'.format(self.HANDS[you3], self.HANDS[enemy3]))

    def enemy_hand(self):
        return random.randint(0, 2)

    def judge3(self, you3, enemy3):
        result3 = (you3 - enemy3) % 3
        if result3 == 0:
            print('DRAW')
        elif result3 == 1:
            print('LOSE')
        else:
            print('WIN')


class GameFlow:
    def __init__(self, game):
        self.game = game

    def play(self):
        self.game.description()
        you3 = int(input())
        enemy3 = self.game.enemy_hand()
        self.game.your_and_enemy_hand(you3, enemy3)
        self.game.judge3(you3, enemy3)


game = Janken2()
flow = GameFlow(game)
flow.play()
=======
>>>>>>> origin/master
