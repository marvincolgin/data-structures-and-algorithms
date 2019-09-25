import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir+'\\..\\data-structures\\stacks_and_queues')
p = parentdir+'\\..\\data-structures\\linked_list'
sys.path.insert(0,p)
sys.path.insert(0,p)
from stacks_and_queues import Queue, Stack
from enum import IntEnum
import json


class AnimalType(IntEnum):
    UNKNOWN = 0
    CAT = 1
    DOG = 2


class Animal(object):

    animaltype = AnimalType.UNKNOWN

    def __init__(self, animaltype : AnimalType):
        # create obj
        self.animaltype = animaltype

    def serialize(self):
        # return json for obj
        return json.dumps(self.__dict__)

    @staticmethod
    def Factory(jsonstr : str): # -> Animal
        # create Animal class Dog|Cat for Json
        d = json.loads(jsonstr)

        if d['animaltype'] == AnimalType.CAT:
            obj = Animal(AnimalType.CAT)
        elif d['animaltype'] == AnimalType.DOG:
            obj = Animal(AnimalType.DOG)
        else:
            print('Bad JSON')
            return None

        return obj


class Cat(Animal):

    def __init__(self):
        # create obj
        # call super with CAT
        super().__init__(AnimalType.CAT)

class Dog(Animal):

    def __init__(self):
        # create obj
        # call super with DOG
        super().__init__(AnimalType.DOG)


class AnimalShelter():

    q = None  # Queue
    def __init__(self):
        # create internal data structs
        self.q = Queue()

    def enqueue(self, animal : Animal):
        # add animal to shelter
        self.q.enqueue(animal.serialize())

    def dequeue(self, pref : AnimalType=None) -> Animal:
        # grab animal that has been in queue the longest, optionally provide parameter

        # No Pref First
        if pref == None:
            b, val = self.q.peek()
            if not b:
                return None

            if self.q.dequeue(val):
                return Animal.Factory(val)
        else:
            stack = Stack()

            # Find the Animal we Want (deq, push to stack)
            found = False
            b, val = self.q.peek()
            while b:
                animal = Animal.Factory(val)
                if animal.animaltype == pref:
                    found = True
                    break
                stack.push(val)
                self.q.dequeue(val)

                b, val = self.q.peek()

            if found:

                # Pop off stack and enqueue back to queue
                # record the current count, as we need to cycle the enq (back of line) to the front
                c = self.q.count()
                b, val = stack.peek()
                while b:
                    val = stack.pop()
                    self.q.enqueue(val)

                    b, val = stack.peek()

                # cycle the back of the list to the front
                diff = self.q.count() - c
                for x in range(diff):
                    val = self.q.peek()
                    self.q.dequeue(val)
                    self.q.enqueue(val)

                return animal
            else:
                return None


