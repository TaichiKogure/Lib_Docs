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
        you = int(self.flow_io.input())
        enemy = self.game.enemy_hand()
        self.flow_io.print(self.game.your_and_enemy_hand(you, enemy))
        result = self.game.judge4(you, enemy)
        self.flow_io.print(result)

game = Janken()
flow_io = systemIO()
flow4 = GameFlow(game, flow_io)
flow4.play()
