Data Structures and Algorithms

Written in Python/Golang

Vin Colgin Summer 2019


Table of Contents:
<!--ts-->
   * [Data Structures](#data-structures)
      * [Singly Linked Lists](#singly-linked-lists)
         * [API: Python](#api-python)
         * [API: Golang](#api-golang)
         * [Whiteboards](#whiteboards)
      * [Stack (LIFO)](#stack-lifo)
         * [API: Python](#api-python-1)
         * [API: Golang](#api-golang-1)
      * [Queue (FIFO)](#queue-fifo)
         * [API: Python using Link-List](#api-python-using-link-list)
         * [API: Python using Stack](#api-python-using-stack)
      * [Binary Tree (BT)](#binary-tree-bt)
         * [API](#api)
      * [Binary Search Tree (BST)](#binary-search-tree-bst)
         * [API](#api-1)
      * [Hash Table](#hash-table)
         * [API](#api-2)
      * [Graphs](#graphs)
         * [API](#api-3)
         * [Whiteboard](#whiteboard)
         * [Challenges](#challenges)
            * [Get Graph Edges](#get-graph-edges)
            * [API](#api-4)
            * [Whiteboard](#whiteboard-1)
         * [Depth-First Traversal](#depth-first-traversal)
            * [API](#api-5)
   * [Challenges](#challenges-1)
      * [Array: Reverse](#array-reverse)
         * [Source: Python](#source-python)
         * [Whiteboard](#whiteboard-2)
      * [Array: Insert and Shift](#array-insert-and-shift)
         * [Source: Python](#source-python-1)
         * [Whiteboard](#whiteboard-3)
      * [Array: Binary Search](#array-binary-search)
         * [Source: Python](#source-python-2)
         * [Whiteboard](#whiteboard-4)
      * [Queue: Animal Shelter](#queue-animal-shelter)
         * [API](#api-6)
         * [Whiteboard](#whiteboard-5)
      * [Stack: Balanced Brackets](#stack-balanced-brackets)
         * [API](#api-7)
         * [Whiteboard](#whiteboard-6)
      * [BinaryTree: Breadth-first Traversal](#binarytree-breadth-first-traversal)
         * [API](#api-8)
         * [whiteboard](#whiteboard-7)
      * [BinaryTree: Find the Maximum Value](#binarytree-find-the-maximum-value)
         * [API](#api-9)
         * [Whiteboard](#whiteboard-8)
      * [BinaryTree: FizzBuzzTree](#binarytree-fizzbuzztree)
         * [API](#api-10)
         * [whiteboard](#whiteboard-9)
      * [Hash Table: Repeated Words](#hash-table-repeated-words)
         * [API](#api-11)
         * [Whiteboard](#whiteboard-10)
      * [Binary Tree: Tree Intersection](#binary-tree-tree-intersection)
         * [API](#api-12)
         * [Whiteboard](#whiteboard-11)
      * [Hash Table: Left Join](#hash-table-left-join)
         * [API](#api-13)
         * [Whiteboard](#whiteboard-12)
   * [Algorithms](#algorithms)
      * [Bubble Sort](#bubble-sort)
         * [API](#api-14)
      * [Insertion Sort](#insertion-sort)
         * [API](#api-15)
      * [Merge Sort](#merge-sort)
         * [API](#api-16)
      * [Quick Sort](#quick-sort)
         * [API](#api-17)

<!-- Added by: mmc, at: Thu Sep 19 14:47:11 PDT 2019 -->

<!--te-->


<!-- ********************* -->
<!-- ********************* -->

# Data Structures

## Singly Linked Lists
Linked-Lists (singly) are dynamic data-structures which resembles a length of chain, where the entire length of chain is the list and the individual links of the chain are nodes. A singlarly linked list is only traversable in one direction, but utilizing a head element that points to the first node in the list, the second node in the list points to the next link in the chain, and finally the last element in the list points to "none"

### API: Python
<a href="https://github.com/marvincolgin/data-structures-and-algorithms/blob/master/data-structures/linked_list/link_list.py">Source Code</a>
```python
class LinkList()

    def __init__(self):
        # constructor

    def toJSON(self):
        # dump object to JSON and return as String

    def insert(self, value):
        # insert value at the head of the list

    def includes(self, value):
        # traverse list and determine if a value exists
        # return bool

    def count(self):
        # count the number of nodes and return count

    def append(value):
        # adds a new node with the given value to the end of the list
        # BigO == O(n)

    def insertBefore(value, newVal):
        # add a new node with the given newValue immediately before the first value node
        # BigO == O(n)

    def insertAfter(value, newVal):
        # add a new node with the given newValue immediately after the first value node
        # BigO == O(n)

class ListNode()
    def __init__(self, value, next=None, prev=None):
         # constructor
```
### API: Golang
<a href="https://github.com/marvincolgin/data-structures-and-algorithms/tree/master/golang/src/linklist">Source Code</a>
```golang
type LinkNode struct {
    value interface{}
	next  *LinkNode
	prev  *LinkNode
}
func (node *LinkNode) Init(value interface{}) {
    head *LinkNode
	// @TODO: comparison_func func
}

type LinkList struct {
	head *LinkNode
	// @TODO: comparison_func func
}
func (list *LinkList) Init()
func (list *LinkList) toJSON() string
func (list *LinkList) toStr() string
func (list *LinkList) Insert(value interface{}) bool
func (list *LinkList) Includes(value interface{}) bool
func (list *LinkList) Get(value interface{}) interface{}
func (list *LinkList) Count() int
func (list *LinkList) Append(value interface{}) bool
func (list *LinkList) Remove(value interface{}) bool
func (list *LinkList) Peek() (bool, interface{})
func (list *LinkList) InsertBefore(targetVal, newVal interface{}, afterInstead bool) bool
func (list *LinkList) InsertAfter(targetVal, newVal interface{}) bool
func (list *LinkList) KthFromEnd(k int) (bool, interface{})
func (list *LinkList) MergeList(listA, listB LinkList) LinkList

```

### Whiteboards
*Insert()*
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/master/data-structures/linked_list/assets/linked_lists-ll_insertions-whiteboard.jpg)
*KthFromEnd(): Iterative Approach*
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/master/data-structures/linked_list/assets/ll_kth_from_end-whiteboard.jpg)
*KthFromEnd(): Recursive Approach*
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/master/data-structures/linked_list/assets/ll_kth_from_end-whiteboard-recursive.jpg)
*MergeList()*
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/master/data-structures/linked_list/assets/ll_merge-whiteboard.jpg)


## Stack (LIFO)

### API: Python
```python
class Stack():
    def push(val) -> bool:
    def pop() -> str:
    def peek() -> str:
```
### API: Golang
<a href="https://github.com/marvincolgin/data-structures-and-algorithms/tree/master/golang/src/linklist">Source Code</a>
``` golang
// Stack implementation of LIFO
type Stack struct {
	_data linklist.LinkList
}

func (stack *Stack) Init()
func (stack *Stack) Count() int
func (stack *Stack) Pop() (bool, interface{})
func (stack *Stack) Push(val interface{}) bool
func (stack *Stack) Peek() (bool, interface{})
```

*Tests*
- [x] push onto a stack
- [x] push multiple values onto a stack
- [x] pop off the stack
- [x] empty a stack after multiple pops
- [x] peek the next item on the stack
- [x] instantiate an empty stack


## Queue (FIFO)
### API: Python using Link-List
```python
class Queue():

    def enqueue(val) -> bool:
        # Add a value to the queue

    def dequeue(val) -> bool:
        # Remove entry from queue with a given value

    def peek() -> str:
        # Get value from the head of the queue (without removing it)
```
*Tests*
- [x] enqueue into a queue
- [x] enqueue multiple values into a queue
- [x] dequeue out of a queue the expected value
- [x] peek into a queue, seeing the expected value
- [x] empty a queue after multiple dequeues
- [x] instantiate an empty queue

### API: Python using Stack
```python
class PseudoQueue(object):

    def __init__(self):
        # create Stack for internal data-struct

    def count(self):
        # pass through method to underlying data struct
        # BigO == O(n)

    def enqueue(self, val: str) -> bool:
        # enqeue a value at the end queue
        # BigO == O(1)

    def dequeue(self) -> (str, bool):
        # dequeue from head of queue
        # BigO == O(n)
        # Algo: use a second stack, as we need the bottom element on the first stack
        # so we are going to unload the first stack, into a temp stack, in order to
        # get at the bottom element of the first, then rebuild it from temp to first-stack
```
*Tests*
- [x] class existence
- [x] enqueue multiple items
- [x] dequeue item
- [x] dequeue multiple items
- [x] dequeue all until empty

*Whiteboard*
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/1805a3f00421d5f5f4bc5578e9cfc4522d47e9ba/challenges/queue_with_stacks/assets/whiteboard.jpg)


<!-- ********************* -->
## Binary Tree (BT)
### API
```python
class TraverseMethod(IntEnum):
    # enum class for traversal and processing order

class Node:
    # class for nodes within Tree

    def __init__(self, value):
        # constructor for creating Node

class BinaryTree:

    def __init__(self):
        # constructor for creating BinaryTree

    def traverse(self, method : TraverseMethod, action_func):
        # visit each node in atree, using a specified method and call action_func() for each node

        def _visit(node):
            # recusive function for visiting each node

    def returnAsArr(self, method : TraverseMethod):
        # return the enter tree as an array using a specified method
```

## Binary Search Tree (BST)
### API
```python
class BinarySearchTree(BinaryTree):
    # class for binary-search-tree

    def add(self, new_value):
        # adds new value to the tree

        def _find_and_insert(node):
            # recursive method for evaluating a node and calling itself depending on the value

    def contains(self, target_value) -> bool:
        # accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

        def _visit(node):
            # recursive function for isiting each node
```
*Tests*
- [x] instantiate an empty tree
- [x] instantiate a tree with a single root node
- [x] add a left child and right child to a single root node
- [x] return a collection from a preorder traversal
- [x] return a collection from an inorder traversal
- [x] return a collection from a postorder traversal

*Whiteboard*
None

<!-- ********************* -->
##  Hash Table
- [x] Implement Hash Table
- [x] TESTS
- [x] Docs
### API
```python
class HashTable():

    def __init__(self, hashtableSize = 1024):
        # create with hashTableSize

    def _makePayload(self, name, value):
        # return dict of name/value pair

    def _makeHash(self, name) -> int:
        # create a hash based on the name to be added to hashtable
        # this is a silly hash, as it's just for experiment and
        # gives us the ability to easily create collisions. Live
        # code should use something more sophisticated

    def _getHashIndex(self, hash: int) -> int:
        # get the index into the hash-table for a given hash value

    def _hashtable_compare_func(self, payload1, payload2) -> bool:
        # func passed to LinkList compare

    def add(self, name, value):
        # accepts name/value pair and adds them to the hashtable
        # if there are collisions, then they will be handled
        # by using a linked-list

    def get(self, name):
        # returns value in hashtable for a given name
        # if the value is not found, and exception will be raised

    def contains(self, name) -> bool:
        # returns true|false if the name is in the hashtable
```
*Tests*
- [x] add
- [x] contains
- [x] not-contains
- [x] hash deterministic
- [x] hash in range
- [x] hash diff value for diff keys
- [x] collisions


<!-- ********************* -->
<!-- ********************* -->


## Graphs
*Features*
- [x] Add Vertex
- [x] Add Edge
- [x] Get Neighbors
- [x] Get Vertexes
- [x] Get Length
### API
```python
class Vertex:
    def __init__(self, value: Any):

class Edge:
    def __init__(self, vertex: Vertex, weight=0):

class Graph:
    def __init__(self):
    def __len__(self) -> int:
    def add_vertex(self, value) -> Vertex:
    def add_edge(self, vert1: Vertex, vert2: Vertex, weight=0.0):
    def get_neighbors(self, vertex: Vertex) -> List[Edge]:
    def get_vertexes(self) -> Optional[List[Vertex]]:
    def breadth_first(self, root, action_func):
```
*Tests*
- [x] Node can be successfully added to the graph
- [x] An edge can be successfully added to the graph
- [x] A collection of all nodes can be properly retrieved from the graph
- [x] All appropriate neighbors can be retrieved from the graph
- [x] Neighbors are returned with the weight between nodes included
- [x] The proper size is returned, representing the number of nodes in the graph
- [x] A graph with only one node and edge can be properly returned
- [x] An empty graph properly returns null

### Whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/graph-day2/data-structures/graph/assets/whiteboard.jpg)

### Challenges

#### Get Graph Edges
Overall: Identify if a given path exists through the Graph where path is a given list of values
Use Case: Given a complete Graph data-structure, containing a variety of Vertexes/Edges containing city-names and costs, (Flight Routes) and a list of cities (Flight Plan), return True|False if the flight-plan can be performed and the cost.
- [x] Function
- [x] Docs
- [x] Tests
#### API
```python
def get_edges(graph: Graph, path_ro: List) -> Tuple[bool, float]:
    # identify if a given path exists through the Graph
    # where path is a given list of values
    # @path_ro will be treated as read-only
    # BigO time==O(V+P*E) .. where p is len(path_ro)
    # BigO space==O(1)
```
*Tests*
- [x] Invalid Input: Graph
- [x] Invalid Input: List
- [x] Flight-Plan with valid Flight-Route
- [x] Flight-Plan with invalid Flight-Route

#### Whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/get-edges/challenges/get_edges/assets/whiteboard.jpg)


<!-- ********************* -->
### Depth-First Traversal
- [x] breadth first traversal method which takes a Binary Tree as its unique input.
- [x] print every node encountered
#### API
```python
def depth_first_recursive(self, root: Vertex, action_func: Any) -> None:
def depth_first(self, root: Vertex, action_func: Any) -> None:
```
*Tests*
- [x] empty tree
- [x] null tree object
- [x] tree of nodes



<!-- ********************* -->
<!-- ********************* -->
# Challenges


<!-- ********************* -->
## Array: Reverse
Create a function, which reverses an array/linked-list, as passed via a parameter and pass the new array back as the `return()` for the function.
*Approach & Efficiency*
My initial approach was to utilize the `list.insert()` and `list.pop()` to rebuild the list in reverse order. However, my white boarding partner showed me a more pythonic method utilizing slices with a -1 stride.
*Solution*
Two solutions were used, one that utilizes a while() loop and is destructive on the inbound array. The second is "pythonic" and utilizes an index slice and a -1 stride.
### Source: Python
<a href="https://github.com/marvincolgin/data-structures-and-algorithms/blob/master/challenges/array_reverse/array_reverse.py">Source Code</a>
```python
def reverse_array(orig):
   """
      Returns a list in reversed order
      Mutable?
   """
   new = []
   while len(orig) > 1:
      new.insert(0, orig[0])
      orig.pop(0)
   return new

def reverse_array2(orig):
   return orig[::-1]

arrOrig = [1,2,3,4,5]
arrNew = reverse_array2(arrOrig)
print(arrNew)
```
### Whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/master/challenges/array_reverse/assets/whiteboard.jpg)


<!-- ********************* -->
## Array: Insert and Shift
Write a function which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.
*Solution*
Create an index into the array where the value will be inserted, utilize slice and .append/.extend to construct a return array
### Source: Python
<a href="https://github.com/marvincolgin/data-structures-and-algorithms/blob/master/challenges/array_shift/array_shift.py">Source Code</a>
### Whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/master/challenges/array_shift/assets/whiteboard.jpg)


<!-- ********************* -->
## Array: Binary Search
Write a function which takes in an array and the value to be searched. Return -1 if the value is not found, otherwise return the index (0 based). Incoming array is sorted.
*Solution*
Divide and Conquer! Look at the middle element, is it the middle element? Return. If not, create a new middle from either the smaller side or larger side. Repeat.
### Source: Python
<a href="https://github.com/marvincolgin/data-structures-and-algorithms/blob/master/challenges/array_binary_search/array_binary_search.py">Source Code</a>
### Whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/master/challenges/array_binary_search/assets/whiteboard.jpg)


<!-- ********************* -->
## Queue: Animal Shelter
create a class called AnimalShelter which holds only dogs/cats. The shelter operates as first-in / first-out
### API
```python
class AnimalType(IntEnum):

class Animal(object):

    def __init__(self, animaltype : AnimalType):
        # create internal data structs

    def serialize(self):
        # return json for obj

    def Factory(jsonstr : str): # -> Animal
        # create Animal class Dog|Cat for Json

class Cat(Animal):
    def __init__(self):
        # create internal data structs

class Dog(Animal):
    def __init__(self):
        # create internal data structs

class AnimalShelter():
    def __init__(self):
        # create internal data structs

    def enqueue(self, animal : Animal):
        # add animal to shelter

    def dequeue(self, pref : AnimalType=None) -> Animal:
        # grab animal that has been in queue the longest, optionally provide parameter
```
*Tests*
- [x] class existence
- [x] enq one
- [x] enq many
- [x] deq one (no pref)
- [x] deq one (with pref)
- [x] deq until empty

### Whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/master/challenges/fifo_animal_shelter/assets/whiteboard.jpg)


<!-- ********************* -->
## Stack: Balanced Brackets
Create a function, which takes in a string and tests it to make sure that any open brackets ('{','(','[') are balanced with their corresponding closing-brackets ('}',')',']').
### API
```python
def multi_bracket_validation(input : str) -> boolean:
```
*Tests*
- [x] Balanced
- [x] Balanced Complicated
- [x] Balanced extra characters
- [x] Balanced nested
- [x] Balanced alternating
- [x] Unbalanced
- [x] Only Open
- [x] Only Closed
- [x] Empty

### Whiteboard
![alt_text](https://github.com/marvincolgin/data-structures-and-algorithms/raw/multi_bracket_validation/challenges/multi_bracket_validation/assets/whiteboard.jpg)

<!-- ********************* -->
## BinaryTree: Breadth-first Traversal
- [x] breadth first traversal method which takes a Binary Tree as its unique input.
- [x] print every node encountered
### API
```python
def breadth_first(tree, action_func):
```
*Tests*
- [x] empty tree
- [x] null tree object
- [x] tree of nodes

### whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/breadth_first/challenges/breadth_first/assets/whiteboard.jpg)


<!-- ********************* -->
## BinaryTree: Find the Maximum Value
- [x] function called find_maximum_value which takes binary tree as its only input
### API
```python
def find_max(tree : BinaryTree) -> (bool,int):
```
*Tests*
- [x] find max
- [x] empty tree
- [x] tree == None

### Whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/c7e136b9fcf6c8522eb6d74643e65a4b8fb83c4e/challenges/find_maximum_binary_tree/assets/whiteboard.jpg)


<!-- ********************* -->
## BinaryTree: FizzBuzzTree
Write a function called FizzBuzzTree which takes a tree as an argument.
Determine weather or not the value of each node is divisible by 3, 5 or both, and change the value of each of the nodes:
- [x] value is divisible by 3, replace the value with "Fizz"
- [x] value is divisible by 5, replace the value with "Buzz"
- [x] value is divisible by 3 and 5, replace the value with "FizzBuzz"
- [x] Return the tree with its new values.
### API
```python
def fizzBuzzTree(tree: BinaryTree) -> BinaryTree:
    # traverse tree, value = value%3==0 ? 'Fizz, value = value%5==0 ? 'Buzz' (set value to 'FizzBuzz' if both conditions met)
```
*Tests*
- [x] empty tree
- [x] None that trigger
- [x] All that trigger FizzBuzz

### whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/be06edcb4417bd0d1a66896bb24b9339ac6ea962/challenges/fizz_buzz_tree/assets/whiteboard.jpg)


<!-- ********************* -->
## Hash Table: Repeated Words
repeated_words(): search the longstr for complete words, return the first word that has more than one occurrence
- [x] Branch Created
- [x] Function Created
- [x] Tests
- [x] Docs
### API
```python
def repeated_word(longstr: str) -> str:
    # search the longstr for complete words
    # return the first word that has more than
    # one occurrence
    # BigO Time==O(n) Space==O(n*1.3)
```
*Tests*
- [x] Sample Text #1
- [x] Sample Text #2
- [x] Sample Text #3

### Whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/repeated_word/challenges/repeated_word/assets/whiteboard.jpg)


<!-- ********************* -->
## Binary Tree: Tree Intersection
tree_intersection(): given two binary-trees, return an array containing shared values
- [x] Branch Created
- [x] Function Created
- [x] Tests
- [x] Docs
- [x] Pep8 Code Styling
### API
```python
def tree_intersection(tree1, tree2: BinaryTree) -> list:
    # return an array with all the values in both tree1 and tree2
    # BigO Time==O(2n)  Space==0(1.3n) 30% for hashtable
    # assumption: No Duplicates within Trees
```
*Tests*
- [x] Func / Empty Trees
- [x] Invalid Params
- [x] All Matches
- [x] No Matches
- [x] Some Matching

### Whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/tree_intersection/challenges/tree_intersection/assets/whiteboard.jpg)


<!-- ********************* -->
## Hash Table: Left Join
left_join(): given two hash-tables, return a list of all items from the first h1 and the value that exists in h2, if no value exists return None
- [x] LEFT JOINs two hashmaps into a single data structure.
- [x] 1st param is hashmap with words and synonyms
- [x] 2nd param is hashmap with words and antonyms
- [x] Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
- [X] Code Styling: PEP8
### API
```python
def left_join(h1, h2: HashTable) -> list:
    # perform a left-join on h1 against h2
    # - returns a list of dict:{word,syntonym,antonym)
    # - BigO time==O(n) space==0(n)
    # -      worst: time==O(3n)
```
*Tests*
- [x] Func / Input Validation
- [x] 2 rec, 1 with value in 2nd hashtable
- [x] Full Sample

### Whiteboard
![alt_text](https://raw.githubusercontent.com/marvincolgin/data-structures-and-algorithms/left_join/challenges/left_join/assets/whiteboard.jpg)




# Algorithms


<!-- ********************* -->
## Bubble Sort
- [x] code sort func
- [x] tests
- [x] blog post
### API
```python
def bubble_sort(arr):
    # BigO == n^2
```
*Tests*
- [x] func exists
- [x] sort 5
- [x] all same
- [x] sort zero array
- [x] sort 1000 random


<!-- ********************* -->
## Insertion Sort
- [x] code sort func
- [x] tests
- [x] blog post
### API
```python
def insertion_sort(arr):
    # BigO = O(2n)
```
*Tests*
- [x] func exists
- [x] sort 5
- [x] all same
- [x] sort zero array
- [x] sort 1000 random


<!-- ********************* -->
## Merge Sort
- [x] code sort func
- [x] tests
- [x] blog post
### API
```python
def merge_sort(arr):
    # BigO (n log n)
    # :: log n, as this is a divide algo
    # :: n, as we need to merge the halfs back

def merge_split(arr):
    # actual merge_sort function, without error handling
    # :: recursivily called

def merge_array(arr, left, right):
    # combine left and right sides
```
*Tests*
- [x] func exists
- [x] sort 5
- [x] all same
- [x] sort zero array
- [x] sort 1000 random


<!-- ********************* -->
## Quick Sort
- [x] code sort func
- [x] tests
- [x] blog post
### API
```python
def quick_sort(arr):
    # BigO (n log n)
    # :: log n, as this is a divide algo
    # :: n, as we need to merge the halfs back
```
*Tests*
- [x] func exists
- [x] sort 5
- [x] all same
- [x] sort zero array
- [x] sort 1000 random


