import math

class Heap():

   # Storage for Heap
   _data = []

   def __init__(self):
      _data = []

   def getRelativesIDX(self, idx: int) -> [int, int, int]:
      # for a given index into the heap: self
      left = (idx*2)
      right = (idx*2) + 1
      parent = math.trunc(idx/2)

      return [left, right, parent]
