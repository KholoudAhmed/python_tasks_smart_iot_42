class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.__fuelRate = fuelRate
        self.__velocity = velocity


    def run(self, velocity, distance):
        self.__velocity = velocity
        for km in range(1, distance + 1, 10):
            self.__fuelRate -= (self.__fuelRate / 10)
            if (self.fuelRate < 0):
                self.fuelRate = 0
                self.stop(distance - km)
                break
        self.stop()


    def stop(self, remainDistance=0):
        self.__velocity = 0
        if (remainDistance == 0):
            print("---- > Reached to Destination")
        else:
            print("---- > Remain Distance = " + remainDistance)


    @property
    def velocity(self):
        return self.__velocity


    @velocity.setter
    def velocity(self, newVelocity):
        if (newVelocity > 0 and newVelocity <= 200):
            self.__velocity = newVelocity


    @property
    def fuelRate(self):
        return self.__fuelRate


    @fuelRate.setter
    def fuelRate(self, fuelValue):
        if (fuelValue > 0 and fuelValue <= 100):
            self.__fuelRate = fuelValue