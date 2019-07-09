"""
In the docs, the requirements of this function is to place the "val" in the literal middle of the arrray
However, the two example use sorted arrays, and I felt the need to go further
"""
def insert_shift_array(arr, val):
   new = []

   # Find location to insert
   c = 0
   found = False
   for x in arr:
      if arr[x-1] > val:
         found = True
         break
      c += 1

   if found:
      new.extend(arr[:c])
      new.append(val)
      new.extend(arr[c:])
      # I want this to work, but the return of Extend() doesn't seem to stay with the interpeter
      # AttributeError: 'NoneType' object has no attribute 'append'
      #new.extend(arr[:c]).append(val).extend(arr[c:])
   else:
      new = arr


   return new


arr = [1,2,4,6,7]
arr = insert_shift_array(arr, 5)
print(arr)

#arr = [1,3,4,7,9]
#arr = isa2(arr, 2)
#print(arr)
