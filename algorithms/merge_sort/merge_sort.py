
def merge_array(arr, left, right: list) -> list:
    # combine left and right sides

    # counters for tracking the left and right side
    # and total data written
    leftCnt = rightCnt = totalCnt = 0

    # Loop thru data in left and right
    # since one side can have one more element
    # we are using two counters
    while leftCnt < len(left) and rightCnt < len(right):

        if left[leftCnt] < right[rightCnt]:

            arr[totalCnt] = left[leftCnt]
            leftCnt += 1

        else:

            arr[totalCnt] = right[rightCnt]
            rightCnt += 1

        totalCnt += 1

    # empty any remain from left and right
    while leftCnt < len(left):
        arr[totalCnt] = left[leftCnt]
        leftCnt += 1
        totalCnt += 1

    while rightCnt < len(right):
        arr[totalCnt] = right[rightCnt]
        rightCnt += 1
        totalCnt += 1

    return arr


def merge_split(arr: list) -> list:
    # actual merge_sort function, without error handling
    # :: recursivily called

    # base case to return
    if len(arr) > 1:

        # get middle point
        mid = len(arr) // 2

        # store a left/right side
        left = arr[:mid]
        right = arr[mid:]

        # recusively call ourselves
        merge_sort(left)
        merge_sort(right)

        # meat, this is actually performs the sort
        arr = merge_array(arr, left, right)

    return arr


def merge_sort(arr: list) -> list:
    # BigO (n log n)
    # :: log n, as this is a divide algo
    # :: n, as we need to merge the halfs back

    # 0 Elements: Exception
    if len(arr) == 0:
        raise Exception('No Elements')

    # 1 Element: Early Return
    if len(arr) == 1:
        return arr

    # call the actual merge_sort
    arr = merge_split(arr)

    return arr
