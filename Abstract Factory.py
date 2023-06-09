class Car:
    def get_info(self):
        return "A " + self.engine.type + " car with " + self.tires.brand + " tires."


class Engine:
    def __init__(self, type):
        self.type = type


class Tires:
    def __init__(self, brand):
        self.brand = brand


class CarFactory:
    def create_car(self):
        pass

    def create_engine(self):
        pass

    def create_tires(self):
        pass


class SportsCarFactory(CarFactory):
    def create_car(self):
        return Car()

    def create_engine(self):
        return Engine("V8")

    def create_tires(self):
        return Tires("Michelin")


class CityCarFactory(CarFactory):
    def create_car(self):
        return Car()

    def create_engine(self):
        return Engine("Inline Four")

    def create_tires(self):
        return Tires("Goodyear")


# Example usage
factory = SportsCarFactory()
engine = factory.create_engine()
tires = factory.create_tires()
car = factory.create_car()
car.engine = engine
car.tires = tires
print(car.get_info())

factory = CityCarFactory()
engine = factory.create_engine()
tires = factory.create_tires()
car = factory.create_car()
car.engine = engine
car.tires = tires
print(car.get_info())