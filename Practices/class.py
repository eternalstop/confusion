# coding=utf-8
class People(object):
    color = "yellow"

    def __init__(self, l):
        print ("Init...Test")
        self.where = "NanJing"

    def lover(self):
        print ("I am a Chiness,I am %s skin" % self.color)
        print ("I love Python!")


class Chiness(People):
    def __init__(self):
        super(Chiness, self).__init__('blue')
        People.__init__(self, 'Blue')

    def lover(self):
        print ("I love China!")


liang = Chiness()
print (liang.color)
liang.lover()
