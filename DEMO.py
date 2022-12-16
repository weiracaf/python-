class Father():
    def bark(self):
        print("动物在叫")
    def drink(self):
        print("父类的drink")
class Son(Father):
    def bark(self):
        print("狗在叫")
f=Father()
s=Son()
s.bark()
s.drink()