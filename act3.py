#class parrot


class Parrot:
    species = "birds"
    def __init__(self, name, age):
        self.name = name
        self.age = age


chery = Parrot("Chery", 5)
tom = Parrot("Tom", 10)

print("Chery and Tom are",chery.species)
print("{} is {} years old".format( chery.name, chery.age))
print("{} is {} years old".format(tom.name, tom.age))
