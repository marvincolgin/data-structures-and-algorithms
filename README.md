# Reverse an Array

## Challenge
Create a function, which reverses an array/linked-list, as passed via a parameter and pass the new array back as the `return()` for the function.

## Approach & Efficiency
My initial approach was to utilize the `list.insert()` and `list.pop()` to rebuild the list in reverse order. However, my white boarding partner showed me a more pythonic method utilizing slices with a -1 stride.

## Solution
Two solutions were used, one that utilizes a while() loop and is destructive on the inbound array. The second is "pythonic" and utilizes an index slice and a -1 stride.

<!-- Embedded whiteboard image -->
![alt_text](https://github.com/marvincolgin/data-structures-and-algorythms/blob/array_reverse/challenges/array_reverse/assets/whiteboard.jpg)
![alt_text](https://github.com/marvincolgin/data-structures-and-algorythms/blob/array_reverse/challenges/array_reverse/assets/whiteboard2.jpg)

# Insert and Shift Array
## Challenge
Write a function which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.
## Solution
Create an index into the array where the value will be inserted, utilize slice and .append/.extend to construct a return array

<!-- Embedded whiteboard image -->
![alt_text](https://github.com/marvincolgin/data-structures-and-algorythms/blob/array_shift/challenges/array_shift/assets/whiteboard.jpg)
