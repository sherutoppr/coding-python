class Dog:
    """ one of the object to be return """

    def speak(self):
        return "bhau!!"

    def __str__(self):
        return "dog"


class DogFactory:
    """A concrete factory"""

    def get_pet(self):
        """return a Dog objects"""
        return Dog()

    def get_food(self):
        """return a dog food object"""
        return "Dog Food!"


class Cat:
    """ one of the object to be return """

    def speak(self):
        return "meaw!!"

    def __str__(self):
        return "cat"


class CatFactory:
    """A concrete factory"""

    def get_pet(self):
        """return a Cat objects"""
        return Cat()

    def get_food(self):
        """return a cat food object"""
        return "Cat Food!"


class PetStore:
    """ abstract factory"""

    def __init__(self, pet_factory=None):
        self.pet_factory = pet_factory

    def show_pet(self):
        """utility method to display the detail of the object return by the concrete factory"""
        pet = self.pet_factory.get_pet()
        pet_food = self.pet_factory.get_food()

        print("our pet is {}".format(pet))
        print("our pet say hello by {}".format(pet.speak()))
        print("its food is {}".format(pet_food))


# create a concrete factory
# factory = DogFactory()
factory = CatFactory()

# create the abstract factory for the concrete factory
shop = PetStore(factory)

# utility method to display the detail of our object
shop.show_pet()