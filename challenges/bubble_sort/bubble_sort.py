

def bubble_sort(arr):
    # BigO == n^2


    # 0 Elements: Exception
    if len(arr) == 0:
        raise Exception('No Elements')

    # 1 Element: Early Return
    if len(arr) == 1:
        return arr

    # vars for optimization
    numItems = len(arr)
    numPasses = 1
    sortMade = True

    # perform until no swaps made
    while sortMade:

        sortMade = False

        maxChecks = numItems-numPasses
        for x in range(maxChecks):

            if arr[x] > arr[x+1]:
                val = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = val
                sortMade = True

        numPasses += 1


    return arr
