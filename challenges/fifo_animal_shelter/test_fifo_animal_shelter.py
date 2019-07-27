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


def helper_shelter_enq10():
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

    return shelter


def test_shelter_enq_lots():

    shelter = helper_shelter_enq10()

    # Deq 10
    for x in range(10):
        a = shelter.dequeue()

        actual= a.serialize()
        if x % 2 == 0:
            expected = '{"animaltype": 1}'
        else:
            expected = '{"animaltype": 2}'

        assert actual == expected


def test_shelter_deq_empty():
    shelter = helper_shelter_enq10()

    # Deq 10
    for x in range(10):
        shelter.dequeue()

    # Deq EMPTY
    expected = None
    actual = shelter.dequeue()
    assert expected == actual

def test_shelter_deq_pref_found():
    shelter = AnimalShelter()

    # Inc 10 (ALTERNATING)
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.DOG))
    shelter.enqueue(Animal(AnimalType.DOG))

    animal = shelter.dequeue(AnimalType.DOG)
    actual = animal.serialize()
    expected = '{"animaltype": 2}'
    assert actual == expected

def test_shelter_deq_pref_notfound():
    shelter = AnimalShelter()

    # Inc 10 (ALTERNATING)
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.CAT))

    actual = shelter.dequeue(AnimalType.DOG)
    expected = None
    assert actual == expected
