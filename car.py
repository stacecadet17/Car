class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if(self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price:" + str(self.price)
        print "Speed:" + str(self.speed) + "mph"
        print "Fuel:" + str(self.fuel)
        print "Mileage:" + str(self.mileage) + "mpg"
        print "Tax:" + str(self.tax)
        return self

car1 = Car(2000, 35, "full", 15)
car2 = Car(2000, 5, "not full", 105)
car3 = Car(2000, 15, "kind of full", 95)
car4 = Car(6000, 25, "full", 25)
car5 = Car(9000, 45, "Empty", 25)
car6 = Car(200000, 35, "Empty", 15)

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
