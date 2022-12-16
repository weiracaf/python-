# 常用魔术方法主要有四种，都是和类绑定的
class Dog:
    name = "狗"
    sex = "公"

    def __init__(self,name):
        print("init执行")
        self.name=name
        print(self.name)






dog1 = Dog("旺财")    # 这里输出，说明只要有对象的创建就会调用__init__方法，实例化对象两个操作创建对象和为对象初始化，这个init是随着对象初始化触发的
# 后一步的操作使的__init__方法执行,对应的self与创建的对象绑定

class Cat:
    def __new__(cls):       # 有一个cls new和类绑定创建对应的类的对象
        print("new 方法执行")
        return object.__new__(cls)     #特别注意这个return，这个return就是返回给新建对象的地址！，一般都是用aobject的__new__
cat = Cat()     # 这一步操作嗲用了__new__方法，说明这个ne是随着对象创建触发的，也就是上面说的两步的第一步，这个方法的主要的作用是分配对应类型的内存空间（一些默认属性_class_)
print(cat)


# __del__触发时机是对象呗系统回收时，是所有代码执行完后进行垃圾回收，每个对象也进行内存释放，调用对应的__del__，只要对应对象没有引用了，就触发del
class Cat:
    def __del__(self):
        print("del方法触发")
    def __str__(self):
        print("str方法触发")
        self.name= "猫"
        return "本类是"+self.name


cat = Cat()
print(cat)
# del cat   # 如果这条语句没有注释那么，del会在下面那一行代码前执行，因为删除后就没有引用去指向对象了，对应的对象无法调用就变成了垃圾
# 是自动回收，不是del触发的__del__方法，如果你把cat1=cat 那么只有把这两个都del才会触发对应类的__del__方法
print("这条语句输出后才有del触发，说明代码执行完才会del而不是创建对象的时候哦")

# __str__ 类似java的toString()
# 使print(对象名) 能够是我们想要看到的形式,最后的返回值才是输出的内容
# __str__中的语句一般是一些赋值操作，最后的return 是输出内容
