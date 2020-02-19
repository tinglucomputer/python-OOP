

class HouseItem(object):

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "The houseitem is %s, the area is %.1f" % (self.name, self.area)


class House(object):

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.houseItem_list = []

    def __str__(self):
        return "The house\'s type is %s, the area is %0.1f" % (self.house_type, self.area)

    def insertItem(self, item):
        self.houseItem_list.append(item)

    def useArea(self):
        sum = 0.0
        if len(self.houseItem_list) > 0:
            for i in self.houseItem_list:
                sum += i.area
        return sum

    def printInfo(self):
        print("The house\'s type is %s, the total area is %0.2f, the unused area is %0.2f, "
              % (self.house_type, self.area, self.area - self.useArea()))
        print("The houseitem is")
        for i in self.houseItem_list:
            print(i.name)


if __name__ == '__main__':
    item1 = HouseItem("席梦思", 4)
    item2 = HouseItem("衣柜", 2)
    item3 = HouseItem("餐桌", 1.5)

    house = House("大", 10)

    print(house)

    house.insertItem(item1)

    house.insertItem(item2)

    house.insertItem(item3)

    house.printInfo()


