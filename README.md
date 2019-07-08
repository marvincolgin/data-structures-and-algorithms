# Reverse an Array

## Challenge
Create a function, which reverses an array/linked-list, as passed via a parameter and pass the new array back as the `return()` for the function.

## Approach & Efficiency
My initial approach was to utilize the `list.insert()` and `list.pop()` to rebuild the list in reverse order. However, my white boarding partner showed me a more pythonic method utilizing slices with a -1 stride.

## Solution
Two solutions were used, one that utilizes a while() loop and is destructive on the inbound array. The second is "pythonic" and utilizes an index slice and a -1 stride.

<!-- Embedded whiteboard image -->
![alt_text](https://github.com/marvincolgin/data-structures-and-algorithyms/blob/array_reverse/challenges/array_reverse/assets/whiteboard.jpg)
![alt_text](https://github.com/marvincolgin/data-structures-and-algorithyms/blob/array_reverse/challenges/array_reverse/assets/whiteboard2.jpg)
