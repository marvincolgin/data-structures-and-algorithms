import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir+'\\..\\data-structures\\stacks_and_queues')
p = parentdir+'\\..\\data-structures\\linked_list'
sys.path.insert(0,p)
sys.path.insert(0,p)
from stacks_and_queues import Queue
from enum import Enum


class AnimalType(Enum):
    CAT = 1
    DOG = 2

class Animal(object):

    def __init__(self, type : AnimalType):
        # create obj
        pass

    def serialize(self):
        # return json for obj
        pass

    @staticmethod
    def Factory(self, json : str): # -> Animal
        # create Animal class Dog|Cat for Json
        pass


class Cat(Animal):

    def __init__(self):
        # create obj
        # call super with CAT
        pass

class Dog(Animal):

    def __init__(self):
        # create obj
        # call super with DOG
        pass


class AnimalShelter():

    def __init__(self):
        # create internal data structs
        pass

    def enqueue(self, animal : Animal):
        # add animal to shelter
        pass

    def dequeue(self, pref : AnimalType=None) -> Animal:
        # grab animal that has been in queue the longest, optionally provide parameter
        pass
