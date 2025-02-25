class dog:
    species = "Canine" # Class attribute

    def __init__(self, name , age):
        self.name = name # Instance attribute
        self.age = age  # Instance attribute

dog2 = dog("nanu",5)
print(dog2.name, dog2.age, dog2.species)


dog1 = dog("Budy",3)
print(dog1.name, dog1.age, dog1.species)
print(dog.species)