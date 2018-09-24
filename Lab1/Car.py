class Car:

    def __init__(self, power, brand, max_speed):
        self.power = power
        self.brand = brand
        self.max_speed = max_speed

    def __repr__(self):
        return "Power " + str(self.power) + ", brand " + self.brand + ", max speed " + str(self.max_speed)
