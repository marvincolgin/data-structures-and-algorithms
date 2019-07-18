import json
#from ll_merge import mergeList


# **********************************
class LinkNode():

    value = ''
    next = None
    prev = None

    def __init__(self, value, next=None, prev=None):
        # constructor
        self.value = value
        self.next = next
        self.prev = prev


# **********************************
class LinkList():

    head = None

    def __init__(self):
        # constructor
        self.head = None

    def toJSON(self):
        # dump object to JSON and return as String
        buf = json.dumps(self, default=lambda o: o.__dict__, indent=0, separators=(',', ': '))
        buf = buf.replace('\n', ' ').replace('\r', '')
        return buf

    def toStr(self):
        # dump list as simple text-list

        # c,cnt are limiters to make sure we don't go run away
        # yes, we need cnt=self.count() and not -1, as we walk off list
        c, cnt = 0, self.count()
        buf = ''
        ptr = self.head
        while ptr is not None:
            buf = buf + ptr.value + ','
            ptr = ptr.next
            c += 1
            if (c > cnt):
                raise AssertionError(f'WAIT!!! Forever Loop!\nRecursive LinkList/Node\nbuf:[{buf}]')

        if buf.endswith(','):
            buf = buf[:-1]
        return buf

    def insert(self, value):
        # insert value at the head of the list
        node = LinkNode(value, self.head)
        node.next = self.head
        self.head = node

    def includes(self, value):
        # traverse list and determine if a value exists
        # return bool
        ret = False
        cur = self.head
        while cur is not None:
            if cur.value == value:
                ret = True
                break
            cur = cur.next
        return ret

    def count(self):
        # count the number of nodes and return count
        cnt = 0
        cur = self.head
        while cur is not None:
            cnt += 1
            cur = cur.next
        return cnt

    def append(self, value):
        # adds a new node with the given value to the end of the list
        # BigO == O(n)

        # walk to end of list
        prev, cur = None, self.head
        while cur is not None:
            prev = cur
            cur = cur.next

        # create the node and add it to the end
        node = LinkNode(value, None)
        if (prev == None):
            self.head = node
        else:
            prev.next = node

        return True

    def insertBefore(self, targetVal: int, newVal: str, afterInstead=False):
        # add a new node with the given newValue immediately BEFORE the node containg targetVal
        # note: this bevahoir can be modified by the bool afterInstead
        # BigO == O(n)

        # walk the list to find it or the end
        found = False
        prev, cur = None, self.head
        while cur is not None:
            if cur.value == targetVal:
                found = True
                break
            prev = cur
            cur = cur.next

        # if found, put it in the chain, as a link right before the node containing value
        if found:
            node = LinkNode(newVal)
            if afterInstead:
                node.next = cur.next
                cur.next = node
            else:
                node.next = cur
                if prev is None:  # edge-case, if the targetVal is first node
                    self.head = node
                else:
                    prev.next = node

        return found

    def insertAfter(self, targetVal: int, newVal: str):
        # add a new node with the given newValue immediately AFTER the node containg targetVal
        # BigO == O(n)
        return self.insertBefore(targetVal, newVal, True)

    def kthFromEnd(self, k):
        # finds the Kth element from the end of the list and returns value for node
        # BigO == O(n)

        # Only positive integers
        if k < 0:
            raise AssertionError(f'WAIT!!! You must pass a positive integer, k:[{k}]')

        ptrA = self.head
        ptrB = self.head

        # Walk ptrA out to "K" elements
        tooSmall = False
        c = 0
        while c < k-1:
            if ptrA.next is None:
                tooSmall = True
                break
            ptrA = ptrA.next
            c += 1
        if tooSmall:
            raise AssertionError(f'WAIT!!! There are not enough elements in the link list for k:[{k}].')

        # Walk ptrA and ptrB out to the end of the list
        # ptrB will point to our requested node
        # note: for short lengths where the value is found before k elements, we are going to skip walking
        # ptrB until the difference between it and ptrA is "k"
        while ptrA.next is not None:
            ptrA = ptrA.next
            if c >= k:
                ptrB = ptrB.next
            c += 1

        return ptrB.value


    def mergeList(self, listA, listB):
        # Merge two lists
        # BigO == O(n)

        ptrA = listA.head
        ptrB = listB.head

        print(f'ptrA:[{ptrA}]')
        print(f'ptrB:[{ptrB}]')
        while ptrA is not None or ptrB is not None:
            print(f'ptrA.value:[{ptrA.value}]')
            print(f'ptrB.value:[{ptrB.value}]')
            if ptrA is not None:
                prev = ptrA
                ptrA = ptrA.next
                prev.next = ptrB
            if ptrB is not None:
                prev = ptrB
                ptrB = ptrB.next
                prev.next = ptrA

        return listA


if __name__ == "__main__":

    listA = LinkList()
    listA.append('apple')
    listA.append('bannana')
    listA.append('orange')

    listB = LinkList()
    listB.append('cheerios')
    listB.append('frosted flakes')
    listB.append('wheaties')

    expected = 'apple,cheerios,bannan,frosted flakes,orange,wheaties'
    listA.mergeList(listA, listB)
    actual = listA.toStr()

    print(f'actual:[{actual}]')
