class Cat():
    def __new__(cls):
        print("cat类的__new__方法")
        return None
    def __init__(self):
        print("Cat的__init__方法")

class Person(object):   # new()方法构造一个类实例，并将该实例传递给自身的__init__()方法，即__init__()方法的self参数。
    __name = "名字"
    def __new__(cls,name, age):
        return object.__new__(cls)
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
b = Person("小明",18)



