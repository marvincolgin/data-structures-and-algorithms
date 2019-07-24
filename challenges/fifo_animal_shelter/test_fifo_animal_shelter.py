from fifo_animal_shelter import AnimalShelter, AnimalType, Animal, Cat, Dog

def test_class_exists():
    AnimalShelter()
    Animal(AnimalType.CAT)
    Cat()
    Dog()

