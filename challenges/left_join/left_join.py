import sys
sys.path.insert(0, '../../data-structures/hashtable')
sys.path.insert(0, '../../data-structures/linked_list')
from hashtable import HashTable  # noqa E402
from link_list import LinkList  # noqa E402
import json  # noqa E402


def left_join(h1, h2: HashTable) -> list:
    # perform a left-join on h1 against h2
    # - returns a list of dict:{word,syntonym,antonym)
    # - BigO time==O(n) space==0(n)
    # -      worst: time==O(3n)

    # Validation: Exception
    if not h1 or not isinstance(h1, HashTable):
        raise ValueError('The first parameter must be a HashTable.')

    # Validation: Return Early
    if not h2 or not isinstance(h2, HashTable):
        return []

    # Return Value
    retval = []

    # Iterate over HashTable (BigO time==O(n))
    for x in range(len(h1._data)):

        # Validate there is data and it's a linklist
        if h1._data[x] and isinstance(h1._data[x], LinkList):

            # obtain an easy reference to the start of the link list
            cur = h1._data[x].head

            # while we haven't walked off link list onto None
            while cur:  # BigO worst time=O(n)

                # obtain the payload and break up into return vals
                payload1 = cur.value
                word = payload1['name']
                synonym = payload1['value']
                antonym = None

                # get word from corresponding hashtable (h2)
                try:
                    antonym = h2.get(word)  # BigO worst time=O(n)
                except ValueError:
                    # Swallow error, as it wasn't found in table
                    pass

                # dict: add to return
                # @TODO: Ask JB about a one-liner for this...
                retval.append({
                   'word': word,
                   'synonym': synonym,
                   'antonym': antonym
                })

                # adv to next in link list
                cur = cur.next

    # return list of dict
    return retval
