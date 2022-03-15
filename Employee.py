from person import  *
from validateEmail import *
class Employee(Person):
    def __init__(self,name,money,mood,healthRate,id , car, email, salary, distanceToWork):
        super(Employee,self).__init__(name,money,mood,healthRate)
        self.id=id
        self.car=car
        self.email=email
        self.salary=salary
        self.distanceToWork=distanceToWork
        if validationEmail(email) != True:
            print("please enter a validate email")
        if salary < 1000:
            print("the salary must be 1000 LE or more")
        if healthRate <0 and healthRate >100:
            print("health rate should be between 0 and 100")


    def work(self,hours):
        if hours == 8:
            self.mood=Person.mood[0]
        elif hours < 8:
            self.mood=Person.mood[2]
        elif hours > 8:
            self.mood=Person.mood[1]
        else:
            print("invalid option")

    def  drive(self,distance,time):
        velocity=self.distanceToWork/time
        self.car.run(velocity,self.distanceToWork)

    def   refuel(self,gasAmount=100):
        self.car.refuel = gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        mail_lines = ["\nFrom: " + self.email, "\nTo: " + to, "\n", "\nHi " + receiver_name, "\n" + msg, "\n" + subject]
        fl = open("mails.txt", 'a')
        for ln in mail_lines:
            fl.write(ln)
        fl.close()



Employee("kholoud",234,"tired",75,1,"volvo","kholoud@gmail.com",21333,87)
print(Employee.mood[2])
