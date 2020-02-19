class Animal(object):

    def drink(self):
        print("这是一个喝水的方法")
        pass

    def run(self):
        print("这是一个跑步的方法")
        pass

    def eat(self):
        print("这是一个吃饭的方法")
        pass

    def bark(self):
        print("这是一个喊叫的方法")
        pass


class Tiger(Animal):

    def __init__(self, name):
        self.name = name

    def run(self):
        print("%s 跑步,这是一只狗儿" % (self.name))

    def drink(self):
        print("%s 喝水,这是一只狗儿" % (self.name))

    def eat(self):
        print("%s 吃饭,这是一只狗儿" % (self.name))

    def bark(self):
        print("%s 喊叫,这是一只狗儿" % (self.name))


class Lion(Animal):

    def __init__(self, name):
        self.name = name

    def run(self):
        print("%s 跑步,这是一只猫儿" % (self.name))

    def bark(self):
        super().bark()  # super()方法可以返回一个父类的对象,可以用来在子类中调用父类方法
        print("%s 喊叫,这是一只猫儿" % (self.name))


class TigerLion(Lion, Tiger):

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':

    tiger1 = TigerLion("虎狮兽")

    tiger1.run()

