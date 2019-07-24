from fifo_animal_shelter import AnimalShelter, AnimalType, Animal, Cat, Dog

def test_class_exists():
    AnimalShelter()
    Animal(AnimalType.CAT)
    Cat()
    Dog()


def test_animal_serialize():
    # test DOG create/serialize
    a = Animal(AnimalType.CAT)
    actual = a.serialize()
    expected = '{"animaltype": 1}'
    assert actual == expected
    # test DOG create/serialize
    a = Animal(AnimalType.DOG)
    actual = a.serialize()
    expected = '{"animaltype": 2}'
    assert actual == expected

def test_animal_factory():
    serialdata = '{"animaltype": 1}'
    a = Animal.Factory(serialdata)
    actual = a.serialize()
    expected = serialdata
    assert actual == expected


