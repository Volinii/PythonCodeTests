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

exe = ExeMaker()
exe.executor = Player()
exe.start_play()
exe.executor = Qq()
exe.start_play()

