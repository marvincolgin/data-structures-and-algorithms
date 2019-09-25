
def insertion_sort(arr):
    # BigO = O(2n)

    # 0 Elements: Exception
    if len(arr) == 0:
        raise Exception('No Elements')

    # 1 Element: Early Return
    if len(arr) == 1:
        return arr


    for i in range(len(arr)):

        # the value to be insertion-sorted
        val = arr[i]


        # Loop backwards, shuffling the values forward through the
        # array, starting at the current 'val' location -1
        j = i-1
        while j >= 0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1

        # insert the value into the sorted location
        arr[j+1] = val


    return arr
