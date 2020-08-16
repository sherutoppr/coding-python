class Bulb(object):
    TotalBulbCount = 0           # Class Variables

    def __init__(self):          # Constructor
        Bulb.TotalBulbCount += 1
        self.isOn = False         # Instance Variables

    @classmethod
    def getBulbCount(cls):         # Class Method
        return cls.TotalBulbCount

    def turnOn(self):             # Instance Method
        self.isOn = True

    def turnOff(self):             # Instance Method
        self.isOn = False
        
    def isOnFun(self):             # Instance Method
        return self.isOn


class BulbDemo(object):
    @classmethod
    def main(cls, args):
        b = Bulb()
        print( "bulb is on return : " , b.isOnFun())
        b.turnOn()
        print("bulb is on return : " , b.isOnFun())
        print(Bulb.getBulbCount())


if __name__ == '__main__':
    import sys
    BulbDemo.main(sys.argv)