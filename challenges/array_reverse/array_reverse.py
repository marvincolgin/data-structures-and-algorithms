def reverse_array(orig):
   """
      Returns a list in reversed order
      Mutable?
   """
   new = []
   while len(orig) > 1:
      new.insert(0, orig[0])
      orig.pop(0)
   return new

def reverse_array2(orig):
   return orig[::-1]

arrOrig = [1,2,3,4,5]
arrNew = reverse_array2(arrOrig)
print(arrNew)