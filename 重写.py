class Father(object):
    def play_game(self):
        print("父类中的play_game")

    def drink(self):
        print("父类中的drink方法")


class Son(Father):
    def play_game(self):  # 重写
        print("子类中的play_game")


father = Father()
father.play_game()  # 调用父类中的方法，因为对象是父类创建的

son = Son()
son.play_game()  # 调用子类中的方法，因为在子类中重写了play_game方法
son.drink()  # 调用父类中的方法，因为子类中并没有重写此方法
