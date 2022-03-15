
class Person:
    mood=("happy","tired","lazy")
    def __init__(self,name,money,mood,healthRate):
        self.name=name
        self.money=money
        self.mood=mood
        self.healthRate=healthRate

    def sleep(self,hours):
        if hours==7:
            self.mood=Person.mood[0]
        elif hours<7:
            self.mood=Person.mood[1]
        elif hours>7:
            self.mood=Person.mood[2]
        else:
            print("invalid option")

    def eat(self,meal):
        if meal == 3:
            self.healthRate=100
        elif meal == 2:
            self.healthRate=75
        elif meal == 1:
            self.healthRate=50

    def buy(self,items):
        self.money -= (items*10)


Person("kholoud",87,"happy",4)
# Person.sleep(self=7)
print(Person.mood[0])