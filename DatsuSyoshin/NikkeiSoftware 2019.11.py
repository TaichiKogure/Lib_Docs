# %%
############################################################
# じゃんけんプログラム　Janken Program
# 　クラスを使わないで書いた場合↓ Program not used "Class".
############################################################
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

####################################################################################################################
# Janken　Class　を使った場合,GameFlowのPlayメソッドがゲーム全体の流れになっている。
# 　ただじゃんけん以外のゲームにもGameFlowクラスを使おうと思ったら　Playメソッド中のJankenクラスを全部修正する必要が出てくる。
####################################################################################################################
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

# %%
###########################################################################
# GameFlow classからJankanを全部消して　代わりにgameっていう変数をつけた場合
###########################################################################
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


# %%
# Janken　Classの記載の仕方を更に改良して、print()の部分をやめて、Returnで返すようにした場合

import random

class Janken:
    HANDS = ['グー', 'チョキ', 'パー']

    def description1(self):
        return "グー：０、チョキ：１、パー：２"  # リターンで返すとPyhonコンソール以外だったとしても表示に使える。らしい。

    def your_and_enemy_hand(self, you4, enemy4):
        return 'あなた：{0}, 相手{1}'.format(self.HANDS[you4], self.HANDS[enemy4])

    def enemy_hand(self):
        return random.randint(0, len(self.HANDS) - 1)  # こうしておくと手数が増えても（じゃんけんルール拡張したゲームになったとしても）計算される

    def judge4(self, you4, enemy4):
        result = (you4 - enemy4) % len(self.HANDS)  # 上と同じく、こうしておくとじゃんけんルールの拡張になる。
        if result == 0:
            print('DRAW')
        elif result == 1:
            print('LOSE')
        else:
            print('WIN')


class systemIO:
    def print(self, message):
        print(message)

    def input(self):
        return input()


class GameFlow:
    def __init__(self, game, flow_io):
        self.game = game
        self.flow_io = flow_io

    def play(self):
        self.flow_io.print(self.game.description1())
        you4 = int(self.flow_io.input())
        enemy4 = self.game.enemy_hand()
        self.flow_io.print(self.game.your_and_enemy_hand(you4, enemy4))
        result = self.game.judge4(you4, enemy4)
        self.flow_io.print(result)

game = Janken()
flow_io = systemIO()
flow4 = GameFlow(game, flow_io)
flow4.play()


 # %%
