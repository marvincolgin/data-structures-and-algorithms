
def getIndex(data : list, ch : str) -> int:
    # getIndex from list of 'ch' element
    # but don't throw exception, just return -1
    try:
        return data.index(ch)
    except ValueError:
        return -1


def multi_bracket_validation(s : str) -> bool:
    # takes in a string and tests it to make sure that any open brackets ('{','(','[') are balanced with their corresponding closing-brackets ('}',')',']').
    # BigO == time(n) space(n)
    arr = []

    openBrackets = ['(', '[', '{']
    closeBrackets = [')', ']', '}']
    for ch in s:
        if ch in openBrackets:
            arr.append(ch)
        elif ch in closeBrackets:
            ch2 = arr.pop()

            i = getIndex(closeBrackets, ch)
            if openBrackets.index(ch2) != i:
                return False

    return len(arr) == 0
