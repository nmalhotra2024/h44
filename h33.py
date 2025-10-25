# cars.py

class BMW:
    def fuel_type(self):
        print("BMW uses Petrol.")

    def max_speed(self):
        print("BMW's maximum speed is 250 km/h.")


class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Premium Petrol.")

    def max_speed(self):
        print("Ferrari's maximum speed is 350 km/h.")

from cars import BMW, Ferrari

def car_details(car):
    """Function demonstrating polymorphism"""
    car.fuel_type()
    car.max_speed()

def main():
    bmw_car = BMW()
    ferrari_car = Ferrari()

    # List of car objects
    cars = [bmw_car, ferrari_car]

    for car in cars:
        car_details(car)
        print("-" * 30)

if __name__ == "__main__":
    main()