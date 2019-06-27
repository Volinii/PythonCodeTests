import random


class ExeMaker:
    def choice_executor(self, exec_name=None):
        self.executor = exec_name

    def start_play(self):
        self.executor.start()


class Player:
    def start(self):
        print('player')


class Qq:
    def start(self):
        print('qq')


def choice():
    return random.choice([Qq, Player])()

exe = ExeMaker()
exe.executor = Player()
exe.start_play()
exe.executor = choice()
print(exe.executor)
exe.start_play()
