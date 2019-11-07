import pytest
import random
from heap import Heap


def test_exists():
   assert Heap


def test_add_single():
   h = Heap()
   h.add(50)
   assert h._data[0] == 50


def test_get_data():
   h = Heap()
   h.add(50)
   actual = h.get_data()
   expected = [ 50 ]
   assert actual == expected


def test_len():
   h = Heap()
   h.add(50)
   actual = len(h)
   expected = 1
   assert actual == expected


def test_add_two():
   h = Heap()
   h.add(50)
   h.add(25)
   actual = h.get_data()
   expected = [ 50, 25 ]
   assert actual == expected


def test_add_three():
   h = Heap()
   h.add(50)
   h.add(25)
   h.add(75)
   actual = h.get_data()
   expected = [ 75, 50, 25 ]
   assert actual == expected


def test_add_four():
   h = Heap()
   h.add(50)
   h.add(25)
   h.add(75)
   h.add(15)
   actual = h.get_data()
   expected = [ 75, 50, 25, 15 ]
   assert actual == expected


def test_add_lots():

   uniq = set()

   for j in range(0, 6):

      while True:
         x = random.randint(1,200)
         if x not in uniq:
            uniq.add(x)
            break

   h = Heap()
   for val in uniq:
      h.add(val)

   actual = h.get_data()
   expected = sorted(uniq, reverse=True)

   assert actual == expected
