
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

    return arr
