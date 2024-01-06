# WRITE YOUR SOLUTION HERE:

class Car:
    def __init__(self):
        self.__amt_petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__amt_petrol = 60

    def drive(self,km:int):

        if km <= self.__amt_petrol:
            distance_possible = km
        else:
            distance_possible = self.__amt_petrol
        
        self.__amt_petrol -= distance_possible  # Reduces petrol based on distance traveled
        self.__odometer += distance_possible

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__amt_petrol} litres"

if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
