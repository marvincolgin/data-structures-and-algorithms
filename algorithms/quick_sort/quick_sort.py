import random

def _partition(arr: list, start, end: int) -> int:

    # Start at the Start
    scout = wagon = start

    # Pick a pivot point (choose: first, end, middle)
    # @TODO: get fancy, pick 3 random ints from array
    # and use the middle value's index as pivot
    pivot = arr[end]

    # Continue until Scout is at end
    while scout < end:

        # is the value less-than pivot?
        if arr[scout] < pivot:

            # swap scout for wagon, vice versa
            arr[wagon], arr[scout] = arr[scout], arr[wagon]

            # adv wagon
            wagon += 1

        # move scout forward
        scout += 1

    # final swap
    arr[wagon], arr[end] = arr[end], arr[wagon]

    return wagon


def _quick_sort(arr: list, start, end: int) -> list:

    # are we overlapped? If so ,we are done, as it means
    # we have processed everything
    if start > end:
        return arr

    # Pick a point
    pos = _partition(arr, start, end)

    # Call ourselves again with the "left" and "right" side of pos
    _quick_sort(arr, start, pos-1)
    _quick_sort(arr, pos+1, end)


    return arr


def quick_sort(arr: list) -> list:
    # BigO (n log n)
    # :: log n, as this is a divide algo
    # :: n, as we need to merge the halfs back

    # 0 Elements: Exception
    if len(arr) == 0:
        raise Exception('No Elements')

    # 1 Element: Early Return
    if len(arr) == 1:
        return arr

    # Do It!!!!
    random.seed()
    arr = _quick_sort(arr, 0, len(arr)-1)

    return arr
