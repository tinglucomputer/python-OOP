class Cat():

    def __init__(self, name):   # 初始化方法,设置类中的变量
        self.name = name

    def drink(self):
        print("%s wants to drink" % self.name)

    def eat(self):
        print("%s wants to eat foods" % self.name)

    def __del__(self):  # 销毁方法,在删除对象之前自动调用
        print("%s is out of memory" % self.name)

    def __str__(self):  # print(instance)的结果是该对象的类和在内存中的地址,如果想输出自定义内容时,使用该函数
        return "Hello, I am %s" % self.name


tom = Cat("大懒猫")    # 实例化一个对象,自动调用__init__()初始化方法

tom.drink()
tom.eat()

print(tom)

del tom

