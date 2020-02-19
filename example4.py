class MusicPlayer(object):

    instance = None

    initFlag = False

    def __new__(cls, *args, **kwargs):  # 先为对象分配空间,返回一个内存引用给__init()__做初始化
        print("实例化一个对象")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if MusicPlayer.initFlag is False:
            print("播放器初始化")
            MusicPlayer.initFlag = True
        else:
            print("播放器已经初始化过,不再初始化")


if __name__ == '__main__':

    player1 = MusicPlayer()

    print(player1)

    player2 = MusicPlayer()

    print(player2)

