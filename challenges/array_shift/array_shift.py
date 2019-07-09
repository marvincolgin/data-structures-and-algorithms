def insert_shift_array_sorted(arr, val):
   """
   This function inserts a value in a sorted array, at it's numericly associated index
   """

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



def insert_shift_array(arr, val):
    """
    Insert value in the middle of an array
    """

    new = []

    c = len(arr) - (len(arr) // 2)

    new.extend(arr[:c])
    new.append(val)
    new.extend(arr[c:])

    return new


#arr = [1,2,4,6,7]
#arr = insert_shift_array(arr, 5)
#print(arr)

#arr = [1,3,4,7,9]
#arr = isa2(arr, 2)
#print(arr)
