from random import choice

class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Bird:
    def speak(self):
        return "Tweet Tweet!"


def get_pet(pet="dog"):
    pet_factory = dict(dog=Dog(), cat=Cat(), bird=Bird())
    return pet_factory[pet]


# Example usage
d = get_pet("dog")
print(d.speak())
c = get_pet("cat")
print(c.speak())
b = get_pet("bird")
print(b.speak())