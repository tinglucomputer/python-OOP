class Dog(object):

    def drink(self):
        print("这是一个喝水的方法")
        pass

    def run(self):
        print("这是一个跑步的方法")
        pass


class XiaoTianQuan(Dog):

    count = 0   # 类属性,记录该类的实例化对象的个数

    def __init__(self, name):
        self.name = name
        XiaoTianQuan.count += 1

    def __str__(self):
        return "%s is a XiaoTianQuan" % (self.name)

    def bark(self):
        print("这是一个喊叫的方法1")

    @classmethod
    def bus(cls):   # 定义一个类方法,第一个参数是cls
        print("这是一个类方法")
        print("生成的对象数量是 %d" % cls.count)

    @staticmethod
    def sleep():    # 定义一个静态方法,不需要任何参数,不需要实例化对象调用,可以直接使用类名.方法名的形式调用
        pass


class QiuMingQuan(Dog):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "%s is a QiuMingQuan" % (self.name)

    def bark(self):
        print("这是一个喊叫的方法2")
        pass


def MultiState(dog):
    print(dog)


if __name__ == '__main__':
    dog1 = XiaoTianQuan("xiaoming")

    print(XiaoTianQuan.count)
    XiaoTianQuan.bus()

    dog2 = QiuMingQuan("xiaole")

    MultiState(dog1)

    MultiState(dog2)








