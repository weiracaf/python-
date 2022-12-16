class Animal:
    name = "动物"
    def bark(self):
        print("动物叫")
    def he(self):
        print("动物喝")
class Dog(Animal):
    def bark(self):
        super().bark()  # super()，调用父类对象的bark方法
        print("狗叫")     # 重写与父类方法同名
class xiaogou(Dog,Animal):
    pass
wangcai = xiaogou()
wangcai.bark()
wangcai.he()
print(wangcai.name)     # 通过旺财的_class_找类中的name，找不到一直找父类
