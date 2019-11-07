import math
from typing import Any, Optional  # noqa 402

class Heap():

   # Storage for Heap
   _data = []

   def __init__(self):
      self._data = []

   def __len__(self):
      return len(self._data)


   def getRelativesIDX(self, idx: int) -> [int, int, int]:
      # for a given index into the heap: self
      left = (idx*2)
      right = (idx*2) + 1
      parent = math.trunc(idx/2)

      return [left, right, parent]


   def max_heapify(self):
      # we will heap-ify, bubble up the last element to the top

      print("** LEN:", len(self._data))

      # early return: we need more elements
      if len(self._data) < 2:
         return

      # Add was at end, so we are going to work with this last leaf node
      cur = len(self._data)-1

      # get indexes to realitives l=i*2 r=i*2+1 p=i/2
      l, r, parent = self.getRelativesIDX(cur)

      # debugging
      print("cur,parent:", cur, parent)
      print(self._data)

      # keep evaluating parent vs cur (child) value and swap
      while cur>0 and self._data[cur] > self._data[parent]:

         # swap
         print("swap: cur,parent", cur, parent)
         print(self._data)

         parent_val = self._data[parent]
         self._data[parent] = self._data[cur]
         self._data[cur] = parent_val

         print(self._data)


         # walk cur/parent "up the tree"
         cur = parent
         _, _, parent = self.getRelativesIDX(cur)
         print("cur,parent:", cur, parent)


   def add(self, value: Any) -> bool:
      self._data.append(value)
      self.max_heapify()
      return True


   def get_data(self) -> list:
      return self._data

