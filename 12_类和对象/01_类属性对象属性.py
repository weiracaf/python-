import statistics


class Dog:
    leg = 4
    eye = 2
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):  # self代表和对象绑定（可以改名），最少包含一个参数self,实例方法只能通过实例化对象调用
        print(f"{Dog.leg}条腿，{Dog.eye}个眼睛")  # self就是调用对应对象的属性，而用类名的话就是对应类属性

    @classmethod  # 类方法前缀，可通过类名或者实例化对象调用
    def func(cls):  # 也是最少包含最少一个参数，与类绑定
        print("正在调用类方法", cls)
        print(cls.leg)
    @staticmethod
    def jingtai(name):
        print("我是静态方法不和任何类的对象绑定，也不能使用他们的东西奥,不过我可以有自己的参数比如")
        print(name)

# wangcai = Dog()
# wangcai.leg = 6
# wangcai.eye = 6
# wangcai.speak()
# wangcai.func()
# Dog.func()
# Dog.jingtai(666)    # 可以通过类和对象调用对应类里的静态方法
# wangcai.jingtai(777)
dog1 = Dog("好狗", 3)
dog2 = Dog("坏狗", 2)
dog1.sex="公"    # 动态绑定属性（就是类外建的属性），与对象绑定！
print(dog1.sex,dog1.name,dog1.age)
def bark():
    print("汪汪汪")
dog2.bark=bark  # 动态绑定方法，相当于在外面创建个方法和对象绑定
dog2.bark()     # 调用成功

