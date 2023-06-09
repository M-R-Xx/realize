class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.color = None
        self.mileage = None

    def __str__(self):
        return f"{self.color} {self.make} {self.model} with {self.mileage} km"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make

    def set_model(self, model):
        self.car.model = model

    def set_color(self, color):
        self.car.color = color

    def set_mileage(self, mileage):
        self.car.mileage = mileage

    def get_result(self):
        return self.car


class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_basic_car(self):
        self.builder.set_make("Ford")
        self.builder.set_model("Focus")
        self.builder.set_color("blue")
        self.builder.set_mileage(0)

    def build_deluxe_car(self):
        self.builder.set_make("Toyota")
        self.builder.set_model("Camry")
        self.builder.set_color("red")
        self.builder.set_mileage(10000)


# Example usage
builder = CarBuilder()
director = CarDirector(builder)
director.build_basic_car()
car = builder.get_result()
print(car)

builder = CarBuilder()
director = CarDirector(builder)
director.build_deluxe_car()
car = builder.get_result()
print(car)