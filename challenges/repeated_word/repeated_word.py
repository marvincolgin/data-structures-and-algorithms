import sys
sys.path.insert(0, '../../data-structures/hashtable')
sys.path.insert(0, '../../data-structures/linked_list')
from hashtable import HashTable  # noqa E402
import json  # noqa E402


def repeated_word(longstr: str) -> str:
    # search the longstr for complete words
    # return the first word that has more than
    # one occurrence
    # BigO Time==O(n) Space==O(n*1.3)

    # init our hash table
    ht = HashTable()

    # Convert string to lower-case for grouping same words
    longstr = longstr.lower()

    # Sanitize input and replace punctuation
    words = "".join((char if char.isalpha() else " ") for char in longstr).split()

    # iterate through all words
    for word in words:
        try:
            ht.add(word, 1)
        except ValueError:
            # first duplicate, this what we return
            return word

