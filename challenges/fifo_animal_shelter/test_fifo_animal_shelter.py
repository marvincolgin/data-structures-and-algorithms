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

def test_shelter_create():
    shelter = AnimalShelter()

def test_shelter_enq_deq():
    shelter = AnimalShelter()
    shelter.enqueue(Animal(AnimalType.CAT))

    animal = shelter.dequeue()
    expected = '{"animaltype": 1}'
    actual = animal.serialize()
    assert actual == expected


def test_shelf_enq_lots():
    shelter = AnimalShelter()

    # Inc 10 (ALTERNATING)
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.DOG))
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.DOG))
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.DOG))
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.DOG))
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.DOG))

    # Deq 10
    for x in range(10):
        a = shelter.dequeue()

        actual= a.serialize()
        if x % 2 == 0:
            expected = '{"animaltype": 1}'
        else:
            expected = '{"animaltype": 2}'

        assert actual == expected

def test_shelf_deq_empty():
    # @TODO
    pass

