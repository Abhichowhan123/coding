class pycharm:
    def execute(self):
        print("compiling")
        print("runing")

class myeditor:
    def execute(self):
        print("spell check") 
        print("convertion check")
        print("compiling")
        print("runing")
class laptop:
    def code(self,ide):
        ide.execute()


lap = laptop()
ide = myeditor()
lap.code(ide)