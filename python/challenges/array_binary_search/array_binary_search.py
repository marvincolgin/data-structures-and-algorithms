def array_binary_search(arr, val):

    start = 0
    end = len(arr)-1

    found = False
    limiter = 0  # THIS ISN'T NEEDED, BUT WHO LIKES INFINITE LOOPS?!?!?
    while start <= end or limiter > len(arr):
        mid = ((end - start) // 2) + start
        if arr[mid] == val:
            found = True
            break
        elif val < arr[mid]:
            end = mid-1
        elif val > arr[mid]:
            start = mid+1

        limiter += 1

    if found:
        return mid
    else:
        return -1
