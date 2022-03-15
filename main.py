from car import Car
from Employee import Employee
# from Office import Office

kholoud= Employee("kholoud",12000,"Happy",100,1,"audi","kholoud@gmail.com",4000,40)
hasnaa= Employee("hasnaa",7000,"Tired",100,2,"volvo","hasnaa@gmail.com",3000,50)

kholoud.sleep(6)
print("-----> kholoud's mood:  ",kholoud.mood)
print("\n")
kholoud.work(8)
print("-----> kholoud's mood:  = ",kholoud.mood)
print("\n")
kholoud.buy(10)
print("-----> kholoud's money:  ",kholoud.money)
print("\n")
kholoud.eat(1)
print("-----> kholoud's health: ",kholoud.healthRate)

kholoud.send_mail("kholoud@gmail.com","Mail Test","Test Mail in Python Lab","hasnaa")